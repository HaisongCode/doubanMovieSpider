import pymysql
def connect_db():
    db = pymysql.connect("localhost", "root", "Tan707208", "douban", charset='utf8')
    return db
def select_info():
    con = connect_db()
    cur = con.cursor()
    sql = """select * from doubanmovie where TYPE = '惊悚'"""
    try:
        cur.execute(sql)
        con.close()
        result = cur.fetchall()
        for row in result:
            rank = row[0]
            name = row[1]
            score = row[2]
            num = row[3]
            dir = row[4]
            act = row[5]
            ty = row[6]
            year = row[7]
            city = row[8]
            qutoe = row[9]
            print("rank=%s,name=%s,score=%s,num=%s,dir=%s,act=%s,ty=%s,city=%s,year=%s,qutoe=%s" \
                  %(rank,name,score,num,dir,act,ty,year,city,qutoe))
    except:
        print("失败")
    con.close()
select_info()


