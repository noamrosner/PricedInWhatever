from flask import Flask
from flask import send_file
from flask import Blueprint, render_template, request, flash, redirect, url_for
from stock import *
from Calender import *
from chart import *
from currency import *
from date import *
import datetime
import os
import sys
import time

import plotly.graph_objects as go

from datetime import datetime
import json
import plotly
import plotly.express as px

from flask import send_from_directory

application = Flask(__name__)
application.config['SECRET_KEY'] = 'SECRETKEY'


@application.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        stock1 = request.form.get('stock1').lower()
        stock2 = request.form.get('stock2').lower()

        if len(stock1) > 8 or len(stock2) > 8:
            print("stock length is above 8, returning to home page")
            render_template("home.html")
        if stock1 == stock2:
            print("stocks are equal, returning to home page")
            return render_template("home.html")

        print("after validation") ##########################

        if stock1 != stock2:
            filename = f'{stock1}pricedin{stock2}.xlsx' # data file
            new_filename = f'pricedinwhatever-{filename}' # final file

            date_end = get_date_from_user(datetime.today().strftime('%Y-%m-%d')) # set the end date (today)

            try:
                common_date = get_common_date(filename, stock1, stock2) # set the first common date
                print(f"first common date is {common_date}")
                print(f"end date is {date_end}")
            except Exception:
                return render_template("home.html")

            curr1 = getCurr(getSuffix(stock1)) # set currency for each stock
            curr2 = getCurr(getSuffix(stock2))

            print(f"curr1 - {curr1}, curr2 - {curr2}")
            print("after currency setup") ##########################

            """     
            date_end = format_date(date_end)
            common_date = format_date(common_date)
            """

            if curr1 != curr2: # conversion is needed
                if curr1 == "usd":
                    wanted_conversion = f"{curr2}=x" # unique usd conversion
                else:
                    wanted_conversion = f"{curr1}{curr2}=x" # normal conversion
                try:
                    getDataC(stock1, stock2, wanted_conversion, common_date, date_end) # get the data to data file
                except Exception as e:
                    print("error in getDataC")
                    print(e)

                date_end = format_date(date_end)
                common_date = format_date(common_date)

                try:
                    fixDates(new_filename, common_date, date_end) # set up the final file with the date column
                except Exception as e:
                    print("error in fixDates")
                    print(e)
                try:
                    emptyStartC(filename, new_filename, stock1, stock2, wanted_conversion)  # fill the first row
                except Exception as e:
                    print("error in emptyStartC")
                    print(e)
                try:
                    fillListC(filename, new_filename, stock1, stock2, wanted_conversion) # fill the final file with values
                except Exception as e:
                    print("error in fillListC")
                    print(e)
                try:
                    removeBlanksC(new_filename) # remove blanks - this should be removed (action is done inside fill list)
                except Exception as e:
                    print("error in removeBlanksC")
                    print(e)
                try:
                    roundUpC(new_filename)
                except Exception as e:
                    print(e)
                try:
                    calculateC(new_filename) # calculate the values in the final file to new columns
                except Exception as e:
                    print("error in calculateC")
                    print(e)
            else:
                try:
                    createTable(stock1, stock2, common_date, date_end)
                except Exception as e:
                    print(e)
                try:
                    fixDates(new_filename, common_date, date_end)
                except Exception as e:
                    print(e)
                try:
                    emptyStart(filename, new_filename, stock1, stock2)
                except Exception as e:
                    print(e)
                try:
                    fillList(filename, new_filename, stock1, stock2)
                except Exception as e:
                    print("error in fillList")
                    print(e)
                """try:
                    removeBlanks(new_filename)
                    print("error in removeBlanks")
                except Exception as e:
                    print(e)"""
                try:
                    roundUp(new_filename)
                except Exception as e:
                    print(e)
                try:
                    calculate(new_filename)
                except Exception as e:
                    print(e)

            fig = plotyChart(new_filename, stock1, stock2, curr1, curr2) # set the Plotly figure object
            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            return render_template('table.html', graphJSON=graphJSON)
    else:
        return render_template("home.html")


@application.route('/table')
def table():
    return render_template("table.html")


@application.route('/syntax')
def inputsyntax():
    return render_template("inputsyntax.html")


@application.errorhandler(404)
def notFound(e):
    return render_template("404.html"), 404


@application.errorhandler(408)
def notFound(e):
    return render_template("408.html"), 408


@application.errorhandler(405)
def notFound(e):
    return render_template("404.html"), 405


@application.errorhandler(500)
def notFound(e):
    return render_template("home.html"), 500


@application.errorhandler(502)
def notFound(e):
    return render_template("home.html"), 502

@application.errorhandler(504)
def notFound(e):
    return render_template("home.html"), 504


@application.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))  # maybe this can be deleted for aws
    os.chdir(dir_path)

    application.run(debug=True)
