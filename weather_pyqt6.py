import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QMessageBox

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 400, 200)

        self.api_key = '30d4741c779ba94c470ca1f63045390a'

        self.city_label = QLabel("Select a city:")
        self.city_combo = QComboBox()
        self.city_combo.setEditable(True)
        self.city_combo.setCompleter(None)  # Disable autocompletion
        self.city_combo.currentIndexChanged.connect(self.get_weather)

        self.weather_label = QLabel("")
        self.temperature_label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_combo)
        layout.addWidget(self.weather_label)
        layout.addWidget(self.temperature_label)

        self.setLayout(layout)

    def get_weather(self):
        city = self.city_combo.currentText()
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&exclude=hourly,daily&APPID={self.api_key}")

        data = weather_data.json()

        if 'weather' in data:
            weather = data['weather'][0]['main']
            temp = round(data['main']['temp'])
            self.weather_label.setText(f"The weather in {city} is: {weather}")
            self.temperature_label.setText(f"The temperature in {city} is: {temp}ºC")
        else:
            # Display an error message
            error_message = f"There is no city like {city}"
            QMessageBox.critical(self, "City Not Found", error_message, QMessageBox.StandardButton.Ok)
            self.weather_label.clear()
            self.temperature_label.clear()

def main():
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
