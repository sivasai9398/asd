from flask import Flask,render_template,request,url_for
import pickle
import sklearn
import pandas as pd
import joblib
model = joblib.load(open('ensemble.pkl', 'rb'))
application=Flask(__name__)
@application.route("/home",methods=["GET","POST"])
def home():
    return render_template('dia.html')
@application.route("/pr",methods=["GET","POST"])
def sad():
    if request.method == 'GET':
        return render_template('dia.html')

    if request.method == 'POST':
        BP = request.form['BP']
        BMI=request.form['BMI']
        DPG=request.form['DPF']
        preg=request.form['preg']
        gluc=request.form['Glucose']
        insulin=request.form['Insulin']
        Age=request.form['Age']
        #skin=request.form['skin']
        X=pd.DataFrame([[preg,gluc,BP,insulin,BMI,DPG,Age]],dtype=object)
        prediction=model.predict(X)
        if prediction==0:
            print("U don't have any chances of diabetes")
            return render_template("dia2.html")
        elif prediction==1:
            print("U have a chance of diabetes")
            return render_template("dia1.html")
        else:
            return render_template('dia.html')
if __name__ == "__main__":
    application.run(debug=True)
#infile.close()
