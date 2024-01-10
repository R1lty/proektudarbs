import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas

from classes import *

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)