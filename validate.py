import logging
import re
import datetime as dt


def validate_add_patient(r_dic):
    try:
        assert (type(r_dic) == dict)
    except AssertionError:
        logging.error("request is not dic.")
        return False
    try:
        patient_id = r_dic["patient_id"]
    except KeyError:
        logging.error("patient_id is not in the dict.")
        return False
    try:
        attending_email = r_dic["attending_email"]
    except KeyError:
        logging.error("attending_email is not in the dict.")
        return False
    try:
        user_age = r_dic["user_age"]
    except KeyError:
        logging.error("user_age is not in the dict.")
        return False
    try:
        assert (type(patient_id) == str)
    except AssertionError:
        logging.error("patient_id is not str.")
        return False
    try:
        assert (type(attending_email) == str)
    except AssertionError:
        logging.error("attending_email is not str.")
        return False
    try:
        assert ((type(user_age) == float) or (type(user_age) == int))
    except AssertionError:
        logging.error("user_age is not number.")
        return False
    if not validate_email(attending_email):
        logging.error("attending_email is not valid.")
        return False
    return True


def validate_heart_rate_request(r_dic):
    try:
        assert (type(r_dic) == dict)
    except AssertionError:
        logging.error("request is not dic.")
        return False
    try:
        patient_id = r_dic["patient_id"]
    except KeyError:
        logging.error("patient_id is not in the dict.")
        return False
    try:
        heart_rate = r_dic["heart_rate"]
    except KeyError:
        logging.error("heart_rate is not in the dict.")
        return False
    try:
        assert (type(patient_id) == str)
    except AssertionError:
        logging.error("patient_id is not str.")
        return False
    try:
        assert ((type(heart_rate) == float) or (type(heart_rate) == int))
    except AssertionError:
        logging.error("heart_rate is not number.")
        return False
    return True


def validate_interval_average_request(r_dic):
    try:
        assert (type(r_dic) == dict)
    except AssertionError:
        logging.error("request is not dic.")
        return False
    try:
        patient_id = r_dic["patient_id"]
    except KeyError:
        logging.error("patient_id is not in the dict.")
        return False
    try:
        heart_rate_average_since = r_dic["heart_rate_average_since"]
    except KeyError:
        logging.error("heart_rate_average_since is not in the dict.")
        return False
    try:
        assert (type(patient_id) == str)
    except AssertionError:
        logging.error("patient_id is not str.")
        return False
    try:
        assert (type(heart_rate_average_since) == str)
    except AssertionError:
        logging.error("heart_rate_average_since is not str.")
        return False
    if not validate_time(heart_rate_average_since):
        logging.error("datetime is not in valid format.")
        return False
    return True


def validate_email(email):
    if len(email) > 5:
        if re.match("(\\w+\\.)?\\w+@(\\w+\\.)+[a-z]{2,3}", email) is not None:
            return True
    return False


def str_to_datetime(date):
    if ":" in date:
        if "." in date:
            return dt.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
        else:
            return dt.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    else:
        return dt.datetime.strptime(date, "%Y-%m-%d")


def validate_time(date):
    try:
        str_to_datetime(date)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    r = {
        "patient_id": "1",
        "user_age": 50,
        "attending_email": "suyash.kumar@duke.edu",
        "heart_rate": 100.1,
        "heart_rate_average_since": "2018-03-09 11:00:36.372339"
    }
    print(validate_heart_rate_request(r))
    print(validate_add_patient(r))
    print(validate_interval_average_request(r))
    print(validate_email("11@11.yy.com"))
    print(validate_email("1/1@11.com"))
    print(validate_email("suyash.kumar@duke.edu"))
    print(validate_email("hh177@duke.edu"))
    print(validate_email("k.11@11.com.cn"))
