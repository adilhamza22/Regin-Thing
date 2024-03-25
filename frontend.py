from flask import Flask, render_template, request
from coursera_crawler import crawl_coursera  # Assuming coursera_crawler.py is in the same directory
from udemy_crawler import crawl_udemy  # Assuming udemy_crawler.py is in the same directory
from harvard_crawler import crawl_harvard_courses  # Assuming harvard_crawler.py is in the same directory
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")  # Render the HTML template

@app.route("/crawl", methods=["POST"])
def crawl():
    # Retrieve platform selection from the form
    platform = request.form.get("platform")

    if platform == "coursera":
        courses = crawl_coursera()  
    elif platform == "udemy":
        courses = crawl_udemy()  
    elif platform == "harvard":
        courses = crawl_harvard_courses()  
    else:
        courses = None  # Handle invalid selections

    # Return the list of courses as JSON data
    return {"courses": courses}

if __name__ == "__main__":
    app.run(debug=True,port =3000)  # Run the Flask app in debug mode for development
