# -*- encoding: utf-8 -*-
"""
Author: Connor Schultz
Date: 03/07/2020

Basic routing program using Flask.
"""
# Python Modules
import os, logging 

# Flask Modules
from flask import render_template

# App Modules
from app import app

# Mapping Modules
import folium
import geopandas as gpd

import json
import requests


# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):

	try:
		# try to match the pages defined in -> pages/<input file>
		return render_template( 'pages/'+path, iframe = 'map.html')

	except:
		# return 404 error page
		return render_template( 'pages/error-404.html' )