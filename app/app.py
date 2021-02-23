# Imports
from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
import os
import pymongo

from config import DevelopmentConfig
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'pic/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

client = pymongo.MongoClient(
    "mongodb+srv://user1:2NvZYRipodUWsipy@cluster1.swpth.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
db = client.chal48_passion_froid
col = db.picture