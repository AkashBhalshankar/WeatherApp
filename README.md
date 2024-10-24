# Weather Monitoring System with Django

## Project Description
The **Weather Monitoring System** is a web application that fetches real-time weather data for Indian cities using the OpenWeatherMap API. The system calculates daily weather summaries, including average, maximum, and minimum temperatures, and allows users to set temperature-based alerts. The project uses Django for the backend and HTML/CSS for the frontend.

## Features
- Fetch real-time weather data for cities like Delhi, Mumbai, and more.
- Calculate daily summaries of temperature (average, max, min).
- Set user-defined temperature alerts.
- Built using Django, HTML, and CSS.

## Technologies Used
- Django (backend)
- HTML & CSS (frontend)
- SQLite (database)
- OpenWeatherMap API (weather data)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/AkashBhalshankar/WeatherApp
    ```

2. Navigate to the project directory:
    ```bash
    cd weather-monitoring-django
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your OpenWeatherMap API key:
    ```bash
    export WEATHER_API_KEY=your_openweathermap_api_key
    ```

5. Apply migrations:
    ```bash
    python manage.py migrate
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the application in your browser:
    ```
    http://127.0.0.1:8000/
    ```

## Usage
- **View Weather Data**: The application will automatically fetch weather data and display daily summaries (temperature, weather conditions).
- **Set Temperature Alerts**: Users can configure alerts for when the temperature exceeds a certain threshold.

## Example
- Set an alert if the temperature exceeds 35°C for two consecutive readings.

## Testing
To run tests:
```bash
python manage.py test
