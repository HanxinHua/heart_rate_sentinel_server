import requests


d = {
    "patient_id": "1",
    "attending_email": "hh177@duke.edu",
    "user_age": 50,
}
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
requests.post("http://127.0.0.1:5000/api/new_patient", json=d)
d = {
    "patient_id": "1",
    "heart_rate": 97
}
requests.post("http://127.0.0.1:5000/api/heart_rate", json=d)
d = {
    "patient_id": "1",
    "heart_rate": 101
}
requests.post("http://127.0.0.1:5000/api/heart_rate", json=d)
d = {
    "patient_id": "1",
    "heart_rate": 186
}
requests.post("http://127.0.0.1:5000/api/heart_rate", json=d)
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
requests.post("http://127.0.0.1:5000/api/heart_rate", json=d)
r = requests.get("http://127.0.0.1:5000/api/status/1")
print(r)
