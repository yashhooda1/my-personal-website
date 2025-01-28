# app.py

from flask import Flask, render_template, request, jsonify
from calculator import calculate_pace, calculate_distance, calculate_time, predict_race_time

app = Flask(__name__)

# Serve the main HTML file
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint for the Running Conversion Calculator
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        goal = request.form['goal']

        # Perform calculations based on the selected goal
        if goal == 'pace':
            time = float(request.form['time'])
            distance = float(request.form['distance'])
            result = calculate_pace(time, distance)

        elif goal == 'distance':
            pace = float(request.form['pace'])
            time = float(request.form['time'])
            result = calculate_distance(pace, time)

        elif goal == 'time':
            pace = float(request.form['pace'])
            distance = float(request.form['distance'])
            result = calculate_time(pace, distance)

        elif goal == 'predict_race_time':
            running_time = float(request.form['running_time'])
            running_distance = float(request.form['running_distance'])
            predicted_distance = float(request.form['predicted_distance'])
            result = predict_race_time(running_time, running_distance, predicted_distance)

        else:
            return jsonify({"error": "Invalid calculation type selected."}), 400

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
