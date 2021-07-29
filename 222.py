import pymysql

connectr = pymysql.connect(
    host='localhost',
    user='root',
    port=9999,
    password='Tang5230',
    charset='utf8',
    db='quan'
)
cursor = connectr.cursor()
# cursor.execute("create database dsad character set utf8;")
# cursor.execute("use berrylook;")
sql = """
CREATE TABLE `athletic_shoes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Trade_name` varchar(255) NOT NULL,
  `Commodity_category` varchar(255) NOT NULL,
  `Applicantis_name` varchar(255) NOT NULL,
  `Applicantis_address` varchar(255) NOT NULL ,
  `Date_of_Application` varchar(255) NOT NULL ,
  `GoodsServices` TEXT NOT NULL ,
  `Agent_name` varchar(255) NOT NULL ,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (Trade_name)
) ENGINE=InnoDB;
"""
cursor.execute(sql)


# def mysql(Title, LowPrice, id, Descriptions_new):
#     connectr = pymysql.connect(
#         host='localhost',
#         user='root',
#         password='tang5230',
#         db='dx',
#         charset='utf8'
#     )
#     cursor = connectr.cursor()
#     sql = """INSERT INTO dresses(user_name,
#              user_iamg, user_price, user_descriptions)
#              VALUES ('%s','%s','%s','%s')""" % (Title, str(id) + '.jpg', LowPrice, Descriptions_new)
#     try:
#         cursor.execute(sql)
#         connectr.commit()
#     except Exception:
#         connectr.rollback()
#     finally:
#         cursor.close()
#         connectr.close()
# mysql(1,1,1,1)