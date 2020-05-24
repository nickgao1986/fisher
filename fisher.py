from flask import Flask, make_response, jsonify
from config import DEBUG
import json
from yushu_book import YuShuBook
from app import create_app

app = create_app()

app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
