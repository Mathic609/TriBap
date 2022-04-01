from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
import os

app = Flask(__name__)
ckeditor = CKEditor(app)
Bootstrap(app)

@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)