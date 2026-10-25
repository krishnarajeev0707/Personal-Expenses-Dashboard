# Personal Expense Tracker

A Streamlit-powered application for analyzing personal finances and tracking expenses through interactive dashboards and visualizations.

## Features

### Data Processing
- Upload bank statements in CSV format
- Automatically normalize column names across different CSV formats
- Convert dates and transaction amounts into appropriate data types
- Handle missing or invalid transaction data
- Identify income and expense transactions

### Financial Analysis
- Calculate total income, total expenses, and net balance change
- Analyze spending patterns across different categories
- Track monthly spending trends
- Filter transactions by category and month
- Display filtered transaction data in a structured table

### Data Visualization
- Category-wise expense breakdown using bar charts
- Monthly expense trends using line plots
- Interactive dashboard with financial summaries
- Custom-styled charts integrated into the dashboard interface

### Performance and Interface
- Interactive web interface built with Streamlit
- Organized dashboard layout with summary cards and tabs
- Cached data processing to reduce unnecessary recalculations

## Tech Stack

- **Programming Language:** Python
- **Web Framework:** Streamlit
- **Data Processing:** Pandas
- **Data Visualization:** Matplotlib

## Getting Started

### Prerequisites
- Python 3.x
- pip package manager

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/personal-expense-tracker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd personal-expense-tracker
   ```

3. Install the required libraries:

   ```bash
   pip install streamlit pandas matplotlib
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

   Replace `app.py` with the actual name of the main Python file if it differs.

5. Upload a bank statement in CSV format to explore the dashboard.


## Purpose

This project was developed as a college mini-project to explore data processing, financial analysis, and interactive data visualization using Python. It demonstrates how raw transaction data can be transformed into meaningful financial summaries and visual insights.

## Future Improvements

- Add budget setting and expense limit tracking
- Support additional bank statement formats
- Export financial summaries and reports
- Add more detailed financial analytics

## Team

Developed as a college mini-project under the guidance of **Dr. Neha Sathe**.

## References

- [Python Documentation](https://docs.python.org/3/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/users/index.html)

## License

This project is intended for educational and personal reference purposes.
