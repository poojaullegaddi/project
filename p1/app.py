# from flask import Flask,render_template,redirect, url_for,request
# import pickle
# import numpy as np
# #init app in flask
# app=Flask(__name__)
# model = pickle.load(open('pizza.pkl','rb'))
# #default route
# @app.route("/")
# def home():
#     return render_template("index.html")
# @app.route("/predict", methods=["POST"])
# def predict():
#     float_features=[float(x) for x in request.form.values()]
#     features=[np.array(float_features)]
#     p = model.predict(features)
#     if p==1:
#         strr="You can eat the pizza"
#     else: 
#         strr="You can't eat the pizza"
#     return render_template("index.html",text_prediction="Your model output is {} and {}".format(p,strr))
# if __name__=='__main__':
#     app.run()
from flask import Flask,render_template,redirect, url_for,request
import pickle
import numpy as np
#init app in flask
app=Flask(__name__)
modelp = pickle.load(open('pizza.pkl','rb'))
#default route
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    float_features=[float(x) for x in request.form.values()]
    features=[np.array(float_features)]
    p = modelp.predict(features)
    if p==1:
        strr="You can eat the pizza"
    else: 
        strr="You can't eat the pizza"
    return render_template("index.html",text_prediction="Your model output is {} and {}".format(p,strr))
if __name__=='__main__':
    app.run()