import csv
import pymysql

mydb = pymysql.connect(host='127.0.0.1',
    user='root',
    passwd='',
    db='hackathon')
cursor = mydb.cursor()
if cursor:
    print("ww")

#csv_data = csv.reader(file('try.csv'))

with open('try.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        xx="INSERT INTO testcsv (srno,student_id,subject_id,mark,year )VALUES (%s,%s,%s,%s,%s)"
        print(xx)
        cursor.execute(xx,row)
        mydb.commit()
#close the connection to the database.
cursor.close()

