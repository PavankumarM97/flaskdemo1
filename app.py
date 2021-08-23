from main import app,api,Student
from main import db
from main.resource import Alldata
db.create_all()
api.add_resource(Student, "/flaskdemo/<int:flaskdemo_id>")
api.add_resource(Alldata, "/alldata")
if __name__ == "__main__":
    app.run(debug=True)