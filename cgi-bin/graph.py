#!/usr/bin/env python3
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import pylab

sensor_data = pd.read_csv("./cgi-bin/sound.csv",names=['sound','time'])
sound_data = sensor_data['sound'].values.tolist()
time_data = sensor_data['time'].values.tolist()

"""
i=0
while i < 167:
    if time_data[i] <= 500:
        time_data[i] = " "
    elif time_data[i] > 1000:
        time_data[i] = time_data[i]
    i = i+1
"""

"""
i=0
while i < 167:
    if i > 0 :
        time_data[i] = "A"
    else:
        time_data[i] = time_data[i]
    i = i+1
"""

pylab.figure(figsize=(10, 7))
plt.plot(time_data,sound_data,color='green')
plt.title('[Sound Of SeLab]',fontsize = 20)
plt.xlabel('time')
plt.xticks([0.0,60.0,120.0,180.0,240.0,300.0],rotation=30)
plt.ylabel('volume')
plt.tick_params(labelsize = 8)
plt.savefig("sound.png")

html_body = """
<html><body>
<img src= "../sound.png">
</body></html>
"""

print("Content-type: text/html\n")
print(html_body)
