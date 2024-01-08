import mysql.connector
from mysql.connector import Error

def add_to_sql_database(name,ethnicity,gender,address,occupation,school,major):
    try:
        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="",                    # Enter your database
            user="",                    # Enter your MySQL username
            passwd="",                  # Enter your password to your database
            database=""                 # Enter the database you want to access
        )
        if db.is_connected():
            print('Successfully connected to the database.')
        cursor = db.cursor()

        # Adding information into SQL database
        def adding_info(query):
            cursor.execute(query)
            db.commit()
            print("Successfully Added Information")
        # Adding User into the database
        adding_info(f"INSERT INTO users (name) VALUES ('{name}')")

        # Getting the user ID
        cursor.execute(f"SELECT id FROM users WHERE name = '{name}'")
        results_id = cursor.fetchall()

        # Getting the id of the user
        results_id = results_id[0][0]
        
        # Adding information
        if results_id is not None:
            adding_info(f"INSERT INTO gender_info (gender, users_id) VALUES ('{gender}', {results_id})")
            adding_info(f"INSERT INTO ethnicity_info (ethnicity, users_id) VALUES ('{ethnicity}', {results_id})")
            adding_info(f"INSERT INTO address_info (address, users_id) VALUES ('{address}', {results_id})")
            adding_info(f"INSERT INTO occupation_info (occupation, users_id) VALUES ('{occupation}', {results_id})")
            adding_info(f"INSERT INTO school_info (school, users_id) VALUES ('{school}', {results_id})")
            adding_info(f"INSERT INTO major_info (major, users_id) VALUES ('{major}', {results_id})")


    except Error as e:
        print(f"An error occurred: {e}")
    finally:
        if db.is_connected():
            cursor.close()
            db.close()
            print("MySQL connection is closed")
