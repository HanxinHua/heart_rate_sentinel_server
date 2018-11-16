from average import calculate_average
import pytest


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
