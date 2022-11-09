
import datetime
import openpyxl

import yfinance as yf
import pandas as pd
import time
from Calender import *
from date import *
import os

from stock import *
from chart import *
from currency import *

def getDateFromUser(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    return date.strftime("%d/%m/%Y")

