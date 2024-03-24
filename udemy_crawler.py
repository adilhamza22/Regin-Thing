import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

def crawl_udemy(page_number):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    gecko_driver_path = os.path.join(current_directory, "geckodriver.exe")
    
    options = Options()
    options.headless = True
    
    service = Service(gecko_driver_path)
    driver = webdriver.Firefox(service=service, options=options)
    
    url = f"https://www.udemy.com/courses/search/?p={page_number}&q=business+development+courses&src=ukw"
    driver.get(url)
    time.sleep(5)  # Wait for dynamic content to load

    course_info = []
    course_cards = driver.find_elements(By.CLASS_NAME, "course-card-module--container--3oS-F")
    for card in course_cards:
        title = card.find_element(By.CLASS_NAME, "ud-heading-md.course-card-title-module--course-title--wmFXN").text.strip()
        try:
            ratings = card.find_element(By.CSS_SELECTOR, "span[data-testid='seo-rating']").text.strip().split()[1]
        except IndexError:
            ratings = "N/A"  # Assign a default value if rating is not available
        duration = card.find_element(By.CSS_SELECTOR, "span[data-testid='seo-content-info']").text.strip()
        course_info.append({"name": title, "ratings": ratings, "duration": duration})
    
    # Close the WebDriver session
    driver.quit()
    
    return course_info

def crawl_udemy_courses(pages):
    udemy_courses = []    
    for page_number in range(1, pages + 1):
        udemy_courses.extend(crawl_udemy(page_number))
        print(f"Scraped page {page_number}")
    
    # Printing course information
    for course in udemy_courses:
        print(course)
    
    return udemy_courses
