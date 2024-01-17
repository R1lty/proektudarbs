<h1>Documentation for the Car Finder Application</h1>

<br>
<h5>Autors</h5>
<h6>Aleksandrs Kuņicins 231RDB271</h6>
<h6>Mihails Koržeņevskis 231RDB232</h6>
<br>

<h3>Introduction<h3>
<h4>
The Car Finder Application is designed to help users find a suitable car based on specified criteria. It utilizes web scraping to gather information about available cars from a popular car listing website in Latvia ("https://www.ss.lv/lv/transport/cars/"). The application supports various commands for sorting and filtering the car data, providing users with flexibility in finding the desired car.
</h4>
<br>
<h3>Libraries</h3>
<h4>
openpyxl
selenium
os
time
pandas
tabulate
</h4>

<br>
<h3>Usage</h3>
<h4>The program starts by displaying a welcome message and then prompts the user to input the desired year, engine size, and transmission type for the car. It validates the input data using the check_yearOfCar, check_engine, and check_transmission methods.</h4>
<br>
<h3>Web Scraping and Excel File Creation</h3>
<h4>The application uses web scraping to gather car data from the specified website based on the user's input criteria. The obtained data is then written to an Excel file ("carlist.xlsx").</h4>
<br>
<h3>User Commands</h3>
<h4>The user is presented with a set of commands to interact with the application. The available commands include:

minpr: Displays the cheapest cars from the Excel list.
maxpr: Displays the most expensive cars from the Excel list.
lowmil: Displays cars with the lowest mileage.
maxmil: Displays cars with the highest mileage.
findmark: Allows the user to find cars by a specific brand or keyword.
help: Displays the list of commands.
exit: Stops the program.</h4>
<br>

<h3>Additional Notes</h3>
<h4>The Excel file from the previous run is removed at the beginning of the program to avoid data duplication.
The program uses the Selenium web driver for web scraping and openpyxl for Excel file manipulation.
The application provides feedback messages and handles unknown commands gracefully.</h4>
