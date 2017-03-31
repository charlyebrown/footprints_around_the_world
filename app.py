from flask import Flask, render_template
import os
from models import db


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/maps')
def maps():
	return render_template('maps.html')

if __name__ == '__main__':
    app.run()