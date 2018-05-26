from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
  return "It works Hurray!!!!"

@app.route("/order-animation")
def order_animation():
  return render_template(
    "order.html",
    invitation="Welcome at ani creatior"
  )


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)
