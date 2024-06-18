from v_format.v_api import v_format
from flask import render_template

@v_format.route('/')
def home():
    return render_template(
        'index.html'
        )