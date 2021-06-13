'''
This program creates a FLASK API that stores a list of contacts. The program is able to add
and get data from the API using the POST and GET mehods respectively.
'''
#importing the required modules
from flask import Flask,jsonify,request

#creating a flask object
app = Flask(__name__)


#creating a contacts list
contacts_list = [
    {"Contact":"9987644456",
     "Name" : "Raju" ,
     "id" : 1
    },
{"Contact":"9927614486",
     "Name" : "Raju" ,
     "id" : 2
    }
]
#creating a route and a function add data using the POST method
@app.route("/add-data",methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide data! :("
        },400)
    t = {
        'id' : contacts_list[-1]['id']+1,
        'Name'   : request.json['Name'],
        "Contact" : request.json['Contact']
    }    
    contacts_list.append(t)
    return jsonify({
        "status" : "data successfully added",
        "message" : "Contact Successfully Added :)"
    })


#creating a route and function to get data using the GET method
@app.route('/get-data')

def get_task():
    return jsonify({
        'data' : contacts_list
    }) 

#enabling the debugging of the code
if __name__ == '__main__' :
    app.run(debug=True)
