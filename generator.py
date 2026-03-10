import random
import string

def generate_test_cases():

    test_cases = []

    # Rule 1: Empty fields
    test_cases.append({"username": "", "password": "123456"})
    test_cases.append({"username": "user1", "password": ""})

    # Rule 2: Very short password
    test_cases.append({"username": "user1", "password": "12"})

    # Rule 3: Very long username
    test_cases.append({"username": "verylongusername123456", "password": "123456"})

    # Rule 4: Random valid usernames
    for i in range(5):
        username = "user" + str(random.randint(100,999))
        password = "pass" + str(random.randint(1000,9999))
        test_cases.append({"username": username, "password": password})

    # Rule 5: Special characters
    test_cases.append({"username": "admin!", "password": "123456"})
    test_cases.append({"username": "@user#", "password": "password123"})

    # Rule 6: Random edge cases
    for i in range(10):
        username = ''.join(random.choices(string.ascii_letters, k=5))
        password = ''.join(random.choices(string.digits, k=6))
        test_cases.append({"username": username, "password": password})

    return test_cases