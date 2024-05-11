
from flask import Flask, request
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)
 
# Simple in-memory data storage for employees
employees_data = [
    {'id': 1, 'name': 'Abhilash Gaurav'},
    {'id': 2, 'name': 'Ramish Verma'}
]
 
# GET and POST Request 
class EmployeesResource(Resource):
    def get(self):
        """
        Get a list of all employees
        ---
        responses:
          200:
            description: A list of employees
        """
        return employees_data, 200
 
    def post(self):
        """
        Add a new employee
        ---
        parameters:
          - in: body
            name: body
            required: true
            schema:
              id: Employee
              required:
                - name
              properties:
                name:
                  type: string
                  description: The name of the employee
        responses:
          201:
            description: The added employee
          400:
            description: Bad request
        """
        # Get the last ID and increment to create a new unique ID
        new_id = employees_data[-1]['id'] + 1
        data = request.get_json()
        new_employee = {'id': new_id, 'name': data['name']}
        employees_data.append(new_employee)
        return new_employee, 201
       
 
 
api.add_resource(EmployeesResource, '/employees')
 
if __name__ == '__main__':
    app.run(debug=True)