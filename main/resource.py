from flask_restful import Resource,abort,reqparse,marshal_with,fields
from main.model import StudentModel
from main import db

task_args=reqparse.RequestParser()
task_args.add_argument("name",type=str,help="task is required",required=True)
task_args.add_argument("collage",type=str,help="task is required",required=True)

flaskdemo_resource_field={
    "id":fields.Integer,
    "name": fields.String,
    "collage": fields.String
}


class Student(Resource):
    @marshal_with(flaskdemo_resource_field)
    def get(self, flaskdemo_id):
        flaskdemo=StudentModel.query.filter_by(id=flaskdemo_id).first()
        if flaskdemo:
            return flaskdemo
        else:
            abort (404,message="tool not found")

    @marshal_with(flaskdemo_resource_field)
    def post(self,flaskdemo_id):
        args=task_args.parse_args()
        flaskdemo = StudentModel.query.filter_by(id=flaskdemo_id).first()
        if flaskdemo:
            abort(409,message="it is already there in table")
        flaskdemo=StudentModel(id=flaskdemo_id,name=args["name"],collage=args["collage"])
        db.session.add(flaskdemo)
        db.session.commit()
        return flaskdemo

    @marshal_with(flaskdemo_resource_field)
    def put(self,flaskdemo_id):
        args = task_args.parse_args()
        flaskdemo = StudentModel.query.filter_by(id=flaskdemo_id).first()
        if flaskdemo:
            flaskdemo.name= args["name"]
            flaskdemo.collage=args["collage"]
            db.session.add(flaskdemo)
            db.session.commit()
            return flaskdemo
        else:
            abort(404, message="Not available")

    @marshal_with(flaskdemo_resource_field)
    def delete(self, flaskdemo_id):
        flaskdemo = StudentModel.query.filter_by(id=flaskdemo_id).first()
        if flaskdemo:
            db.session.delete(flaskdemo)
            db.session.commit()
            return flaskdemo
        else:
            abort(404, message="Not available")

class Alldata(Resource):
    @marshal_with(flaskdemo_resource_field)
    def get(self):
        alldata=StudentModel.query.all()
        return alldata



