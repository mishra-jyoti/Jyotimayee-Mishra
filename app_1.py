from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/api/sensors')
def get_sensor_data():
    data = {
        "soil_moisture": random.randint(30, 70),
        "temperature": random.uniform(25.0, 35.0),
        "humidity": random.randint(50, 90),
        "rain_detected": random.choice([True, False]),
        "irrigation_on": random.choice([True, False])
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)