**Script Overview:**

This Python script is a simple weather information retrieval tool using the OpenWeatherMap API. It prompts the user to input the name of a city, queries the API for weather data about that city, and then displays the current weather condition and temperature in Celsius.

**Key Components:**

1. **API Key:** The script starts by defining an API key. This key is required to authenticate and access the OpenWeatherMap API.

2. **User Input:** The script prompts the user to enter the name of a city for which they want to retrieve weather information. The input is stored in the `user_input` variable.

3. **API Request:** It constructs a URL for the OpenWeatherMap API by using the provided API key, the user's city input, and specifying units in Celsius (`units=metric`) and excluding hourly and daily forecasts (`exclude=hourly,daily`). Then, it sends a GET request to the API using the `requests.get()` method.

4. **API Response Handling:** The script checks the response status code (`cod`) from the API. If it's '404', it means the city was not found, and the script displays an error message. Otherwise, it extracts weather and temperature data from the API response.

5. **Display Weather Information:** Finally, the script prints the current weather condition (e.g., "Clouds," "Rain") and the temperature in Celsius for the specified city. However, there are two variables used in the `print` statements, `hourly` and `daily`, which are not defined anywhere in the script. These should be replaced with `weather` and `temp`, respectively, to correctly display the data.

