
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

@app.route('/update-location', methods=['POST'])
def update_location():
    try:
        data = request.get_json()
        print("Received location data:", data)
        return jsonify({"message": "Location received successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
