import mysql.connector
from mysql.connector import Error

def edit_sql_database(name,info_type,info):
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

        # Getting the user ID
        cursor.execute(f"SELECT id FROM users WHERE name = '{name}'")
        results_id = cursor.fetchall()

        # Getting the id of the user
        results_id = results_id[0][0]

        if info_type == "Address":
            cursor.execute(f"UPDATE address_info SET address = '{info}' WHERE id = {results_id}")
            db.commit()
            print(f"Updated {info_type}")

        elif info_type == "Age":
            cursor.execute(f"UPDATE age_info SET age = '{info}' WHERE id = {results_id}")
            db.commit()
            print(f"Updated {info_type}")

        elif info_type == "Ethnicity":
            cursor.execute(f"UPDATE ethnicity_info SET ethnicity = '{info}' WHERE id = {results_id}")
            db.commit()
            print(f"Updated {info_type}")

        elif info_type == "Gender":
            cursor.execute(f"UPDATE gender_info SET gender = '{info}' WHERE id = {results_id}")
            db.commit()
            print(f"Updated {info_type}")
        
        elif info_type == "Major":
            cursor.execute(f"UPDATE major_info SET major = '{info}' WHERE id = {results_id}")
            db.commit()
            print(f"Updated {info_type}")
        
        elif info_type == "Occupation":
            cursor.execute(f"UPDATE occupation_info SET occupation = '{info}' WHERE id = {results_id}")
            db.commit()
            print(f"Updated {info_type}")
        
        elif info_type == "Phone Number":
            cursor.execute(f"UPDATE phone_number_info SET phone_number = '{info}' WHERE id = {results_id}")
            db.commit()
            print(f"Updated {info_type}")
        
        elif info_type == "School":
            cursor.execute(f"UPDATE school_info SET school = '{info}' WHERE id = {results_id}")
            db.commit()
            print(f"Updated {info_type}")
        
        else:
            print("No match")
        
    except Error as e:
        print(f"An error occurred: {e}")
    finally:
        if db.is_connected():
            cursor.close()
            db.close()
            print("MySQL connection is closed")
