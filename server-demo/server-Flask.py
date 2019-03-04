from flask import Flask, jsonify, render_template, request, make_response, redirect
import gameSession, dbconn
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Page not found'}), 404)


@app.route('/players', methods=['GET'])
def onlineUsers():
    showList = json.dumps(session.show_all_players(), ensure_ascii=False)
    return showList


@app.route('/server/join/<string:username>', methods=['GET', 'POST'])
def joinSession(username):
    session.add_player(username)
    flow = {"username": username}
    op_db.insert_data('players', flow)
    return redirect('/players')


@app.route('/server/leave/<string:username>', methods=['GET', 'POST'])
def leaveSession(username):
    session.remove_player(username)
    flow = {"username": username}
    op_db.delete_data('players', flow)
    return redirect('/players')


if __name__ == '__main__':
    session = gameSession.session()
    op_db = dbconn.mongo()
    app.run()
