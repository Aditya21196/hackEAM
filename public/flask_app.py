"""
request url example - https://localhost:8000/api/name="test"&id=2
above get request prints data as dict {"name": "manan", "id": 2}
"""
from flask import Flask
from flask_restful import Resource, Api, reqparse


def parse_payload(string):
	query = {}
	for s in string.split("&"):
		s = s.split("=")
		query.update({s[0].strip(): s[1].strip()})
	return query


app = Flask(__name__)
api = Api(app)


class ApiTest(Resource):
	def get(self, query):
		data = parse_payload(query)
		print(data)
		# do processing on data
		return {"message": "data received."}


api.add_resource(ApiTest, "/api/<string:query>")
if __name__ == '__main__':
	parser = reqparse.RequestParser()
	app.run(debug=True, host="0.0.0.0", port=80)
