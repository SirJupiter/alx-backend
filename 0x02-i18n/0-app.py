#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template

app = Flask()


@app.route
def single_route():
    """Define a single route"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
