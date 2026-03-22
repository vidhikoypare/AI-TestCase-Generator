from flask import Flask, render_template, request
import re
from selenium import webdriver
import time

app = Flask(__name__)

# ---------------- AI RULE-BASED EXPERT SYSTEM ----------------
def evaluate_test_case(username, password):

    # State S1
    if username == "":
        return "FAIL: Username cannot be empty"

    # State S2
    if password == "":
        return "FAIL: Password cannot be empty"

    # State S3
    if len(username) < 3:
        return "FAIL: Username too short"

    # State S4
    if len(username) > 15:
        return "FAIL: Username too long"

    # State S5
    if not username.isalnum():
        return "FAIL: Username must be alphanumeric"

    # State S6
    if len(password) < 6:
        return "FAIL: Password too short"

    # State S7
    if not re.search(r"[A-Z]", password):
        return "FAIL: Must include uppercase letter"

    # State S8
    if not re.search(r"[a-z]", password):
        return "FAIL: Must include lowercase letter"

    # State S9
    if not re.search(r"[0-9]", password):
        return "FAIL: Must include number"

    # State S10
    if not re.search(r"[!@#$%^&*]", password):
        return "FAIL: Must include special character"

    # State S11
    return "PASS: Strong credentials"


# ---------------- TEST CASE GENERATOR ----------------
def generate_test_cases():

    return [
        {"username": "", "password": "123456", "result": "FAIL"},
        {"username": "user1", "password": "", "result": "FAIL"},
        {"username": "ab", "password": "Password1!", "result": "FAIL"},
        {"username": "user@123", "password": "Password1!", "result": "FAIL"},
        {"username": "user1", "password": "pass", "result": "FAIL"},
        {"username": "user1", "password": "password1!", "result": "FAIL"},
        {"username": "user1", "password": "Password1!", "result": "PASS"},
        {"username": "admin01", "password": "Admin@123", "result": "PASS"},
        {"username": "vidhi99", "password": "StrongPass9#", "result": "PASS"}
    ]


# ---------------- SELENIUM DEMO ----------------
def run_selenium_demo():

    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(2)
    driver.quit()


# ---------------- FLASK ROUTE ----------------
@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    test_cases = []

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        action = request.form.get("action")

        if action == "run":
            result = evaluate_test_case(username, password)
            run_selenium_demo()

        elif action == "generate":
            test_cases = generate_test_cases()

    return render_template("index.html", result=result, test_cases=test_cases)


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)