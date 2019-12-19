from flask import Flask, jsonify, request, abort
from MenuDAO import MenuDAO


app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello, World!"

#curl "http://127.0.0.1:5000/menu"
@app.route('/menu')
def getAll():
    #print("in getall")
    results = MenuDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/menus/2"
@app.route('/menu/<int:id>')
def findById(id):
    foundMenu = MenuDAO.findByID(id)

    return jsonify(foundMenu)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Item\":\"hello\",\"Item_ Description\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/menus
@app.route('/menus', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    menu = {
        "Item": request.json['Item'],
        "Item_ Description": request.json['Item_ Description'],
        "Price": request.json['Price'],
    }
    values =(menu['Item'],menu['Item_ Description'],menu['Price'])
    newId = MenuDAO.create(values)
    menu['id'] = newId
    return jsonify(menu)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Item\":\"hello\",\"Item_ Description\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/menus/1
@app.route('/menus/<int:id>', methods=['PUT'])
def update(id):
    foundMenu = MenuDAO.findByID(id)
    if not foundMenu:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)

    if 'Item' in reqJson:
        foundMenu['Item'] = reqJson['Item']
    if 'Item_ Description' in reqJson:
        foundMenu['Item_ Description'] = reqJson['Item_ Description']
    if 'Price' in reqJson:
        foundMenu['Price'] = reqJson['Price']
    values = (foundMenu['Item'],foundMenu['Item_ Description'],foundMenu['Price'],foundMenu['id'])
    MenuDAO.update(values)
    return jsonify(foundMenu)
        

    

@app.route('/menus/<int:id>' , methods=['DELETE'])
def delete(id):
    MenuDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)