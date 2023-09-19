#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def test_index_text():
    return f'<h1>Python Operation with Flask Routing and Views</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
