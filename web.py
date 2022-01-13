from flask import Flask, send_from_directory
from main import render_board, fen_to_str, create_bg

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET'


@app.route('/fen/<fen1>/<fen2>/<fen3>/<fen4>/<fen5>/<fen6>/<fen7>/<fen8>/<flipped>')
def send_fen(fen1, fen2, fen3, fen4, fen5, fen6, fen7, fen8, flipped):
    if flipped != '0' and flipped != '1':
        return ('INVALID FEN - PLEASE ADD 0 or 1 (flipped or no)')
    fen = fen1 + '/' + fen2 + '/' + fen3 + '/' + fen4 + '/' + fen5 + '/' + fen6 + '/' + fen7 + '/' + fen8
    try:
        return send_from_directory('fens', fen1 + '-' + fen2 + '-' + fen3 + '-' + fen4 + '-' + fen5 + '-' + fen6 + '-' + fen7 + '-' + fen8 + '-' + flipped + '.png')
    except:
        try:
            render_board(fen_to_str(fen), create_bg(), True if flipped == '1' else False).save('fens' + '/' + fen1 + '-' + fen2 + '-' + fen3 + '-' + fen4 + '-' + fen5 + '-' + fen6 + '-' + fen7 + '-' + fen8 + '-' + flipped + '.png')
        except:
            return ('INVALID FEN')
        return send_from_directory('fens', fen1 + '-' + fen2 + '-' + fen3 + '-' + fen4 + '-' + fen5 + '-' + fen6 + '-' + fen7 + '-' + fen8 + '-' + flipped + '.png')

if __name__ == '__main__':
    app.run(host='0.0.0.0')