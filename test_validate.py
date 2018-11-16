from validate import *
import pytest
import datetime


@pytest.mark.parametrize("email,expected", [
    ("hh177@duke.edu", True),
    ("kh.gg.com", False),
    ("suyash.kumar@duke.edu", True),
    ("10000@qq.9ishell.com", True),
    ("qqk@dukeedu", False),
    ("jk.hh.ll@duke.edu", False),
    ])
def test_validate_email(email, expected):
    response = validate_email(email)
    assert response == expected


@pytest.mark.parametrize("date,expected", [
    ("2018-03-09 11:00:36.372339", datetime.datetime(2018, 3, 9, 11, 0, 36, 372339)),
    ("2018-03-09", datetime.datetime(2018, 3, 9)),
    ("2018-03-09 11:00:36", datetime.datetime(2018, 3, 9, 11, 0, 36)),
    ])
def test_str_to_datetime(date, expected):
    response = str_to_datetime(date)
    assert response == expected


@pytest.mark.parametrize("date,expected", [
    ("2018-03-09 11:00:36.372339", True),
    ("2018-03-09", True),
    ("20181111", False),
    ("this", False),
    ("1028-18-01", False),
    ("2018-03-09 11:00:36", True),
    ])
def test_validate_time(date, expected):
    response = validate_time(date)
    assert response == expected


@pytest.mark.parametrize("r_dic,expected", [
    ({"patient_id": "1",
      "attending_email": "suyash.kumar@duke.edu",
      "user_age": 50,
      }, True),
    ({"patient_id": 90,
      "attending_email": "suyash.kumar@duke.edu",
      "user_age": 50,
      }, False),
    ({"patient_id": "1",
      "attending_email": "suyash.kumar@duke.edu",
      "user_age": 0.5,
      }, True),
    ({"patient_id": "1",
      "attending_email": "suyash.kumar@duke.edu",
      }, False),
    ({"patient_id": "1",
      "user_age": 50,
      }, False),
    ({"attending_email": "suyash.kumar@duke.edu",
      "user_age": 50,
      }, False),
    ({"patient_id": "1",
      "attending_email": 90,
      "user_age": 50,
      }, False),
    (["1", "ff", 6], False),
    ])
def test_validate_add_patient(r_dic, expected):
    response = validate_add_patient(r_dic)
    assert response == expected


@pytest.mark.parametrize("r_dic,expected", [
    ({"patient_id": "1",
      "heart_rate": 100,
      }, True),
    ({"patient_id": "1",
      }, False),
    ({"heart_rate": 100,
      }, False),
    ({"patient_id": 9,
      "heart_rate": 100,
      }, False),
    ({"patient_id": "1",
      "heart_rate": "ij",
      }, False),
    (["1", "ff", 6], False),
    ])
def test_validate_heart_rate_request(r_dic, expected):
    response = validate_heart_rate_request(r_dic)
    assert response == expected


@pytest.mark.parametrize("r_dic,expected", [
    ({"patient_id": "1",
      "heart_rate_average_since": "2018-03-09 11:00:36.372339"
      }, True),
    ({"patient_id": "1",
      }, False),
    ({"heart_rate_average_since": "2018-03-09 11:00:36.372339",
      }, False),
    ({"patient_id": 9,
      "heart_rate_average_since": "2018-03-09 11:00:36.372339",
      }, False),
    ({"patient_id": "1",
      "heart_rate_average_since": 2018,
      }, False),
    (["1", "ff", 6], False),
    ])
def test_validate_interval_average_request(r_dic, expected):
    response = validate_interval_average_request(r_dic)
    assert response == expected
