#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(request) as response:
        html_body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html_body)))
        print("\t- content: {}".format(html_body))
        print("\t- utf8 content: {}".format(html_body.decode("utf-8")))
