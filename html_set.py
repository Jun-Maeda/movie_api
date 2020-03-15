from flask import Flask, render_template, request
from movies import Popular, Detail

app = Flask(__name__)


@app.route('/')
def hello():
    title = "映画情報"
    message = "人気ランキング"
    pops = Popular()
    return render_template('index.html', title = title, message = message, pops = pops)


@app.route('/movie', methods=["GET"])
def movie():
    title = "映画詳細"
    # getで取得したIDを使用して映画情報を取得する
    id = request.args.get('id')
    movie = Detail(id)
    return render_template("shosai.html", title = title, movie = movie, method = request.method)


if __name__ == "__main__":
    app.run()
