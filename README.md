## **StockTracker**

StockTracker is a web application designed to help employees manage stocks efficiently. It simplifies Stock tracking and provides alerts for low stock quantities, enabling businesses to avoid inventory shortages and ensure smooth operations.

## Table of Contents
- [Introduction](#Introduction)
- [Prerequisites](#Prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Conclusion](#Conclusion)


## **Introduction**

StockTracker is a comprehensive stock management solution developed using Python Django. It was created to address the challenges businesses face in inventory tracking and management. Key features include:

- User authentication (SignUp and SignIn functionality).

- Stock tracking with low stock alerts.

- An intuitive and responsive user interface.

This application is designed to streamline Stock processes and enhance productivity.

## Prerequisites
- Node.js 14.x or higher
- Python 3.8 or higher
- Windows, macOS, or Linux operating system


## **Installation**

To install Project Title, follow these steps:

1. Clone the repository: **`https://github.com/moatez-ouislati/StockTracker.git`**
2. Navigate to the project directory: **`cd stock-tracker`**
3. activate virtual env For macOS/Linux: **`source env/bin/activate`**
4. activate virtual env For Windows: **`.\env\Scripts\activate`**
5. Configure the database in the settings.py file
6. Apply migrations: **`python manage.py migrate`**
7. Start the project: **`py manage.py runserver`**

## **Usage**

To use StockTracker:

1. Sign Up:

  - Visit http://127.0.0.1:8000/ in your web browser.

  - Click on the "Sign Up" button on the homepage.

Fill in your details (username, email, password) and submit the form.

2. Sign In:

  - Navigate to the "Sign In" page.

  - Enter your credentials (username and password) and log in.

3. Manage Stock Items:

  - Once logged in, access the "Dashboard".

  - Use the following features to manage stock items:

- Add Items:

  - Click on the "Add Item" button.

  - Fill out the form with item details (name, quantity, description, etc.).

  - Submit the form to save the item.

- Update Items:

  - Locate the item you want to update from the list.

  - Click the "Edit" button next to the item.

  - Modify the details as needed and save the changes.

- Delete Items:

  - Locate the item you want to remove.

  - Click the "Delete" button next to the item.

  - Confirm the deletion in the pop-up dialog.

4. Monitor Stock Levels:

  - View the list of items and their quantities on the dashboard.

  - Receive alerts or notifications for items with low stock quantities.

## **Conclusion**

This README provides the necessary details for understanding, installing, and contributing to the StockTracker project. Customize it further to reflect additional features or updates as the application evolves.
