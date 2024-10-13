from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Thingspeak API settings
CHANNEL_ID = "2683427"  # Replace with your Thingspeak Channel ID
API_KEY = "W5481K3NJWUEBJC32"  # Replace with your Thingspeak Write API Key
BASE_URL = f"https://api.thingspeak.com/update?api_key={API_KEY}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_thingspeak', methods=['POST'])
def update_thingspeak():
    try:
        # Get the data from the request
        data = request.get_json()
        full_name = data['name']
        email = data['email']
        persons = data['persons']
        booking_date = data['date']
        message = data['message']

        # Create the data dictionary to send to Thingspeak
        params = {
            "field1": full_name,
            "field2": email,
            "field3": persons,
            "field4": booking_date,
            "field5": message
        }

        # Send data to Thingspeak channel
        response = requests.get(BASE_URL, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            return jsonify({'status': 'success', 'message': 'Data uploaded successfully!'}), 200
        else:
            return jsonify({'status': 'error', 'message': 'Failed to upload data to Thingspeak'}), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)