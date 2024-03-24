# Business Development Courses Crawler

This project is a web scraping application that crawls various online platforms to gather information about business development courses. The user can run the `driver.py` file to execute the program.

## Prerequisites

Before running the program, ensure you have the following dependencies installed:

- `selenium`: A Python library used for automating web browser interaction.
- `sqlite3`: A built-in module in Python used for working with SQLite databases.
- `requests`: A Python library used for making HTTP requests.
- `BeautifulSoup`: A Python library used for parsing HTML and XML documents.

You can install these dependencies using pip:

`bash`
pip install selenium sqlite3 requests beautifulsoup4

## How to Run
To run the program, follow these steps:

Clone the repository to your local machine.
Install the required dependencies using pip.
`bash`
Run the driver.py file using Python:
```bash
python driver.py
```
# Program Overview

The program will execute and scrape data from various online platforms, including Coursera, Udemy, and Harvard, storing the information in a SQLite database named `courses.db`.

## Project Structure

The project consists of the following files:

- `driver.py`: Main entry point of the program. Executes the crawlers and stores data in the database.
- `coursera_crawler.py`, `udemy_crawler.py`, `harvard_crawler.py`: Crawler scripts for Coursera, Udemy, and Harvard respectively.
- `database.py`: Contains functions to interact with the SQLite database.
- `README.md`: This file providing an overview of the project and instructions for running it.

## Note

All other files in the repository are for internal use and can be ignored by the user.

