from is_tachycardia import is_tachycardia
import pytest


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
