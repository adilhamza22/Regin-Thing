import requests
from bs4 import BeautifulSoup
import re
import logging

logging.basicConfig(level=logging.INFO) # Configure logging


def crawl_coursera():
    logging.info(":::::::::SCRAPING ------COURSERA------ STARTED:::::")
    url = "https://www.coursera.org/courses?query=business%20development"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    courses = soup.find_all("a", class_="cds-119 cds-113 cds-115 cds-CommonCard-titleLink css-si869u cds-142")
    course_info = []
    for course in courses:
        label = course.get("aria-label")
        if label:
            label_parts = label.split(',')
            name = label_parts[0].strip()
            ratings = label_parts[1].strip().split()[1]
            duration = ""
            for part in reversed(label_parts):
                match = re.search(r'(\d+)\s*-\s*(\d+)\s*(Hours|Days|Weeks|Months?)|Less\s*Than\s*(\d+)\s*(Hours|Days|Weeks|Months?)', part.strip())
                if match:
                    if match.group(1):  # if matched "X-Y Hours/Days/Weeks/Months"
                        duration = match.group(0)
                    elif match.group(4):  # if matched "Less Than X Hours/Days/Weeks/Months"
                        duration = match.group(0)
                    break
            course_info.append({"name": name, "ratings": ratings, "duration": duration})
    return course_info

# Crawling each website and gathering course information
coursera_courses = crawl_coursera()

# Printing course information
for course in coursera_courses:
    print(course)

