import requests
import datetime
import time


d = {
    "patient_id": "1",
    "attending_email": "hh177@duke.edu",
    "user_age": 50,
}
'''
requests.post("http://127.0.0.1:5000/api/new_patient", json=d)
d = {
    "patient_id": "2",
    "attending_email": "hh177@duke.edu",
    "user_age": 10,
}
requests.post("http://127.0.0.1:5000/api/new_patient", json=d)
d = {
    "patient_id": "3",
    "attending_email": "hh177@duke.edu",
    "user_age": 5,
}
'''
r = requests.post("http://vcm-7300.vm.duke.edu:5000/api/new_patient", json=d)
print(r.text)
time.sleep(1)
d = {
    "patient_id": "1",
    "heart_rate": 90
}
r = requests.post("http://vcm-7300.vm.duke.edu:5000/api/heart_rate", json=d)
print(r.text)
time.sleep(1)
d = {
    "patient_id": "1",
    "heart_rate": 100
}
t = datetime.datetime.now()
r = requests.post("http://vcm-7300.vm.duke.edu:5000/api/heart_rate", json=d)
time.sleep(1)
print(r.text)
d = {
    "patient_id": "1",
    "heart_rate": 110
}
r = requests.post("http://vcm-7300.vm.duke.edu:5000/api/heart_rate", json=d)
print(r.text)
time.sleep(1)
d = {
    "patient_id": "1",
    "heart_rate": 120
}
r = requests.post("http://vcm-7300.vm.duke.edu:5000/api/heart_rate", json=d)
print(r.text)
d = {
    "patient_id": "1",
    "heart_rate": 130
}
r = requests.post("http://vcm-7300.vm.duke.edu:5000/api/heart_rate", json=d)
print(r.text)
time.sleep(1)
d = {
    "patient_id": "1",
    "heart_rate": 140
}
r = requests.post("http://vcm-7300.vm.duke.edu:5000/api/heart_rate", json=d)
print(r.text)
time.sleep(1)
'''
d = {
    "patient_id": "2",
    "heart_rate": 150
}
requests.post("http://127.0.0.1:5000/api/heart_rate", json=d)
d = {
    "patient_id": "2",
    "heart_rate": 100
}
requests.post("http://127.0.0.1:5000/api/heart_rate", json=d)
d = {
    "patient_id": "3",
    "heart_rate": 120
}
requests.post("http://127.0.0.1:5000/api/heart_rate", json=d)
d = {
    "patient_id": "3",
    "heart_rate": 130
}
'''
d = {
    "patient_id": "1",
    "heart_rate_average_since": str(t)
}
r = requests.post("http://vcm-7300.vm.duke.edu:5000/api/"
                  "heart_rate/interval_average",
                  json=d)
print(r.text)
