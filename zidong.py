import pymysql
import random

connectr = pymysql.connect(
    host='106.55.26.254',
    user='root',
    port=3306,
    password='Tang5230.',
    charset='utf8',
    db='company',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = connectr.cursor()
sql = 'select * from about_us order by rand() limit 1;'

data_count = cursor.execute(sql)
data = cursor.fetchone()

print(data)