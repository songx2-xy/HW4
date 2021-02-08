def average(list):
    try:
        sum=0
        for i in list:
            sum+=i
        return sum/len(list)
    except(TypeError,ZeroDivisionError):
        return "Error"