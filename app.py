import csv
from pathlib import Path
from datetime import datetime
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Personal Expense Tracker", page_icon="💸", layout="wide")
DATA_FILE = Path(__file__).with_name("expenses.csv")
FIELDS = ["date", "category", "amount", "description"]

def initialize_file():
    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        with DATA_FILE.open("w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=FIELDS).writeheader()

def load_expenses():
    initialize_file()
    with DATA_FILE.open("r", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row["amount"] = float(row["amount"])
    return rows

def save_expense(date, category, amount, description):
    with DATA_FILE.open("a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=FIELDS).writerow({
            "date": date.isoformat(), "category": category,
            "amount": f"{amount:.2f}", "description": description.strip()
        })

initialize_file()
st.title("💸 Personal Expense Tracker")
st.caption("Project 03 • Python + CSV • Record, filter, and summarize daily spending")
rows = load_expenses()
c1, c2, c3 = st.columns(3)
c1.metric("Total spending", f"₹{sum(r['amount'] for r in rows):,.2f}")
c2.metric("Transactions", len(rows))
c3.metric("Categories", len(set(r["category"] for r in rows)))
add_tab, view_tab, filter_tab, summary_tab = st.tabs(["➕ Add Expense", "📋 All Expenses", "🔎 Filter", "📊 Category Summary"])

with add_tab:
    st.subheader("Add a new expense")
    with st.form("add_expense_form", clear_on_submit=True):
        date = st.date_input("Date", value=datetime.now().date())
        category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Health", "Education", "Entertainment", "Other"])
        amount = st.number_input("Amount (₹)", min_value=0.01, value=100.0, step=10.0)
        description = st.text_input("Description", placeholder="e.g., Lunch, bus fare, groceries")
        submitted = st.form_submit_button("Save expense", type="primary")
        if submitted:
            save_expense(date, category, amount, description)
            st.success("Expense saved to expenses.csv!")
            st.rerun()
    st.info("Expenses are stored locally in expenses.csv and persist after restarting the app.")

with view_tab:
    current = load_expenses()
    st.subheader("All recorded expenses")
    if current:
        df = pd.DataFrame(current).rename(columns={"date":"Date","category":"Category","amount":"Amount (₹)","description":"Description"})
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.download_button("⬇️ Download CSV", data=DATA_FILE.read_bytes(), file_name="expenses.csv", mime="text/csv")
    else:
        st.info("No expenses yet. Add your first expense.")

with filter_tab:
    current = load_expenses()
    st.subheader("Filter expenses")
    if current:
        categories = ["All"] + sorted(set(r["category"] for r in current))
        left, right = st.columns(2)
        selected = left.selectbox("Category", categories)
        selected_date = right.date_input("Date (optional)", value=None, key="filter_date")
        filtered = current
        if selected != "All":
            filtered = [r for r in filtered if r["category"] == selected]
        if selected_date:
            filtered = [r for r in filtered if r["date"] == selected_date.isoformat()]
        if filtered:
            st.dataframe(pd.DataFrame(filtered).rename(columns={"date":"Date","category":"Category","amount":"Amount (₹)","description":"Description"}), use_container_width=True, hide_index=True)
            st.metric("Filtered total", f"₹{sum(r['amount'] for r in filtered):,.2f}")
        else:
            st.warning("No expenses match those filters.")
    else:
        st.info("Add an expense first to use filters.")

with summary_tab:
    current = load_expenses()
    st.subheader("Category summary")
    if current:
        totals = {}
        for row in current:
            totals[row["category"]] = totals.get(row["category"], 0) + row["amount"]
        summary = pd.DataFrame([{"Category": k, "Total (₹)": v} for k, v in sorted(totals.items())])
        st.bar_chart(summary, x="Category", y="Total (₹)")
        st.dataframe(summary, use_container_width=True, hide_index=True)
    else:
        st.info("No expenses available for summary yet.")

st.divider()
st.caption("Built with Python's csv module and Streamlit. Currency: INR (₹).")
