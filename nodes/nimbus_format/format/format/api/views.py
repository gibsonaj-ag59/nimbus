from format.api import format
from flask import render_template

@format.route('/')
def home():
    return render_template(
        'index.html'
        )