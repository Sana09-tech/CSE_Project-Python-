## Project Title

**Python Console Expense Tracker**

## Overview of the Project

The Python Console Expense Tracker is a simple, command-line application designed to help individuals monitor and manage their daily spending. It allows users to easily **add, view, and summarize** their financial expenditures.

The application leverages Python's standard libraries, including `csv` for file handling and `datetime` for date management, ensuring all expense data is saved persistently to a local file (`expenses.csv`) and automatically loaded upon startup. This makes it a lightweight, portable, and effective tool for basic personal finance tracking.

## Features

  * **Add Expense:** Users can quickly log new expenses by providing the **amount**, **category** (e.g., Food, Rent), **description**, and **date**.
  
  * **Persistent Storage:** All data is automatically saved to and loaded from a local **`expenses.csv`** file, ensuring data integrity between sessions.
  
  * **View Expenses:** Displays a formatted, detailed list of all recorded expenditures, including date, category, amount, and description.
  
  * **Expense Summary:** Calculates and displays the **total amount spent** and a detailed **breakdown of spending by category**.
  
  * **Input Validation:** Ensures the expense amount entered is a positive numerical value.

## Technologies/Tools Used

| Technology | Purpose |
| :--- | :--- |
| **Python 3.x** | The core programming language used to build the application logic. |
| **`csv` Module** | Used for reading from and writing to the persistent `expenses.csv` file. |
| **`datetime` Module** | Used for managing and validating expense dates. |
| **`os` Module** | Used to check for the existence of the `expenses.csv` file. |

## Steps to Install & Run the Project

### Prerequisites

You need **Python 3.x** installed on your system. You can verify your installation by running:

```bash
python --version
# or
python3 --version
```

### Installation

1.  **Clone the Repository (or Download the Code):**

    ```bash
    git clone https://github.com/your-username/expense-tracker-repo.git
    cd expense-tracker-repo
    ```

    *(Note: Since this is a single file, you can also just save the code as `tracker.py`.)*

2.  **No dependencies are required** (it uses only standard Python libraries).

### Running the Application

Execute the script directly from your terminal:

```bash
python tracker.py
# or
python3 tracker.py
```

The application will start, display the main menu, and begin tracking your expenses. If the `expenses.csv` file doesn't exist, it will be created automatically upon adding the first expense.

## Instructions for Testing

Since this is a console application, testing is done interactively through the main menu.

### Test Scenarios

1.  **Initial Run Test:**

      * Run `python tracker.py`.
      * **Expected Result:** The welcome message and the main menu (options 1-4) should display. The application should start without errors.

2.  **Add Expense Test (Option 1):**

      * Select **1** (Add a new expense).
      * Enter a **positive number** for the amount (e.g., `25.50`).
      * Enter a **category** (e.g., `Dinner`).
      * Enter a **description** (e.g., `Pizza night`).
      * **Expected Result:** The message "✅ Expense added and saved successfully\!" should appear, and the program should return to the main menu.

3.  **View Expenses Test (Option 2):**

      * Select **2** (View all expenses).
      * **Expected Result:** The expense added in the previous step should be displayed in a formatted table.

4.  **Summarize Expenses Test (Option 3):**

      * Add a second expense in the *same category* (e.g., Amount: `10.00`, Category: `Dinner`).
      * Select **3** (Summarize expenses).
      * **Expected Result:**
          * The **Total Spent** should be the sum of both expenses (`35.50`).
          * The **Spending by Category** section should show the category `Dinner` totaling `35.50`.

5.  **Exit Test (Option 4):**

      * Select **4** (Exit and save).
      * **Expected Result:** The message "Goodbye\! All data is saved to expenses.csv." should appear, and the program should terminate.
      * Verify that the `expenses.csv` file in the directory contains the two expense records
