from flask import Flask

# from aitoolbox.server.state import ConvesationState


def main():
    app = Flask(__name__)
    # conversation = ConvesationState()

    @app.route("/msg")
    def msg():
        return "Hello, World!"

    app.run()
