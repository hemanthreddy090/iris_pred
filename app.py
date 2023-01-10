import pickle 
from flask import Flask,request

model = pickle.load(open('SVM.pickle','rb'))

app = Flask(__name__)

@app.route('/') # '/' -> denotes homepage
def homepage(): # <- handler function
    return 'API Server Launched'

@app.route('/predict',methods=['GET'])# 
def  predict():
    sl = float(request.args.get('sl'))
    sw = float(request.args.get('sw'))
    pl = float(request.args.get('pl'))
    pw = float(request.args.get('pw'))

    data = [[sl,sw,pl,pw]]
    result = model.predict(data)[0]
    return result
if(__name__=="__main__"):
    app.run(
        host = '0.0.0.0',
        port = 5000,
        debug = True
    )
