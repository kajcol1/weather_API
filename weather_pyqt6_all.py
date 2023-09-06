import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QMessageBox

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 400, 300)  # Increased the window height for additional weather data

        self.api_key = '30d4741c779ba94c470ca1f63045390a'

        self.city_label = QLabel("Put a city name or select from the list:")
        self.city_combo = QComboBox()
        self.city_combo.setEditable(True)
        self.city_combo.setCompleter(None)  # Disable autocompletion
        self.city_combo.currentIndexChanged.connect(self.get_weather)

        # Labels for weather information
        self.weather_label = QLabel("")
        self.temperature_label = QLabel("")
        self.humidity_label = QLabel("")
        self.pressure_label = QLabel("")
        self.wind_label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_combo)
        layout.addWidget(self.weather_label)
        layout.addWidget(self.temperature_label)
        layout.addWidget(self.humidity_label)
        layout.addWidget(self.pressure_label)
        layout.addWidget(self.wind_label)

        self.setLayout(layout)

    def get_weather(self):
        city = self.city_combo.currentText()
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&exclude=hourly,daily&APPID={self.api_key}")

        if weather_data.json()['cod'] == 404:
            # Display an error message
            error_message = f"There is no city like {city}"
            QMessageBox.critical(self, "City Not Found", error_message, QMessageBox.StandardButton.Ok)
            self.clear_weather_labels()
        else:
            data = weather_data.json()
            weather = data['weather'][0]['main']
            temp = round(data['main']['temp'])
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind_speed = data['wind']['speed']
            weather_description = data['weather'][0]['description']

            self.weather_label.setText(f"The weather in {city} is: {weather_description}")
            self.temperature_label.setText(f"Temperature: {temp}ºC")
            self.humidity_label.setText(f"Humidity: {humidity}%")
            self.pressure_label.setText(f"Pressure: {pressure} hPa")
            self.wind_label.setText(f"Wind Speed: {wind_speed} m/s")

    def clear_weather_labels(self):
        # Clear all weather labels
        self.weather_label.clear()
        self.temperature_label.clear()
        self.humidity_label.clear()
        self.pressure_label.clear()
        self.wind_label.clear()

def main():
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
