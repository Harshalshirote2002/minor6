from flask import Flask, request, jsonify
from process2 import process_array
import numpy as np

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    # Receive the JSON payload containing the array
    data = request.get_json()

    # Extract the array from the payload
    data=np.array(data)
    sample_array = data

    # Process the array and obtain the result
    result = process_array(sample_array)

    # Return the result as a JSON response
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
