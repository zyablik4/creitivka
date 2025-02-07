f = open('123.txt', 'r', encoding="utf-8")
str1 = f.readline().strip()
str2 = f.readline().strip()
str3 = f.readline().strip()
str4 = f.readline().strip()
if str1 == 'плюс':
    if str3 == 'плюс':
        print(int(str2)+int(str4))
    if str3 == 'минус':
        print(int(str2)-int(str4))
if str1 == 'минус':
    if str3 == 'плюс':
        print(-int(str2)+int(str4))
    if str3 == 'минус':
        print(-int(str2)-int(str4))
f.close()