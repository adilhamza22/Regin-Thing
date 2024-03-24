import os
import sqlite3
import logging
import subprocess

# Configure logging
logging.basicConfig(level=logging.INFO)

def display_logo():
    logo = """
  _____            _        _______ _     _             
 |  __ \          (_)      |__   __| |   (_)            
 | |__) |___  __ _ _ _ __     | |  | |__  _ _ __   __ _ 
 |  _  // _ \/ _` | | '_ \    | |  | '_ \| | '_ \ / _` |
 | | \ \  __/ (_| | | | | |   | |  | | | | | | | | (_| |
 |_|  \_\___|\__, |_|_| |_|   |_|  |_| |_|_|_| |_|\__, |
              __/ |                                __/ |
             |___/                                |___/ 
"""
    print(logo)

def view_top_10_from_database():
    # Connect to SQLite database
    conn = sqlite3.connect('courses.db')
    c = conn.cursor()
    
    # Retrieve top 10 course information from the database
    c.execute("SELECT * FROM courses LIMIT 10")
    top_10_courses = c.fetchall()
    
    # Log top 10 courses to console
    logging.info("Top 10 courses in the database:")
    for course in top_10_courses:
        logging.info(course)
    
    # Close connection
    conn.close()

def view_bottom_from_database():
    # Connect to SQLite database
    conn = sqlite3.connect('courses.db')
    c = conn.cursor()
    
    # Retrieve total number of entries in the database
    c.execute("SELECT COUNT(*) FROM courses")
    total_entries = c.fetchone()[0]
    
    # Retrieve bottom 10 course information from the database
    c.execute("SELECT * FROM courses ORDER BY ROWID DESC LIMIT 10")
    bottom_10_courses = c.fetchall()
    
    # Log bottom 10 courses to console
    logging.info("Bottom 10 courses in the database:")
    for course in bottom_10_courses:
        logging.info(course)
    
    # Close connection
    conn.close()

def view_all_from_database():
    # Connect to SQLite database
    conn = sqlite3.connect('courses.db')
    c = conn.cursor()
    
    # Retrieve all course information from the database
    c.execute("SELECT * FROM courses")
    all_courses = c.fetchall()
    
    # Log all courses to console
    logging.info("All courses in the database:")
    for course in all_courses:
        logging.info(course)
    
    # Close connection
    conn.close()

def run_crawlers():
    logging.info("Running crawlers...")
    subprocess.run(["python", "main_crawler.py"])

def main():
    display_logo()
    
    while True:
        print("\nChoose an option:")
        print("1. View top 10 elements of the database")
        print("2. View bottom 10 elements of the database")
        print("3. View all entries in the database")
        print("4. Run the crawlers")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            view_top_10_from_database()
        elif choice == "2":
            view_bottom_from_database()
        elif choice == "3":
            view_all_from_database()
        elif choice == "4":
            run_crawlers()
        elif choice == "5":
            logging.info("Exiting the program.") 
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
