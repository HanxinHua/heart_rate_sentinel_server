def calculate_average(data, time, since):
    sum_heart_rate = 0
    num = 0
    for i, t in enumerate(time):
        if t >= since:
            sum_heart_rate += data[i]
            num += 1
    return float(sum_heart_rate)/num
