# firewatchBC: CSc 497 Interdisciplinary Project
> By: Connor Schultz

## Project Description

## Build from Sources

1. Install project files
   * Clone sources using `git clone` on this directory
   * Change directories to this directory `cd <path/GISalmon>`
   
2. Install virtualenv modules and activate the virtual environment  
  * **Unix** based systems: 
      * `virtualenv --no-site-packages env`
      * `source env/bin/activate`
   * **Windows** based systems:
      * `virtualenv --no-site-packages env`
      * `.\env\Scripts\activate`
	   
3. Install requirements: 
   * `pip3 install -r requirements.txt`

4. Set FLASK_APP environment variable:
   * **Unix** based systems:
   	  * `export FLASK_APP=run.py`
   * **Windows** based systems:
      * `set FLASK_APP=run.py`

5. Set DEBUG environment:
   * **Unix** based systems:
      *  `export FLASK_ENV=dev`
   * **Windows** based systems:
      *  `set FLASK_ENV=dev`

6. Run!
   * `flask run --host=0.0.0.0 --port=5000`

<br />

## Deployment
The app is provided with configuration to be executed in [Docker](https://www.docker.com/) and [Gunicorn](https://gunicorn.org/).

<br />

### [Docker](https://www.docker.com/) execution
---


1. `sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d`


2. Go to `http://localhost:5005` in browser.

<br />

### [Gunicorn](https://gunicorn.org/) execution
---

<br />

1. Install gunicorn: `pip install gunicorn`

2. Start the app using gunicorn binary: `gunicorn --bind 0.0.0.0:8001 run:app`

3. Go to `http://localhost:8001` in browser.

<br />

## Other Tools


### [Mapshaper](https://github.com/mbloch/mapshaper) Polygon Simplification Tool
---


1. Install mapshaper: `npm install -g mapshaper`
2. Simplification Tool: `mapshaper-xl <infile>.shp simplify <x>% -o <outfile>.shp`
   * note: this will take a while

<br />



## Change Log

<br />

## Credits & Links
### [Flask Framework](https://www.palletsprojects.com/p/flask/)

[Flask](/what-is/flask) is the python web framework that the application is built upon.

<br />

### Python Libraries
* [folium](https://python-visualization.github.io/folium/)
* [numpy](https://docs.scipy.org/doc/numpy/reference/)
* [pandas](https://pandas.pydata.org/pandas-docs/stable/)
* [geopandas](http://geopandas.org/)