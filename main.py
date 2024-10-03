import mysql.connector
import streamlit as st

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",         
            user="root",   
            password="", 
            database="sleep_apnea"  
        )
        if connection.is_connected():
            st.success("Successfully connected to the database")
        return connection
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None

def fetch_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sleep")  
    rows = cursor.fetchall()

    if rows:
        st.write("Data from the table:")
        for row in rows:
            st.write(row)
    else:
        st.warning("No data found")
    cursor.close()


def main():
    st.title("Streamlit and MySQL Integration")
    
    connection = create_connection()
    
    if connection:
        fetch_data(connection)
        connection.close()

if __name__ == "__main__":
    main()
