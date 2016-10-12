'''
Created on Dec 19, 2014

@author: justin
'''
from datetime import datetime

now = datetime.now();
print now
print now.year
print now.month
print now.day
print now.hour
print now.minute
print now.second

data = open("timeData.txt", "r+")

year = int(data.readline())
month = int(data.readline())
day = int(data.readline())
hour = int(data.readline())
minute = int(data.readline())

print "previous date was:", year, month, day, hour, minute

pastMinuteTotal = 525949 * year \
    + 43829.1 * month \
    + 1440 * day \
    + 60 * hour \
    + minute

MinuteTotal = 525949 * now.year \
    + 43829.1 * now.month \
    + 1440 * now.day \
    + 60 * now.hour \
    + now.minute
    
print MinuteTotal - pastMinuteTotal

data.close()
data = open("timeData.txt", "w")

data.write(str(now.year) + "\n")
data.write(str(now.month) + "\n")
data.write(str(now.day) + "\n")
data.write(str(now.hour) + "\n")
data.write(str(now.minute) + "\n")

data.close()