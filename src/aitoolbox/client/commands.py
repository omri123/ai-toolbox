import sys
import requests
import argparse

url = "http://127.0.0.1:8000/msg"


def message():
    parser = argparse.ArgumentParser()
    parser.add_argument("msg", type=str)
    args = parser.parse_args()

    with requests.post(url, stream=True, json={"content": args.msg}) as r:
        for chunk in r.iter_content(16):
            sys.stdout.write(chunk.decode("utf-8"))
            sys.stdout.flush()
        print("")
