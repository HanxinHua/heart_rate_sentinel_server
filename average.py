def calculate_average(data, time, since):
    """
        :Synopsis: Judge whether the patient is tachycardic at that time
        :param data: The patient's heart beat data list
        :param time: The patient's time data list matching the heart beat
        :param since: The given time which is interested by the user
        :returns: The average heart beat since a time
    """
    sum_heart_rate = 0
    num = 0
    for i, t in enumerate(time):
        if t >= since:
            sum_heart_rate += data[i]
            num += 1
    return float(sum_heart_rate)/num
