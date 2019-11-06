import json

import requests


def login():
    # url = "http://172.18.6.74:5000/course/allCourseList"
    # url = "http://127.0.0.1:5000/3"
    post_data = {
        "username": "123",
        "password": "abc"
    }
    response = requests.request("POST", url, data=post_data)
    print(response.text)


if __name__ == "__main__":
    login()
