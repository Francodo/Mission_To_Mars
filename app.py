from flask import flask, render_template
from flask_pymongo import PyMongo
from flask import Flask, jsonify
from bs4 import BeautifulSoup as soup
from splinter import Browser
import scraping

import datetime as dt
import numpy as np
import pandas as pd

app = Flask(__name__)  
                               
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")                                 # This Flask instance tells Flask what to dispalay
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced")
def cerberus():
   mars = mongo.db.mars                         # Define a variable that points to Mongo DB
   mars_data = scraping.scrape_all()            # Create a variable to hold scraped data 
   mars.update({}, mars_data, upsert=True)      # Update the database.Use data in mars_data,Ask Mongodb to create a new document
   return                                       # Let us know if scraping is successful

@app.route("/https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced")
def schiaparelli():
   mars = mongo.db.mars                         # Define a variable that points to Mongo DB
   mars_data = scraping.scrape_all()            # Create a variable to hold scraped data 
   mars.update({}, mars_data, upsert=True)      # Update the database.Use data in mars_data,Ask Mongodb to create a new document
   return                                       # Let us know if scraping is successful

app.route("/https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced")
def syrtis_major():
   mars = mongo.db.mars                         # Define a variable that points to Mongo DB
   mars_data = scraping.scrape_all()            # Create a variable to hold scraped data 
   mars.update({}, mars_data, upsert=True)      # Update the database.Use data in mars_data,Ask Mongodb to create a new document
   return                                       # Let us know if scraping is successful

app.route("/https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced")
def valles_marineris():
   mars = mongo.db.mars                         # Define a variable that points to Mongo DB
   mars_data = scraping.scrape_all()            # Create a variable to hold scraped data 
   mars.update({}, mars_data, upsert=True)      # Update the database.Use data in mars_data,Ask Mongodb to create a new document
   return                                       # Let us know if scraping is successful

@app.route("/scrape")
def scrape():                                   # Create and define a function
   mars = mongo.db.mars                         # Define a variable that points to Mongo DB
   mars_data = scraping.scrape_all()            # Create a variable to hold scraped data 
   mars.update({}, mars_data, upsert=True)      # Update the database.Use data in mars_data,Ask Mongodb to create a new document
   return "Scraping Successful!"                # Let us know if scraping is successful



if __name__ == '__main__':
    app.run()