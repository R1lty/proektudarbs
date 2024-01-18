class Car:
    def write_welcome_message(self):
        print(
            """
            Welcome to the application for finding a suitable car. 
            We will help you find a car according to your criteria
            """
        )

    def check_yearOfCar(self, yearOfCar):
        return True if 1923 < yearOfCar <= 2024 else False

    def check_engine(self, engineOfCar):
        return True if 0.6 <= engineOfCar <= 7.3 else False

    def check_transmission(self, carTransmission):
        return (
            True
            if carTransmission == "manual" or carTransmission == "automatic"
            else False
        )

    def command_instruction(self):
        import time

        print("\n\tSelect a command to search for a suitable car")

        time.sleep(2)

        print(
            """
          minpr - the cheapest car from the excel list
          maxpr - most expensive car from the excel list
          lowmil - car with the lowest mileage
          maxmil - car with the highest mileage
          findmark -  all cars this brand from the excel will be displayed in the console
          help - will display all comands
          exit - command that stops the program 
          """
        )

    def read_excel(self):
        import pandas

        excel_file_data = pandas.read_excel("carlist.xlsx")
        excel_info_list = excel_file_data.values.tolist()

        return excel_info_list
