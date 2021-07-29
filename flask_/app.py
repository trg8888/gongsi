from flask import Flask,render_template
from flask_bootstrap import Bootstrap

def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  return app

app = create_app()

@app.route('/')
def index():
  return render_template('1.html')