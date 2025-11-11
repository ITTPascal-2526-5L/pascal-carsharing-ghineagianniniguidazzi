from flask import Blueprint, render_template,redirect
import json

login_bp = Blueprint("login", __name__)

@login_bp.route("/login_driver", request=['GET','POST'])
def login_driver():
    pass
