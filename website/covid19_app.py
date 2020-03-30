from flask import Flask, request, session, redirect, url_for, render_template, flash
import csv

from datetime import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.WARN)

app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)  # load config from this file , flaskr.py


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

# Retieve data from 'static' directory. Used most typically for rendering images.
@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)


@app.route('/')
@app.route('/index')
def index():
    ui_data = {"slide2":slide2_data(),
               "slide3":slide3_data()
               }
    return render_template('index.html', ui_data=ui_data)

def slide2_data():
    dir_path = "./static/data/covid_19_cases_by_state.csv"
    state_data = csv.DictReader(open(dir_path),delimiter=',')
    state_data = list(state_data)
    for item in state_data:
        item['deaths']= "{:,}".format(int(item['deaths']))
        item['cases'] = "{:,}".format(int(item['cases']))

    return state_data

def slide3_data():
    # Build up data required to render slide two and return it in the form of a dictionary
    dir_path = "./static/data/covid_19_cases_by_county.csv"
    county_data = csv.DictReader(open(dir_path),delimiter=',')
    county_data_list = list(county_data)
    for item in county_data_list:
        item['state_county'] = item['state']+", "+item['county']
        item['deaths']= "{:,}".format(int(item['deaths']))
        item['cases'] = "{:,}".format(int(item['cases']))
    
    return county_data_list


# Load default config and override config from an environment variable
app.debug = False
app.config.update(dict(
    SECRET_KEY='development key',
    WTF_CSRF_ENABLED=True,
))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)
    # app.run(host='0.0.0.0')
