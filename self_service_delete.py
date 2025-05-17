import os
import json
import uuid
import smtplib
from datetime import datetime
from flask import Flask, request, jsonify

DATA_FILE = 'data_store.json'
LOG_FILE = 'data_processing.log'

ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT', '0'))
SMTP_USERNAME = os.getenv('SMTP_USERNAME')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')

app = Flask(__name__)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"users": []}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def log_event(action, email):
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_FILE, 'a') as f:
        f.write(f"{timestamp} - {action} - {email}\n")

def send_admin_email(subject, body):
    if not all([ADMIN_EMAIL, SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD]):
        return
    msg = f"Subject: {subject}\nFrom: {SMTP_USERNAME}\nTo: {ADMIN_EMAIL}\n\n{body}"
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, ADMIN_EMAIL, msg)
    except Exception:
        pass

@app.route('/register', methods=['POST'])
def register():
    data = load_data()
    user = {
        "id": str(uuid.uuid4()),
        "name": request.form.get('name'),
        "email": request.form.get('email'),
        "images": request.form.getlist('images'),
        "created_at": datetime.utcnow().isoformat(),
        "deleted": False
    }
    data["users"].append(user)
    save_data(data)
    log_event('REGISTER', user['email'])
    send_admin_email('New Registration', f"User {user['email']} registered.")
    return jsonify({"status": "ok", "id": user['id']})

@app.route('/delete', methods=['POST'])
def delete_user():
    email = request.form.get('email')
    data = load_data()
    for user in data['users']:
        if user['email'] == email and not user['deleted']:
            user['deleted'] = True
            save_data(data)
            log_event('DELETE', email)
            send_admin_email('Deletion Request', f"Delete user data for {email}.")
            return jsonify({"status": "deleted"})
    return jsonify({"status": "not_found"}), 404

@app.route('/users', methods=['GET'])
def list_users():
    data = load_data()
    return jsonify(data['users'])

if __name__ == '__main__':
    app.run(debug=True)

