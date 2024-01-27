# Data_Pipeline_Project: Ticket Sales Database Uploader
This repository consists of a Python script for creating a basic data pipeline using Python's database connector. This Python script allows you to upload ticket sales data from a CSV file into a SQL database using the MySQL Python Connector library.

## Prerequisites

Before running the script, make sure you have the following installed:

1. **MySQL Python Connector:**
   - Install the MySQL Python Connector by running the following command:
     ```
     pip3 install mysql-connector-python
     ```

2. **MySQL Database:**
   - If you don't have MySQL installed, [download and install MySQL](https://dev.mysql.com/downloads/installer/).
   - Set up your MySQL database server.

## Database Setup

1. **Create a Database:**
   - Open your MySQL command-line client or a MySQL GUI tool. 
   - Execute the following SQL command to create a new database:
     ```
     CREATE DATABASE Event_Ticket_Sales;
     ```

2. **Create Table and Columns:**
   - Execute the following SQL command to create the `TicketSalesTable` table with the specified schema:
     ```sql
     USE Event_Ticket_Sales;

     CREATE TABLE TicketSalesTable (
         ticket_id INT,
         trans_date DATE,
         event_id INT,
         event_name VARCHAR(50),
         event_date DATE,
         event_type VARCHAR(10),
         event_city VARCHAR(20),
         customer_id INT,
         price DECIMAL,
         num_tickets INT
     );
     ```

## Running the Script

1. **Download the CSV File:**
   - [Download the CSV dataset]() containing ticket sales data.
   - Save the CSV file in the same directory as the Python script.

2. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing the Python script.
   - Run the script using the following command:
     ```bash
     python your_script.py /path/to/you/csv_file
     ```
   - If you have a different Python version, replace `python` with `python3`.

3. **Provide CSV File Path (Optional):**
   - If you want to use a different CSV file, you can provide the file path as a command-line argument:
     ```bash
     python your_script.py --csv /path/to/your/csv/file.csv
     ```

4. **View Results:**
   - The script will upload the data from the CSV file to the `TicketSalesTable` table in the MySQL database.
   - You can run queries to view the results or analyze the data in your MySQL database.
   - 

## Contributor

- Shilpa Hegde


