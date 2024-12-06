from flask import Flask, request, jsonify, make_response
import json
app = Flask(__name__)
import uuid

student = []

# flask --app app2 run on 5000 port


# In-memory storage for API keys (replace with a database in production)
api_keys = {'rth25th345ny4ertyrtg5r6ynn46yu566','wertb45yn5ty24b5y3h5ne6u3we6u363'}

# @app.route('/generate_api_key', methods=['POST'])
# def generate_api_key():
#     api_key = str(uuid.uuid4())
#     api_keys[api_key] = True
#     return jsonify({'api_key': api_key})


@app.get("/")
def hello():
    return "Welcome to the Student API!"

@app.get("/students")
def students():
    api_key = request.headers.get('X-API-KEY') # in postman set headers key value 
    if api_key in api_keys:
        return student
    else:
        return jsonify({'error': 'Invalid API key'}), 401
    


@app.get("/student_name/<string:name>") 
def student_name(name):
    return "hello" + name + "!"




# set postman body > raw , type 'json' for post requeset

# {
#     "name":"shubhankar",
#     "country": "india",
#     "city": "kolkata",
#     "birthyear":"1997",
#     "skills": "python",
#     "bio":"xyz"
# }

@app.post("/create_students")  # set postman body > raw , type 'json'
def create_student():
    form = request.get_json()
    details = {
    'name': form['name'],
    'country': form['country'],
    'city': form['city'],
    'birthyear': form['birthyear'],
    'skills': form['skills'].split(', '),
    'bio': form['bio'],
    }
    student.append(details)
    return details


@app.get('/get_students/<int:id>')
def get_one_friend(id):
    return student[id]['name'] , 200

@app.route('/update_student/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    student[id]['name'] = data.get('name', student[id]['name'])
    student[id]['country'] = data.get('country', student[id]['country'])
    student[id]['city'] = data.get('city', student[id]['city'])
    student[id]['birthyear'] = data.get('birthyear', student[id]['birthyear'])
    student[id]['skills'] = data.get('skills', student[id]['skills'])
    student[id]['bio'] = data.get('bio', student[id]['bio'])

    return student[id], 200

@app.delete('/delete_student/<int:id>')
def delete_friend(id):
    del student[id]
    return {"success": "data successfully deleted from the server"}, 200

if __name__ == '__main__':
    app.run(debug=True,port=5000)