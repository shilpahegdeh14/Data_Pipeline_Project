import mysql.connector
import csv
from datetime import datetime
import sys

def get_db_connection(): 
    connection=None 
    try: 
        connection=mysql.connector.connect(
            user='test_user', 
            password='Shils@007', 
            host= '127.0.0.1', 
            port='3306', 
            database='Event_Ticket_Sales'
            ) 
    except Exception as error: 
        print("Error while connecting to database for job tracker",error) 
    return connection

# get_db_connection()

def load_third_party(connection,file_path_csv): 
    # print("Inserting csv file to database")
    try:
        cursor=connection.cursor() 
        #[Iterate through the CSV file and execute insert statement] 
        
        # SQL insert statement
        insert_query = """
        INSERT INTO TicketSalesTable 
        (ticket_id, trans_date, event_id, event_name, event_date, event_type, event_city, customer_id, price, num_tickets) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        #open and read csv file
        with open(file_path_csv, 'r') as csv_file:
            # print(f"Reading CSV file: {file_path_csv}")
            csv_reader = csv.reader(csv_file)
            # next(csv_reader)  # Skip the header row if present

            for row in csv_reader:
                # Convert data types if needed
                ticket_id = int(row[0])
                trans_date = datetime.strptime(row[1],'%m/%d/%y').date() if row[1] else None
                event_id = int(row[2])
                event_name = row[3]
                # Convert the date string to a datetime.date object
                event_date = datetime.strptime(row[4], '%m/%d/%y').date() if row[4] else None
                event_type = row[5]
                event_city = row[6]
                customer_id = int(row[7])
                price = float(row[8])
                num_tickets = int(row[9])

                row_data = (
                    ticket_id, trans_date, event_id, event_name, event_date, event_type, event_city, customer_id, price, num_tickets
                )
                # Execute the insert query
                cursor.execute(insert_query, row_data)
                # print(f"Inserted data: {row_data}")
        connection.commit()
        # print("Committed changes to the database.")
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
     cursor.close()
     # print("Closed database cursor.")
    return

def query_popular_tickets(connection): 
    #Get the most popular ticket in the pastmonth 
    # print("Querying the database:")
    try:
        sql_statement = """ 
                        SELECT
                        event_name,
                        SUM(num_tickets) AS total_tickets_sold
                        FROM
                            Event_Ticket_Sales.TicketSalesTable
                        WHERE
                            YEAR(event_date) = 2020
                        GROUP BY
                            event_name
                        ORDER BY
                            total_tickets_sold DESC
                        LIMIT 3; 
        """
    
        cursor=connection.cursor() 
        # print("Executing the SQL statement")
        cursor.execute(sql_statement) 
        # print("Fetching the Data")
        records = cursor.fetchall() 

        # printing each row in the record set
        print("Here are the most popular tickets in the year 2020:")
        for record in records:
            print(f"- {record[0]}")     
   
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close() 
    return records

def main():
    try:
        connection = get_db_connection()
        # load_third_party(connection, '/Users/shilpa/Documents/Data_Engineer_BootCamp_Projects/Data_pipeline_ticket_sales_mini_project/third_party_sales_1.csv')
        if len(sys.argv) < 2:
            print("Please provide the path to the CSV file.")
            print("Usage: python your_script.py /path/to/your/csv/file.csv")
            sys.exit(1)

        # Get the CSV file path from the command-line argument
        csv_file_path = sys.argv[1]

        connection = get_db_connection()
        load_third_party(connection, csv_file_path)
        query_popular