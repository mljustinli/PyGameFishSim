'''
Created on Dec 19, 2014

@author: justin
'''
import time

try:
    data = open("unixTimeData.txt", "r+")
    start = float(data.readline())
    data.close()
except:
    start = time.time()
    
done = time.time()

data = open("unixTimeData.txt", "r+")
data.write(str(done))
data.close()

print done - start
