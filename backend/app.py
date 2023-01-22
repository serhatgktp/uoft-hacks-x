from flask import Flask, request, make_response, jsonify
from flask_cors import CORS, cross_origin   # For handling cross-origin requests
import event_bus

# Initialize Flask App
app = Flask(__name__)
CORS(app, support_credentials=True)

# Get GPT Conversation (3 opinions)
#########
@app.route('/get-gpt-conversation', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_convo():

    content_type = request.headers.get('Content-Type')
    r = request 
    if (content_type == 'application/json'):
        json = r.json
        topic = json['topic']
    else:
        topic = r.form['topic']

    rw_resp, lw_resp, neutral_resp = event_bus.get_conversation(topic)
    resp = make_response(jsonify( {
        'message': 'Success',
        'rw_opinion':rw_resp,
        'lw_opinion':lw_resp,
        'neutral_opinion':neutral_resp
        } ), 200,)
    resp.headers["Content-Type"] = "application/json"
    return resp
#########