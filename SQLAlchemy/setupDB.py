import csv,sqlite3, textOps

conn = sqlite3.connect('titanic.db')
csvFile = csv.DictReader(open('/media/share/Linux/titanic.csv','r'))
cur = conn.cursor()

fieldNames = textOps.sanitize(csvFile.fieldnames)
query = textOps.createSQL(fieldNames,'titanic')


#create table
cur.execute(query)


#put Data
data = []
for i in csvFile:
    temp = []
    for n in csvFile.fieldnames:
        temp.append(i[n])
    data.append(temp)

cur.executemany("INSERT INTO titanic VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?)", data)

conn.commit()
