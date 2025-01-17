f = open('123.txt', 'r', encoding="utf-8")
temp = f.readline()
dav = f.readline()
if int(temp) >= 10 and int(temp) <= 30 and int(dav) >= 40 and int(dav) <= 60:
    print('Температура и влажность в норме')
if int(temp) < 10 or int(temp) > 30:
    print('Температура не в норме!')
if int(dav) < 40 or int(dav) > 60:
    print('Давление не в норме!')
f.close()