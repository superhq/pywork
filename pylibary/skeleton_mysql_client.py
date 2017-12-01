# coding:utf-8
"""
通过pysql访问mysql
"""


import pymysql.cursors


connection = pymysql.connect(host= '192.168.0.61',
                             user='root',
                             password='sunrunvas',
                             db='mysql',
                             port=3306,
                             charset='utf8')
try:
    with connection.cursor() as cursor:
        sql = "show variables like 'max%'"
        print(cursor.execute(sql))
        #connection.commit()
        for i in cursor.fetchall():
            print(i)

finally:
    connection.close()

