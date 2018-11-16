from validate import *
import pytest
import datetime
from is_tachycardia import is_tachycardia
from average import calculate_average


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
    ("2018-03-09 11:00:36.372339", datetime.datetime(2018, 3, 9, 11, 0, 36,
                                                     372339)),
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


@pytest.mark.parametrize("age, heart_rate,expected", [
    (50, 101, True),
    (40, 100, False),
    (15, 120, True),
    (12, 119, False),
    (11, 131, True),
    (8, 130, False),
    (7, 134, True),
    (5, 133, False),
    (4, 138, True),
    (3, 137, False),
    (2, 152, True),
    (1, 151, False),
    (0.9, 170, True),
    (0.5, 169, False),
    (0.4, 187, True),
    (0.25, 186, False),
    (1/12, 180, True),
    (2/12, 179, False),
    (7/356, 183, True),
    (8/356, 182, False),
    (3/356, 167, True),
    (4/356, 166, False),
    (2/356, 160, True),
    (1/356, 159, False),
    ])
def test_is_tachycardia(age, heart_rate, expected):
    response = is_tachycardia(heart_rate, age)
    assert response == expected


@pytest.mark.parametrize("data, time, since, expected", [
    ([1, 2, 3], [1, 2, 3], 1, 2),
    ([1, 2, 3], [1, 2, 3], 2, 2.5),
    ([1, 2, 3], [1, 2, 3], 1.5, 2.5),
    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 1, 3.5),
    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 3.5, 5),
    ])
def test_average(data, time, since, expected):
    response = calculate_average(data, time, since)
    assert response == expected
