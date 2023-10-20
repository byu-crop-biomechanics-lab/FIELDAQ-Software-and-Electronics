import datetime, time, math, csv

with open(foldername + str(self.fileName)) as testFile:
            readCSV = csv.reader(testFile, delimiter=',')
            testData = 0
            for row in readCSV:
                if testData == 1:
                    self.pot_angle.append(row[1])
                    self.imu_angle.append(row[2])
                    self.force_app.append(row[3])
                if str(row[0]) == 'TIME (milliseconds)' and testData == 0:
                    testData = 1