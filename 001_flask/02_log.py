#coding:utf-8
from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)
## cknown_lib config
app.config['MONGO_HOST'] = '10.11.118.102',
app.config['MONGO_PORT'] = 22107
app.config['MONGO_DBNAME'] = 'cknown_tactics'
app.config['MONGO_USERNAME'] = 'cknown_tactics'
app.config['MONGO_PASSWORD'] = 'cknown_tactics'

@app.route('/')
def hello_world():
    cknown_tactics = PyMongo(app)
    a = cknown_tactics.db['tactics_ip'].find()
    for b in a:
        cknown_tactics.db['tactics_ip'].update({'_id':b['_id']},{'$set':{"type":b['key_words1'],"key_words1":''}})
        print b
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
