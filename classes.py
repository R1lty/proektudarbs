
class Car:
    
    
    def write_welcome_message(self):
        print("""
            Welcome to the application for finding a suitable car. 
            We will help you find a car according to your criteria
            """)
        
    def check_yearOfCar(self,yearOfCar):
        return  True if 1923 < yearOfCar<=2024 else False
    
    def check_engine(self,engineOfCar):
        return True if 0.6 <= engineOfCar <= 7.3 else False
    
    def check_transmission(self,carTransmission):
        return True if carTransmission==("manual" or "automatic") else False