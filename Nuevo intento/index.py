from app import app
from utils.db import db
import config

with app.app_context():
    try:
        db.create_all()
    except Exception as exception:
        print("Error db.create_all() : " + str(exception))

if __name__ == "__main__":
    app.run(debug=True)
