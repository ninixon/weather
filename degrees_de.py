from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',de&appid=8e457b829930ac77ad2bc76dac41ddb5')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_f = (temp_k - 273.15) * 1.8 + 32
    temp_c = (temp_f - 32) / 1.8
    return render_template('temperature.html', temp1=temp_f, temp2=temp_c)

@app.route('/')
def index():
    return render_template('index.html')

# if __name__ == '__main__':
app.run(debug=True)