from flask import Flask, render_template,jsonify,request
import config
from Project.utils import MedicalInsurance

app = Flask(__name__)
@app.route("/")
def Morning_class():
    # return "Success"
    return render_template("index.html")

@app.route("/predict_charges",methods = ["POST","GET"])
def get_insurance_charges():
    if request.method == "POST":
        print("WE ARE RUNNING POST METHOD")
        data = request.form
        age = int(data["age"])
        sex = data["sex"]
        bmi = eval(data["bmi"])
        children = int(data["children"])
        smoker = data["smoker"]
        region = data["region"]
        med_ch = MedicalInsurance(age,	sex,	bmi,	children,	smoker,region)
        charges = med_ch.get_predicted_charges()
        return jsonify({"Result":f"Predict medical Insurance charges {charges}"})
    else:
        print("we are running get method")
        age = int(request.args.get("age"))
        sex = request.args.get("sex")
        bmi = int(request.args.get("bmi"))
        children = int(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")
        med_ch = MedicalInsurance(age,	sex,	bmi,	children,	smoker,region)
        charges = med_ch.get_predicted_charges()
        return jsonify({"Result":f"Predict medical Insurance charges {charges}"})



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER)
