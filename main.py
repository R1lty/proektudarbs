
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


import time
#import pandas
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
driver = webdriver.Chrome()
url = "https://www.ss.lv/lv/transport/cars/"
driver.get(url)
time.sleep(2)

#YEAR
find = driver.find_element(By.ID, "f_o_18_min")
find.send_keys(car.yearOfCar)
time.sleep(0.5)

find = driver.find_element(By.ID, "f_o_18_max")
find.send_keys(car.yearOfCar)
time.sleep(0.5)

#ENGINE
find = driver.find_element(By.ID, "f_o_15_min")
find.send_keys(car.carEngine)
time.sleep(0.5)
find = driver.find_element(By.ID, "f_o_15_max")
find.send_keys(car.carEngine)
time.sleep(0.5)
#TRANSMISSION
find = driver.find_element(By.ID, "f_o_35")
find.send_keys(car.carTransmission)
time.sleep(0.5)




#------------------------------------ READING -------------------------------------------------------------------------

car_model_elements = driver.find_elements(By.XPATH, '//tr[starts-with(@id, "tr_5")]')

if not car_model_elements:
    print("Nav mašinas")
else:
    with open('carlist.txt', 'w', encoding='utf-8'):
        pass

    
    with open('carlist.txt', 'a', encoding='utf-8') as file:
        for car_model_element in car_model_elements:
            try:
                nested_elements = car_model_element.find_elements(By.CLASS_NAME, "amopt")
                car_model_text = " ".join([nested_element.text.replace('\n', ' ') for nested_element in nested_elements])
                car_model_text = car_model_text.replace('€ maniņai', '\n')
                file.write(car_model_text + '\n')
            
                
            except Exception as e:
                print(f"Error: {e}")
                
   
        print("Visi dati ir nolasiti")
   
        

    driver.quit()