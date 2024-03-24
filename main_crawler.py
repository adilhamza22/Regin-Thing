# import coursera_crawler
# import udemy_crawler
# import harvard_crawler
# import sqlite3

# def crawl_coursera_courses():
#     # Call the function from coursera_crawler.py to crawl Coursera courses
#     return coursera_crawler.crawl_coursera_courses()

# def crawl_udemy_courses():
#     # Call the function from udemy_crawler.py to crawl Udemy courses
#     return udemy_crawler.crawl_udemy_courses()

# def crawl_harvard_courses():
#     # Call the function from harvard_crawler.py to crawl Harvard courses
#     return harvard_crawler.crawl_harvard_courses()

# def store_in_database(courses):
#     # Connect to SQLite database
#     conn = sqlite3.connect('courses.db')
#     c = conn.cursor()
    
#     # Create a table to store course information
#     c.execute('''CREATE TABLE IF NOT EXISTS courses
#                  (name TEXT, ratings REAL, price TEXT, registration_date TEXT)''')
    
#     # Insert course information into the database
#     for course in courses:
#         c.execute("INSERT INTO courses VALUES (?, ?, ?, ?)", 
#                   (course.get('name'), course.get('ratings'), course.get('price'), course.get('registration_date')))
    
#     # Commit changes and close connection
#     conn.commit()
#     conn.close()

# def main():
#     # Crawl courses from different sources
#     coursera_courses = crawl_coursera_courses()
#     udemy_courses = crawl_udemy_courses()
#     harvard_courses = crawl_harvard_courses()
    
#     # Store course information in the database
#     all_courses = coursera_courses + udemy_courses + harvard_courses
#     store_in_database(all_courses)
    
#     print("Course information stored in the database successfully!")

# if __name__ == "__main__":
#     main()
    


import coursera_crawler
import udemy_crawler
import harvard_crawler
import sqlite3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def crawl_coursera_courses():
    # Call the function from coursera_crawler.py to crawl Coursera courses
    return coursera_crawler.crawl_coursera()

def crawl_udemy_courses():
    logging.info(":::::::::SCRAPING ------UDEMY------ STARTED:::::")    
    # Call the function from udemy_crawler.py to crawl Udemy courses
    return udemy_crawler.crawl_udemy_courses(10)

def crawl_harvard_courses():
    logging.info(":::::::::SCRAPING ------HARVARD------ STARTED:::::")    
    # Call the function from harvard_crawler.py to crawl Harvard courses
    return harvard_crawler.crawl_harvard_courses()

def store_in_database(courses):
    # Connect to SQLite database
    conn = sqlite3.connect('courses.db')
    c = conn.cursor()
    
    # Create a table to store course information
    c.execute('''CREATE TABLE IF NOT EXISTS courses
                 (name TEXT, ratings REAL, price TEXT, registration_date TEXT)''')
    
    # Insert course information into the database
    for course in courses:
        c.execute("INSERT INTO courses VALUES (?, ?, ?, ?)", 
                  (course.get('name'), course.get('ratings'), course.get('price'), course.get('registration_date')))
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

def print_top_10_from_database():
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

def main():
    # Crawl courses from different sources
    coursera_courses = crawl_coursera_courses()
    udemy_courses = crawl_udemy_courses()
    harvard_courses = crawl_harvard_courses()
    
    # Store course information in the database
    all_courses = coursera_courses + udemy_courses + harvard_courses
    store_in_database(all_courses)
    
    # Log top 10 courses from the database
    print_top_10_from_database()
    
    logging.info("Course information stored in the database successfully!")

if __name__ == "__main__":
    main()
