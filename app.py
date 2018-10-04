from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# enable browser logging
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL', 'level':'INFO' }
driver = webdriver.Chrome('./chromedriver', service_args=["--verbose", "--log-path=./mylog.log"])
# load some site
driver.get('https://dev.gamespot.com/videos/pubgs-new-update-shakes-up-the-desert-map-and-blue/2300-6443547/?debug_video_player=1')
# print messages
# for entry in driver.get_log('browser'):
#     print entry

import csv

# CSV file head title
myData = []
myData.append(["From", "To", "Time spent(ms)"])

with open("mylog.log") as search:
    timestamps = []
    descriptions = []
    for line in search:
        if line.find(">>>>>>>>>>") is not -1:
            text_start = line.find(">>>>>>>>>>") + 10
            text_end = line.find("at")
            text = line[text_start:text_end]
            descriptions.append(text)

            timeString_start = line.find(" : ") + 3
            timeString = line[timeString_start:]
            timestamps.append(timeString)

    for i in range(len(descriptions) - 1):
        print("{} => {} spent time {} ms".format(descriptions[i], descriptions[i + 1], int(timestamps[i + 1]) - int(timestamps[i])))

        # Adding data to CSV file
        myData.append([descriptions[i], descriptions[i + 1], int(timestamps[i + 1]) - int(timestamps[i])])
        myFile = open('result.csv', 'w')
        with myFile:
           writer = csv.writer(myFile)
           writer.writerows(myData)

print("ALL saved in result.csv file.")

driver.close()
