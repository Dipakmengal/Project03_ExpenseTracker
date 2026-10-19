# 💸 Personal Expense Tracker with CSV

A beginner-friendly Python project that helps users record, manage, and analyze their daily expenses using CSV file storage. This project is developed as part of my Python internship tasks.

## 🚀 Live Demo

Try the Personal Expense Tracker here:

**[Open Live Demo](https://project03expensetracker-bc4pilyp5be9rcyktj7xim.streamlit.app/)**

## 💻 Source Code

[View this project on GitHub](https://github.com/Dipakmengal/Project03_ExpenseTracker)


## 📌 Project Overview

The Personal Expense Tracker allows users to add expenses, view all recorded transactions, filter expenses by category or date, and generate category-wise spending summaries. All expense records are stored in a CSV file for persistent storage.

## ✨ Features

- ➕ **Add Expenses:** Record the date, category, amount, and description of each expense.
- 📋 **View Expenses:** Display all saved expense records in a table.
- 🔍 **Filter Expenses:** Filter transactions by category and date.
- 📊 **Category Summary:** Calculate and visualize total spending by category.
- 💾 **CSV Storage:** Save expense records permanently in `expenses.csv`.
- 📥 **Download CSV:** Download expense data for further use.
- 📈 **Spending Overview:** View total spending, transaction count, and number of categories.
- 🖥️ **Interactive Web Interface:** Use the application through a browser with Streamlit.

## 🛠️ Technologies Used

- Python 3
- Streamlit
- CSV module
- Pandas
- Datetime module
- pathlib module

## 📂 Project Structure

```text
Project03_ExpenseTracker/
├── app.py
├── expenses.csv
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Install Python

Download and install Python 3 from:

https://www.python.org/downloads/

### 2. Clone the Repository


```bash
git clone https://github.com/Dipakmengal/Project03_ExpenseTracker.git
```

### 3. Open the Project Folder

```bash
cd Project03_ExpenseTracker
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Application

```bash
python -m streamlit run app.py
```

### 6. Open in Your Browser

Open the local URL displayed in the terminal. Usually:

http://localhost:8501

## 🚀 How to Use

1. Start the application.
2. Open the **Add Expense** tab.
3. Enter the date, category, amount, and description.
4. Click **Save expense** to store the record.
5. Open **All Expenses** to view saved transactions.
6. Use the **Filter** tab to search by category or date.
7. Open **Category Summary** to view category-wise spending totals and a bar chart.
8. Download your expense records as a CSV file when needed.

## 📄 CSV Data Storage

Expenses are stored in `expenses.csv` with the following columns:

| Column | Description |
|---|---|
| date | Date of the expense |
| category | Expense category |
| amount | Expense amount |
| description | Details of the expense |

Example:

```csv
date,category,amount,description
2026-10-19,Food,250.00,Lunch
2026-10-19,Travel,100.00,Bus fare
2026-10-19,Food,150.00,Dinner
```

## 🎯 Learning Objectives

- Understand CSV file reading and writing in Python.
- Learn how to store structured data persistently.
- Practice Python functions and conditional statements.
- Filter and process records using Python.
- Calculate category-wise statistics.
- Build an interactive web application using Streamlit.
- Display data using tables and charts.

## 🔮 Future Enhancements

- Add monthly expense reports.
- Set budgets for different categories.
- Add expense editing and deletion.
- Export reports to Excel or PDF.
- Add charts showing monthly spending trends.

## 👨‍💻 Author

**Dipak Mengal**

GitHub: https://github.com/Dipakmengal

## 📜 License

This project is intended for educational and learning purposes.
