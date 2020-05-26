import os
import time
import Network.Whois
import argparse

os.system('clear')
print('установка модулей')
time.sleep(5)
os.system('pip install pysqlite3')
os.system('clear')
time.sleep(1)
os.system('clear')
print('установка модулей произошла успешно')

import sqlite3

print('создание db') 
conn = sqlite3.connect("db.db")
cursor = conn.cursor()

ip = Network.Whois.MyIp()


print('Создание таблицы')

cursor.execute("""CREATE TABLE profile
                  (ip text, username text, password text, port text)
               """)

username = input('Input username: ')
password = input('input password: ')
port = input('Input port: ')

# Вставляем данные в таблицу
cursor.execute("""INSERT INTO profile
                  VALUES ('""" + ip + """', '""" + username + """', '""" + password + """',
                  '""" + port + """')"""
               )
# Сохраняем изменения
conn.commit()
conn.close()

print('установка прошла успешно')
print('используй python GEN.py')