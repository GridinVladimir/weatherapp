from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        api_key = '2b5dc7a1335a4efcb3b132528230607'
        city = request.form['city']
        url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=3&aqi=yes&alerts=yes&lang=ru'
        response = requests.get(url)
        data = response.json()

        if 'forecast' in data and 'forecastday' in data['forecast']:
            forecast_day = data['forecast']['forecastday']
        else:
            return render_template('index.html', weather_available=False)
        
        
        weather_data = []
        city_name = data['location']['name']
        for idx, day in enumerate(forecast_day):
            date = day['date']
            maxtemp_c = day['day']['maxtemp_c']
            maxtemp_f = day['day']['maxtemp_f']
            mintemp_c = day['day']['mintemp_c']
            mintemp_f = day['day']['mintemp_f'] 
            condition_text = day['day']['condition']['text']
            condition_icon = day['day']['condition']['icon']
            maxwind_kph = day['day']['maxwind_kph']
            avghumidity = day['day']['avghumidity']

            if idx == 0:
                date_label = "Сегодня"
            elif idx == 1:
                date_label = "Завтра"
            else:
                date_label = "Послезавтра"

            weather_data.append({
                'date': date,
                'date_label': date_label,
                'maxtemp_c': maxtemp_c,
                'maxtemp_f': maxtemp_f,
                'mintemp_c': mintemp_c,
                'mintemp_f': mintemp_f,
                'condition_text': condition_text,
                'condition_icon': condition_icon,
                'maxwind_kph': maxwind_kph,
                'avghumidity': avghumidity,
            })

        return render_template('index.html', weather_available=True, weather_data=weather_data, city_name=city_name)
    
    return render_template('index.html', weather_available=False)

if __name__ == '__name__':
    app.run(debug=True)