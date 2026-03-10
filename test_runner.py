from selenium import webdriver
from generator import generate_test_cases
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

print("Browser opened successfully!\n")

test_cases = generate_test_cases()

results = []

for i, test in enumerate(test_cases):

    username = test["username"]
    password = test["password"]

    # Simple validation rules
    if username == "" or password == "":
        status = "FAIL"

    elif len(password) < 4:
        status = "FAIL"

    else:
        status = "PASS"

    results.append((i+1, username, password, status))

# Print test report
print("\nTEST REPORT")
print("---------------------------------------------")
print("ID | Username | Password | Status")
print("---------------------------------------------")

for r in results:
    print(r[0], "|", r[1], "|", r[2], "|", r[3])

time.sleep(5)

driver.quit()