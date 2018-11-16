import logging
import re
import datetime as dt


def validate_add_patient(r_dic):
    """
        :Synopsis: Judge whether the request format is legal
        :param r_dic: The patient's personal info request dict info
        :returns: True if it is legal and false otherwise
        :raise: AssertionError: data type is not legal
        :raise: KeyError: data cannot be found
    """
    try:
        assert (type(r_dic) == dict)
    except AssertionError:
        logging.error("request is not dic.\n")
        return False
    try:
        patient_id = r_dic["patient_id"]
    except KeyError:
        logging.error("patient_id is not in the dict.\n")
        return False
    try:
        attending_email = r_dic["attending_email"]
    except KeyError:
        logging.error("attending_email is not in the dict.\n")
        return False
    try:
        user_age = r_dic["user_age"]
    except KeyError:
        logging.error("user_age is not in the dict.\n")
        return False
    try:
        assert (type(patient_id) == str)
    except AssertionError:
        logging.error("patient_id is not str.\n")
        return False
    try:
        assert (type(attending_email) == str)
    except AssertionError:
        logging.error("attending_email is not str.\n")
        return False
    try:
        assert ((type(user_age) == float) or (type(user_age) == int))
    except AssertionError:
        logging.error("user_age is not number.\n")
        return False
    if not validate_email(attending_email):
        logging.error("attending_email is not valid.\n")
        return False
    return True


def validate_heart_rate_request(r_dic):
    """
        :Synopsis: Judge whether the request format is legal
        :param r_dic: The patient's heart rate request dict info
        :returns: True if it is legal and false otherwise
        :raise: AssertionError: data type is not legal
        :raise: KeyError: data cannot be found
    """
    try:
        assert (type(r_dic) == dict)
    except AssertionError:
        logging.error("request is not dic.\n")
        return False
    try:
        patient_id = r_dic["patient_id"]
    except KeyError:
        logging.error("patient_id is not in the dict.\n")
        return False
    try:
        heart_rate = r_dic["heart_rate"]
    except KeyError:
        logging.error("heart_rate is not in the dict.\n")
        return False
    try:
        assert (type(patient_id) == str)
    except AssertionError:
        logging.error("patient_id is not str.\n")
        return False
    try:
        assert ((type(heart_rate) == float) or (type(heart_rate) == int))
    except AssertionError:
        logging.error("heart_rate is not number.\n")
        return False
    return True


def validate_interval_average_request(r_dic):
    """
        :Synopsis: Judge whether the request format is legal
        :param r_dic: The patient's average heart beat request dict info
        :returns: True if it is legal and false otherwise
        :raise: AssertionError: data type is not legal
        :raise: KeyError: data cannot be found
    """
    try:
        assert (type(r_dic) == dict)
    except AssertionError:
        logging.error("request is not dic.\n")
        return False
    try:
        patient_id = r_dic["patient_id"]
    except KeyError:
        logging.error("patient_id is not in the dict.\n")
        return False
    try:
        heart_rate_average_since = r_dic["heart_rate_average_since"]
    except KeyError:
        logging.error("heart_rate_average_since is not in the dict.\n")
        return False
    try:
        assert (type(patient_id) == str)
    except AssertionError:
        logging.error("patient_id is not str.\n")
        return False
    try:
        assert (type(heart_rate_average_since) == str)
    except AssertionError:
        logging.error("heart_rate_average_since is not str.\n")
        return False
    if not validate_time(heart_rate_average_since):
        logging.error("datetime is not in valid format.\n")
        return False
    return True


def validate_email(email):
    """
        :Synopsis: Judge whether the email format is legal
        :param email: The email str
        :returns: True if it is a legal email format and false otherwise
    """
    if len(email) > 5:
        # use RFC standard
        if re.match("(\\w+\\.)?\\w+@(\\w+\\.)+[a-z]{2,3}", email) is not None:
            return True
    return False


def str_to_datetime(date):
    """
        :Synopsis: Transfer the date from str to datetime
        :param date: The date
        :returns: date in datetime type
    """
    if ":" in date:
        if "." in date:
            return dt.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
        else:
            return dt.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    else:
        return dt.datetime.strptime(date, "%Y-%m-%d")


def validate_time(date):
    """
        :Synopsis: Judge whether the date format is legal
        :param date: The date
        :returns: True if it is legal and false otherwise
        :raise: ValueError: data cannot be transferred to datetime
    """
    try:
        str_to_datetime(date)
        return True
    except ValueError:
        return False
