#!/usr/bin/python3
"""Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a
parameter, and finally displays the body of the response
by using requests package
"""
import sys
import requests


if __name__ == "__main__":
    playload = {"email": sys.argv[2]}
    response = requests.post(sys.argv[1], data=playload)
    print(response.text)
