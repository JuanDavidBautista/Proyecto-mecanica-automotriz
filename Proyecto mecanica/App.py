from flask import Flask 
from flask_sqlalchemy import SQLAlchemy


# crear el objeto de aplicación
app = Flask(__name__)
#configurar app para conectarse a bd
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask-shopy-2687350'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# crear el objeto sqlalchemy
db = SQLAlchemy(app)