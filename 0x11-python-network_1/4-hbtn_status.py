#!/usr/bin/python3
"""Python script that fetches
https://alx-intranet.hbtn.io/status
by using requests package
"""
import requests


if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
