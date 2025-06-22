import re
time = input("time: ")
time_split = re.split(r"[ /,:.|]",time)
def hours(time_split,time):
    h = int(time_split[0])
    m = int(time_split[1])
    s = int(time_split[2])
    if m < 60 and s < 60:
        return f'{time} in seconds : {((h*60 + m)*60)+s}'
    elif m > 60 or s > 60:
        return "erro"
    else:
        return "erro"
hours = hours(time_split,time)
print(hours)