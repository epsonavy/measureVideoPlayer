import csv

# CSV file head title
myData = []
myData.append(["From", "To", "Time spent(ms)"])

with open("log.txt") as search:
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
            #print(timeString)
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
