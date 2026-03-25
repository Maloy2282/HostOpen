import os
from ftplib import FTP



print("Программа HostOpen впишет любой текст на ваш сайт через файл .html")
print("Нажмите Enter, чтобы продолджить")

n = input("")

if n == "":
    with open("index.html", "w", encoding='utf-8') as f:
        n2 = input("Введите текст:")
        html_temple = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text</title>
</head>
<body>
    <h1><b>{n2}</b></h1>
</body>
</html> """
        
        f.write(html_temple)

else:
    exit()

ftp = FTP()
ftp.connect('FTP IP', PORT)

ftp.login(user="FTP USER", passwd="FTP PASSWORD")
ftp.set_pasv(True)
local_filename = 'index.html'

ftp.cwd('Ur folder of files')

with open("index.html", 'rb') as file_data:
    ftp.storbinary('STOR ' + local_filename, file_data)

ftp.quit()

n4 = input("Успешно залито на сайт! Открыть его? Y/N: ")

if n4 == "Y":
    os.system("start Ur ip adress")

else:
    exit()
