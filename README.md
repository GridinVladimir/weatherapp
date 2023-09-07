The Weather Forecast App is a simple web application that allows users to obtain a 3-day weather forecast for any city. The app is built using Python Flask for the backend, and HTML, CSS, and a bit of JavaScript for the frontend. The weather data is retrieved from the WeatherAPI (api.weatherapi.com).
Installation

To set up and run the project locally, follow the steps below:
Clone the repository or download the project files.
Install the required Python package:

    pip install flask

Set up the API key:
Sign up for an API key from WeatherAPI.
Create a config.py file in the project directory.
In the config.py file, add the following line (replace YOUR_API_KEY with your actual API key):

    API_KEY = "YOUR_API_KEY"

Run the Flask application:

    python app.py

Open a web browser and go to http://127.0.0.1:5000/.
Enter the name of a city in the input field and click the search button (or press Enter) to get the 3-day weather forecast.
The weather forecast will be displayed below the search bar, including details such as temperature, weather conditions, and wind speed.
