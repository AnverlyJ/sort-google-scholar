#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
This code creates a database with a list of publications data from Google 
Scholar.
The data acquired from GS is Title, Citations, Links and Rank.
It is useful for finding relevant papers by sorting by the number of citations
This example will look for the top 100 papers related to the keyword, 
so that you can rank them by the number of citations

As output this program will plot the number of citations in the Y axis and the 
rank of the result in the X axis. It also, optionally, export the database to
a .csv file.


"""

import requests, os, datetime, argparse
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
from time import sleep
import warnings
import random
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
