import pymysql
import traceback
import sys


class MysqlUtil():
    def __init__(self):
        """
        初始化方法
        """
        host = '3.143.242.127'
        user = 'root'
        password = 'Tang5230.'
        database = 'notebook'
        self.db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=database
        )
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)  # 设置游标，并将游标位置设置字典类型

    def insert(self, sql):
        """
        :param sql: 插入数据库的SQL
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as file:
            print('发生异常', file)
            self.db.rollback()
        finally:
            self.db.close()

    def fetchone(self, sql):
        """
        :param sql:查询数据库单个结果集
        :return: fetchone():该方法获取下一个查询结果集，结果集是一个对象176678
        """
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
        except:
            traceback.print_exc()
            self.db.rollback()
            result = '查询异常'
        finally:
            self.db.close()
        return result

    def fetchall(self, sql):
        """
        :param sql: 查询数据库：多个结果集
        :return:
        """
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except:
            info = sys.exc_info()
            print(info[0], ':', info[1])
            self.db.rollback()
            results = '查询异常'
        finally:
            self.db.close()
        return results

    def delete(self,sql):
        """
        :param sql: 删除
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            f = open('\log.txt','a+')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            self.db.rollback()
        finally:
            self.db.close()

    def update(self,sql):
        """
        :param sql: 更新字段
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
        finally:
            self.db.close()

