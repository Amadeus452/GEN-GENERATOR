import os
import time
import Network.Whois
import argparse

os.system('clear')
print('installation of modules')
time.sleep(5)
os.system('pip install pysqlite3')
os.system('clear')
time.sleep(1)
os.system('clear')
print('the modules were installed successfully')

import sqlite3

print('creating a db') 
conn = sqlite3.connect("db.db")
cursor = conn.cursor()

ip = Network.Whois.MyIp()


print('Creating a table')

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

print('installation was successful')
print('use python GEN.py')
