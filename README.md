
# Pulse — Expense Tracker

A desktop expense tracker built with Python and CustomTkinter to manage expenses and analyze spending.

## Features

- Dashboard showing total spending, today's spending, monthly spending, and transaction count
- Add, edit, and delete expenses
- Search transactions by category, description, date, day, or time
- Filter transactions by today or this month
- Daily, monthly, and annual spending analytics
- Category-wise spending breakdown
- Local JSON storage for expense records
- Input validation for amounts, dates, and times
- Amounts displayed in Indian rupees (₹)

## Built With

- Python
- CustomTkinter
- Tkinter and ttk
- JSON

## Installation

Install the required library:

```bash
python -m pip install customtkinter
```

## Run the Application

Run the Python file from your terminal:

```bash
python main.py
```

Replace `main.py` with your actual Python filename.

## How to Use

1. Open the application.
2. Select **Add Expense** to enter expense details.
3. View spending summaries on the dashboard.
4. Open the transactions section to search, filter, edit, or delete records.
5. Use analytics to review spending by day, month, or year.

## Data Storage

Expense records are stored locally in `expenses.json`. Keep a backup of this file to preserve your expense history.

## Project Structure

```text
Pulse-Expense-Tracker/
├── main.py
├── expenses.json
└── README.md
```

This is an example structure. Replace `main.py` with your actual Python filename. The `expenses.json` file is created by the application when needed.

## Future Improvements

- Export expense reports to CSV
- Add budget limits and alerts
- Add charts for spending trends
- Support recurring expenses
- Add expense data backup and restore

## Author

**Prateesraj K**  
Electronics and Communication Engineering  
Coimbatore Institute of Technology
