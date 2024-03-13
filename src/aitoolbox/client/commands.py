import sys
import requests
import argparse

url = "http://127.0.0.1:8000/"


def message():
    parser = argparse.ArgumentParser()
    parser.add_argument("msg", type=str)
    parser.add_argument("--forget", action="store_true",
                        help="don't add to chat history.")
    parser.add_argument("--prompt", type=str,
                        default="You are an helpful chatbot.",
                        help="The system message presented to the chatbot.")
    args = parser.parse_args()

    body = {"content": args.msg, "forget": args.forget, "prompt": args.prompt}
    with requests.post(url + "msg", stream=True, json=body) as r:
        for chunk in r.iter_content(16):
            sys.stdout.write(chunk.decode("utf-8"))
            sys.stdout.flush()
        print("")


def history():
    with requests.get(url + "history") as r:
        print(r.content.decode("utf-8"))
