from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/request-deletion', methods=['POST'])
def request_deletion():
    data = request.get_json(force=True)
    # In a real implementation you would verify the request
    # and remove the associated data from your systems.
    print('Received deletion request:', data)
    return jsonify({'status': 'received'})

if __name__ == '__main__':
    app.run(port=5000)
