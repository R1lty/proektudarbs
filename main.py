import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas

from classes import *

car = Car()


#------------------------------------ WELCOME MESSAGE -------------------------------------------------------------------------

car.write_welcome_message()

#------------------------------------ DATA CHEACKING -------------------------------------------------------------------------


while (True):
    yearOfCar = int(input("Please write what year of car you want to purchase 'e.g 2018' (Year): "))
    if car.check_yearOfCar(yearOfCar):
        car.yearOfCar = yearOfCar 
        break
    else:
        print("We cannot find a car of this year, please enter another year")


while (True):
    carEngine = float(input("Now write what engine size you want 'e.g 1.6' (Engine): "))
    if car.check_engine(carEngine):
        car.carEngine = carEngine
        break
    else:
        print("We can't find a car with this engine size, please enter another engine")


while (True):
    carTransmission = input("What kind of transmission do you want in your car 'manual/automatic ' (Transmission): ").lower()
    if car.check_transmission(carTransmission):
        if carTransmission == "manual":
            car.carTransmission = "Manuāla"
        elif carTransmission == "automatic":
            car.carTransmission = "Automāts"
        break
    else:
        print("We can't find a transmission of this type, either manual or automatic")


#------------------------------------ SEARCHING -------------------------------------------------------------------------

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.ss.lv/lv/transport/cars/"
driver.get(url)
time.sleep(2)

#YEAR
find = driver.find_element(By.ID, "f_o_18_min")
find.send_keys(car.yearOfCar)

find = driver.find_element(By.ID, "f_o_18_max")
find.send_keys(car.yearOfCar)

#ENGINE
find = driver.find_element(By.ID, "f_o_15_min")
find.send_keys(car.carEngine)

find = driver.find_element(By.ID, "f_o_15_max")
find.send_keys(car.carEngine)

#TRANSMISSION
find = driver.find_element(By.ID, "f_o_35")
find.send_keys(car.carTransmission)
