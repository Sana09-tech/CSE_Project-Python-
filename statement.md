## Project Statement

The lack of a simple, quick, and accessible tool makes it difficult for individuals to track, record, and categorize their daily expenditures effectively. 

This common oversight leads to poor personal financial awareness, difficulty in adhering to a budget, and an inability to easily identify areas of potential cost-saving or overspending.

A solution is needed that provides a low-friction method for logging expenses and generating immediate, actionable spending summaries.

## Scope of the Project

The project scope is limited to a single-user, command-line interface (CLI) application built entirely in standard Python.

In Scope:

Recording and managing expense records (date, category, amount, description).

Data persistence using a local CSV file (expenses.csv).

Generating basic financial summaries (total spent and category-wise breakdown).

Input validation for monetary amounts and basic date formatting.

Out of Scope (Future Enhancements):

Graphical User Interface (GUI).

Multi-user support, authentication, or roles.

Advanced budgeting, forecasting, or reporting features (e.g., monthly limits, trend analysis).

Integration with external financial accounts or APIs.

Features like deleting or modifying existing expense records.

## Target Users
The primary target users are individuals seeking a simple, private, and efficient way to track personal finances without the complexity of full-featured financial software.

Students: Need a quick way to track monthly spending against a limited budget.

Individuals New to Budgeting: Require a low-barrier-to-entry tool to start monitoring spending habits.

Developers/Power Users: Prefer command-line tools for quick, keyboard-driven data entry and analysis.

## High-Level Features
Expense Logging: Allow the user to record new expenditures with essential details: Amount, Category, Description, and Date.

Data Persistence: Automatically load and save all expense data to a local file (expenses.csv) to ensure records are preserved between sessions.

Expense Listing: Provide a clear, formatted display of all recorded expenses for review.

Financial Summarization: Calculate and present an aggregated summary showing:

The total amount spent across all categories.

The total spending broken down for each unique category.
