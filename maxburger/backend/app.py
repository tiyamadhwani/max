from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import csv
import os
from datetime import datetime
import google.generativeai as genai

app = Flask(__name__, static_folder='../frontend/build', static_url_path='')
CORS(app)

# GOOGLE GEMINI API KEY
genai.configure(api_key="")

model = genai.GenerativeModel("gemini-2.0-flash")

CSV_FILE = 'franchise_inquiries.csv'
CSV_HEADERS = ['Name', 'Email', 'Phone', 'City', 'State', 'Investment_Budget', 'Experience', 'Message', 'Timestamp']


def ensure_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)


@app.route('/api/franchise-inquiry', methods=['POST'])
def franchise_inquiry():
    data = request.json
    ensure_csv()

    row = [
        data.get('name', ''),
        data.get('email', ''),
        data.get('phone', ''),
        data.get('city', ''),
        data.get('state', ''),
        data.get('budget', ''),
        data.get('experience', ''),
        data.get('message', ''),
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ]

    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)

    return jsonify({'success': True, 'message': 'Inquiry submitted successfully!'})


@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    history = data.get('history', [])

    system_prompt = """You are Max, the friendly franchise assistant for Max Burger & More — a fast-growing Indian burger franchise brand.

Your role is to help potential franchise partners learn about:
- Franchise investment details (investment range: ₹7-15 lakhs depending on location type)
- Setup & support: full training, kitchen setup, branding, and ongoing support provided
- Revenue potential: average outlet earns ₹2–5 lakhs/month
- Franchise models: Kiosk, Takeaway, Dine-In
- Current locations: Udaipur
- Menu highlights: Burgers, Momos , Fries , Spring rolls , Cold Coffee and many more
- Contact: email maxburgerandmore@gmail.com or fill the inquiry form on the website

Be enthusiastic, helpful, and professional. Use emojis occasionally. Keep answers concise but informative. Always encourage potential franchisees to fill out the contact form for personalized consultation. If asked about something unrelated to Max Burger franchise, politely redirect to franchise-related topics.
"""

    conversation = system_prompt + "\n\n"

    for msg in history[-10:]:
        role = msg.get("role")
        content = msg.get("content")

        if role == "user":
            conversation += f"User: {content}\n"
        else:
            conversation += f"Assistant: {content}\n"

    conversation += f"User: {user_message}\nAssistant:"

    try:
        response = model.generate_content(conversation)
        bot_reply = response.text
    except Exception as e:
        bot_reply = "Sorry, I'm having trouble responding right now. Please try again later."

    return jsonify({'response': bot_reply})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    ensure_csv()
    app.run(debug=True, port=5000)
