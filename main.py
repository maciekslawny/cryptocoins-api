from coinsapi import *
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = "hello"



coins_data = create_coin('all')


@app.route("/")
def main():
    return render_template("index.html", coins_data = coins_data)



@app.route("/<coin>")
def coin_page(coin):
    coin_info = create_coin(coin)
    return render_template("coinpage.html", coin_info = coin_info)


if __name__ == "__main__":
    app.run(debug=True)
