#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def single_route():
    """Define a single route"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
