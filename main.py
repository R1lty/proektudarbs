import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time
import pandas 
from tabulate import tabulate

# import pandas
from classes import *

car = Car()
# ------------------------------------ REMOVING EXCEL FROM PREVIOUS USING -------------------------------------------------------------------------


if os.path.exists("carlist.xlsx"):
    os.remove("carlist.xlsx")


# ------------------------------------ WELCOME MESSAGE -------------------------------------------------------------------------

car.write_welcome_message()

# ------------------------------------ DATA CHEACKING -------------------------------------------------------------------------


while True:
    yearOfCar = int(
        input("Please write what year of car you want to purchase 'e.g 2018' (Year): ")
    )
    if car.check_yearOfCar(yearOfCar):
        car.yearOfCar = yearOfCar
        break
    else:
        print("We cannot find a car of this year, please enter another year")


while True:
    carEngine = float(input("Now write what engine size you want 'e.g 1.6' (Engine): "))
    if car.check_engine(carEngine):
        car.carEngine = carEngine
        break
    else:
        print("We can't find a car with this engine size, please enter another engine")


while True:
    carTransmission = input(
        "What kind of transmission do you want in your car 'manual/automatic ' (Transmission): "
    ).lower()
    if car.check_transmission(carTransmission):
        if carTransmission == "manual":
            car.carTransmission = "Manuāla"
        elif carTransmission == "automatic":
            car.carTransmission = "Automāts"
        break
    else:
        print("We can't find a transmission of this type, either manual or automatic")


# ------------------------------------ SEARCHING -------------------------------------------------------------------------

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome()
url = "https://www.ss.lv/lv/transport/cars/"
driver.get(url)
time.sleep(2)

# YEAR
find = driver.find_element(By.ID, "f_o_18_min")
find.send_keys(car.yearOfCar)
time.sleep(0.5)

find = driver.find_element(By.ID, "f_o_18_max")
find.send_keys(car.yearOfCar)
time.sleep(0.5)

# ENGINE
find = driver.find_element(By.ID, "f_o_15_min")
find.send_keys(car.carEngine)
time.sleep(0.5)
find = driver.find_element(By.ID, "f_o_15_max")
find.send_keys(car.carEngine)
time.sleep(0.5)
# TRANSMISSION
find = driver.find_element(By.ID, "f_o_35")
find.send_keys(car.carTransmission)
time.sleep(0.5)


# ------------------------------------ READING AND COMPLETING AN EXCEL FILE-------------------------------------------------------------------------

file_name = "carlist.xlsx"
first_row_values = ["Marka", "Gads", "Tilpums", "Nobraukums", "Cena"]


car_model_elements = driver.find_elements(By.XPATH, '//tr[starts-with(@id, "tr_5")]')


if not car_model_elements:
    print("Nav mašinas")
else:
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    sheet.append(first_row_values)

    columns_data = []

    for car_model_element in car_model_elements:
        try:
            nested_elements = car_model_element.find_elements(By.CLASS_NAME, "amopt")
            car_model_text = "?".join(
                [
                    nested_element.text.replace("\n", " ")
                    for nested_element in nested_elements
                ]
            )

            lines = car_model_text.split("?")

            for i, line in enumerate(lines):
                if len(columns_data) <= i:
                    columns_data.append([])
                columns_data[i].append(line)

        except Exception as e:
            print(f"Error: {e}")

    for i, column_data in enumerate(columns_data):
        for j, value in enumerate(column_data):
            sheet.cell(row=j + 2, column=i + 1, value=value)

    workbook.save(file_name)

    driver.quit()
# ------------------------------------ PRINTING THE RESULT-------------------------------------------------------------------------


    print("Visi dati ir nolasiti")
    print("Jūsu dati atrodas failā carlist.xlxs")


# ------------------------------------ USER PROMTS-------------------------------------------------------------------------
    
    
    car.command_instruction()
    

    while True: 
        user_prompt = input("Select a command : ")

        if user_prompt == "minpr":

            sorted_car_list = sorted(car.read_excel(), key=lambda x: float(x[4].replace(' €', '').replace(',', '').replace('-', '0').replace('maiņai','')))

            headers = ["Model", "Year", "Capacity", "Mileage", "Price"]
            table_data = list(zip(headers, sorted_car_list[0]))
            table = tabulate(table_data, headers="firstrow", tablefmt="grid")

            print(table)
        
        elif user_prompt == "maxpr":
            
            sorted_car_list= sorted(car.read_excel(), key=lambda x: float(x[4].replace(' €', '').replace(',', '').replace('-', '0').replace('maiņai','')), reverse=True)

            headers = ["Model", "Year", "Capacity", "Mileage", "Price"]
            table_data = list(zip(headers, sorted_car_list[0]))
            table = tabulate(table_data, headers="firstrow", tablefmt="grid")

            print(table)

        elif user_prompt == "lowmil":
            
            sorted_car_list = sorted(car.read_excel(), key=lambda x: float(x[3].replace(' tūkst.', '').replace('-', "500000")))

            headers = ["Model", "Year", "Capacity", "Mileage", "Price"]
            table_data = list(zip(headers, sorted_car_list[0]))
            table = tabulate(table_data, headers="firstrow", tablefmt="grid")

            print(table)

        elif user_prompt == "maxmil":

            sorted_car_list = sorted(car.read_excel(), key=lambda x: float(x[3].replace(' tūkst.', '').replace('-', "0")),reverse=True)

            headers = ["Model", "Year", "Capacity", "Mileage", "Price"]
            table_data = list(zip(headers, sorted_car_list[0]))
            table = tabulate(table_data, headers="firstrow", tablefmt="grid")

            print(table)

        elif user_prompt == "exit":
            break
        
        elif user_prompt == "findmark":
            user_prompt = input("Write the mark you want to find : ").capitalize()
            check = False
            car_info_list = car.read_excel()
            print("")
            for car_info in car_info_list:
                # if user_prompt in car_info[0]:
                #     check = True
                #     print(f"{car_info[0]} {car_info[1]} {car_info[2]} {car_info[3]} {car_info[4]}")

                if all(word in car_info[0].split() for word in user_prompt.split()):
                    print(f"{car_info[0]} {car_info[1]} {car_info[2]} {car_info[3]} {car_info[4]}")

            if check == False:

                print("There are no such mark")    
                

        else: 
            print("Unknown command")