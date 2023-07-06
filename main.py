# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import flask
from flask import Flask,request
import Data
arr=Data.data
# obj={
#     'Id':1,
#     'name':'name',
#     'age':88,
#     'place':'Kajora'
# }
app = Flask(__name__)
@app.route('/add')
def add():
    obj=request.get_json()
    Data.addData(obj)
    return obj
@app.route('/remove/<id>', methods=['delete'])
def remove(id):

    if id.isnumeric():
        id=int(id)
    else:
        return 'Id is not Valid'
    return Data.removeData(id);
@app.route('/update/<id>',methods=['patch'])
def update(id):

    if id.isnumeric():
        id=int(id)
    else:
        return 'Id is not Valid'
    index=None
    index=Data.isAvailableAndGetIndex(id)
    if not index:
        return 'Id Not Found'
    Data.data[index].update(request.get_json())
    return Data.data[index]
@app.route('/')
def display():
    return Data.data




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
