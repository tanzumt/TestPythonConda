import os
import sys

from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template("/templates/index.html")

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
