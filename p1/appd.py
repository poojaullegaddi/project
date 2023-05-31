from flask import Flask,redirect,render_template,url_for,request
import pickle
import numpy as np
app=Flask(__name__)
modeld=pickle.load(open('diabetes.pkl','rb'))
@app.route("/")
def home():
    return render_template("indexd.html")
@app.route("/predict", methods=["POST"])
def predict():
    float_features=[float(x) for x in request.form.values()]
    features=[np.array(float_features)]
    p = modeld.predict(features)
    if p==1:
        strr="You may have diabetes!"
    else:
        strr="You may not have diabetes!"
    return render_template("indexd.html",text_prediction="Your model output is {} which indicates that {}".format(p,strr))
if __name__=='__main__':
    app.run()