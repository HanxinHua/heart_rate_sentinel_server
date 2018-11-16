import sys
from flask import Flask, jsonify,  request
import datetime
import sendgrid
from sendgrid.helpers.mail import *
import os
from is_tachycardia import is_tachycardia
from validate import *
import logging
from average import calculate_average
app = Flask(__name__)
patients = []


@app.route("/api/status/<patient_id>", methods=["GET"])
def status(patient_id):
    try:
        patient = [x for x in patients if x["patient_id"] == patient_id][0]
    except IndexError:
        logging.error("This patient is not in the system yet.")
        return "This patient is not in the system yet."
    age = patient["user_age"]
    time = patient["time"]
    heart = patient["heart_rate"]
    mail_add = patient["attending_email"]
    index = time.index(max(time))
    tag = is_tachycardia(heart[index], age)
    if tag:
        message = "Patient {} is tachycardic at {}".format(patient_id, str(time[index]))
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
    try:
        patient = [x for x in patients if x["patient_id"] == patient_id][0]
    except IndexError:
        logging.error("This patient is not in the system yet.")
        return "This patient is not in the system yet."
    return jsonify(patient["heart_rate"])


@app.route("/api/heart_rate/interval_average/<patient_id>", methods=["GET"])
def get_interval_average(patient_id):
    try:
        patient = [x for x in patients if x["patient_id"] == patient_id][0]
    except IndexError:
        logging.error("This patient is not in the system yet.")
        return "This patient is not in the system yet."
    data = patient["heart_rate"]
    time = patient["time"]
    try:
        since = time.index(min(time))
    except ValueError:
        logging.error("This patient has no heart_rate measurement yet.")
        return "This patient has no heart_rate measurement yet."
    ave = calculate_average(data, time, time[since])
    return "patient {} has average heart beat {} bpm".format(patient_id, ave)


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    r_dic = request.get_json()
    if validate_add_patient(r_dic):
        try:
            patient = [x for x in patients if x["patient_id"] == r_dic["patient_id"]][0]
            patient["attending_email"] = r_dic["attending_email"]
            patient["user_age"] = r_dic["user_age"]
        except IndexError:
            d = {
                "patient_id": r_dic["patient_id"],
                "attending_email": r_dic["attending_email"],
                "user_age": r_dic["user_age"],
                "heart_rate": [],
                "time": [],
            }
            patients.append(d)
            return jsonify(d)
    else:
        sys.exit(1)


@app.route("/api/heart_rate", methods=["POST"])
def post_heart_rate():
    r_dic = request.get_json()
    if not validate_heart_rate_request(r_dic):
        sys.exit(1)
    try:
        patient = [x for x in patients if x["patient_id"] == r_dic["patient_id"]][0]
    except IndexError:
        logging.error("This patient is not in the system yet.")
        return "This patient is not in the system yet."
    patient["heart_rate"].append(r_dic["heart_rate"])
    patient["time"].append(datetime.datetime.now())
    logging.info("Successfully post heart_rate.")
    return jsonify(patient)


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def post_interval_average():
    r_dic = request.get_json()
    if not validate_interval_average_request(r_dic):
        sys.exit(1)
    try:
        patient = [x for x in patients if x["patient_id"] == r_dic["patient_id"]][0]
    except IndexError:
        logging.error("This patient is not in the system yet.")
        return "This patient is not in the system yet."
    time = str_to_datetime(r_dic["heart_rate_average_since"])
    try:
        ave = calculate_average(patient["heart_rate"], patient["time"], time)
    except ZeroDivisionError:
        logging.error("This patient has no heart_rate measurement since the time yet.")
        return "This patient has no heart_rate measurement since the time yet."
    logging.info("Successfully calculate the heart_rate.")
    return jsonify(ave)


if __name__ == "__main__":
    app.run(host="127.0.0.1")
