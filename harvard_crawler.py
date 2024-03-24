from bs4 import BeautifulSoup
import requests

def crawl_harvard_courses():
    url = "https://pll.harvard.edu/subject/business-development"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    course_info = []
    courses = soup.find_all("div", class_="group-details")
    for course in courses:
        name = course.find("div", class_="field--name-title").text.strip()
        price_raw = course.find("div", class_="field---extra-field-pll-extra-field-price").text.strip()
        registration_date_raw = course.find("div", class_="field---extra-field-pll-extra-field-registration-date").text.strip()

        # Extracting only the relevant information from the raw text
        price = price_raw.split("\n")[1].rstrip("*")
        registration_date = registration_date_raw.split("\n")[1]

        course_info.append({"name": name, "price": price, "registration_date": registration_date})
    return course_info

harvard_courses = crawl_harvard_courses()

# Printing course information
for course in harvard_courses:
    print(course)
