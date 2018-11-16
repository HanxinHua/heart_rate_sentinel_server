def is_tachycardia(heart_rate, age):
    if age > 15:
        if heart_rate > 100:
            return True
        else:
            return False
    elif age > 11:
        if heart_rate > 119:
            return True
        else:
            return False
    elif age > 7:
        if heart_rate > 130:
            return True
        else:
            return False
    elif age > 4:
        if heart_rate > 133:
            return True
        else:
            return False
    elif age > 2:
        if heart_rate > 137:
            return True
        else:
            return False
    elif age >= 1:
        if heart_rate > 151:
            return True
        else:
            return False
    elif age >= 0.5:
        if heart_rate > 169:
            return True
        else:
            return False
    elif age >= 0.25:
        if heart_rate > 186:
            return True
        else:
            return False
    elif age >= 1/12:
        if heart_rate > 179:
            return True
        else:
            return False
    elif age >= 7/356:
        if heart_rate > 182:
            return True
        else:
            return False
    elif age >= 3/356:
        if heart_rate > 166:
            return True
        else:
            return False
    else:
        if heart_rate > 159:
            return True
        else:
            return False
