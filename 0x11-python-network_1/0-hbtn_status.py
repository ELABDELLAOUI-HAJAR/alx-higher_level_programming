#!/usr/bin/python3
# script that fetches https://alx-intranet.hbtn.io/status
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        body = res.read()
        print("Body response:")
        print("    - type: {}".format(type(body)))
        print("    - content: {}".format(body))
        print("    - utf8 content: {}".format(body.decode("utf-8")))
