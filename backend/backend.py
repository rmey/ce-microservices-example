from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# List of messages of the day
messages = [
    "Keep pushing forward!",
    "Believe in yourself!",
    "Strive for greatness!",
    "Embrace the journey!",
    "Today is a new opportunity!"
]

@app.route('/api/time', methods=['GET'])
def get_current_time_and_message():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message_of_the_day = random.choice(messages)
    return jsonify({
        'current_time': current_time,
        'message_of_the_day': message_of_the_day
    })

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    