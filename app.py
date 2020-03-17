from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/input', methods=["POST"])
def input():
    payload = request.get_json(force=True)
    x = payload['x']
    y = payload['y']
    if x < 0 or x > ROOM_SIZE_X or y < 0 or y > ROOM_SIZE_Y :
        answer = 'out'
    else :
        answer = 'in'
    resp = {'status': answer, 'x': x, 'y': x}
    return jsonify(resp)
    
if __name__ == '__main__':
    app.run(debug=True, port=8000)