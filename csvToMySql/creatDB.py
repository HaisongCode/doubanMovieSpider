import pymysql
 # 连接数据库
def connect_db():
    db = pymysql.connect("localhost", "root", "Tan707208", "douban", charset='utf8')
    return db

# 创建数据库
def create_table():
    con =connect_db()
    cursor = con.cursor()
    cursor.execute("DROP TABLE IF EXISTS DOUBANMOVIE")
    sql = """CREATE TABLE DOUBANMOVIE (
         RANK VARCHAR(10),
         NAME VARCHAR(100),
         SCORE VARCHAR(10),
         NUM VARCHAR(20),
         DIR VARCHAR(500),
         ACT VARCHAR(500),
         TYPE VARCHAR(500),
         YEAR VARCHAR(500),
         CITY VARCHAR(500),
         QUTOE VARCHAR(500))"""
    try:
        cursor.execute(sql)
        con.commit()
        print("创建成功")
        con.close()
    except:
        print("创建失败")
        con.rollback()
        con.close()

create_table()