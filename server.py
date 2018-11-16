from flask import Flask, jsonify,  request
import datetime
import sendgrid
from sendgrid.helpers.mail import *
import os
from is_tachycardia import is_tachycardia
app = Flask(__name__)
patients = []


@app.route("/api/status/<patient_id>", methods=["GET"])
def status(patient_id):
    heart = []
    time = []
    age = 0
    mail_add = ""
    for item in patients:
        if item["patient_id"] == patient_id:
            age = item["user_age"]
            time = item["time"]
            heart = item["heart_rate"]
            mail_add = item["attending_email"]
            break
    temp = time[0]
    index = 0
    for i, t in enumerate(time):
        if temp < t:
            temp = t
            index = i
    tag = is_tachycardia(heart[index], age)
    if tag:
        message = "Patient {} is tachycardic at {}".format(patient_id, str(temp))
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email("alert@medicalcenter.com")
        to_email = Email(mail_add)
        subject = "Alert"
        mail_content = Content("text/plain", message)
        send_mail = Mail(from_email, subject, to_email, mail_content)
        response = sg.client.mail.send.post(request_body=send_mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)
    else:
        message = "This patient is not tachycardic."
    return message


@app.route("/api/heart_rate/<patient_id>", methods=["GET"])
def get_heart_rate(patient_id):
    heart = []
    for item in patients:
        if item["patient_id"] == patient_id:
            heart = item["heart_rate"]
    return jsonify(heart)


@app.route("/api/heart_rate/interval_average/<patient_id>", methods=["GET"])
def get_interval_average(patient_id):
    data = []
    for item in patients:
        if item["patient_id"] == patient_id:
            data = item["heart_rate"]
            break
    ave = sum(data)/float(len(data))
    return "patient {} has average heart beat {} bpm".format(patient_id, ave)


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    r = request.get_json()
    d = {
        "patient_id": r["patient_id"],  # usually this would be the patient MRN
        "attending_email": r["attending_email"],
        "user_age": r["user_age"],  # in years
        "heart_rate": [],
        "time": [],
    }
    patients.append(d)
    return jsonify(d)


@app.route("/api/heart_rate", methods=["POST"])
def post_heart_rate():
    r = request.get_json()
    order = -1
    for index, ppl in enumerate(patients):
        if ppl["patient_id"] == r["patient_id"]:
            order = index
            break
    if order != -1:
        patients[order]["heart_rate"].append(r["heart_rate"])
        patients[order]["time"].append(datetime.datetime.now())
        message = "Successfully post heart_rate."
    else:
        message = "There is no such patient yet."
    print(message)
    return message


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def post_interval_average():
    r = request.get_json()
    order = -1
    sum_heart_rate = 0
    num = 0
    ave = 0.0
    for index, item in enumerate(patients):
        if item["patient_id"] == r["patient_id"]:
            order = index
            break
    if order != -1:
        time = r["heart_rate_average_since"]
        for i, t in enumerate(patients[order]["time"]):
            if t > time:
                sum_heart_rate = sum_heart_rate + patients[order]["heart_rate"][i]
                num = num + 1 
        ave = float(sum_heart_rate)/num
        message = "Successfully post heart_rate."
    else:
        message = "There is no such patient yet."
    print(message)
    return ave


if __name__ == "__main__":
    app.run(host="127.0.0.1")
