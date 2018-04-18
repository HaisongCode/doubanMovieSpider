import csv
import pymysql

ranks = []
names = []
scores = []
nums = []
dirs = []
acts = []
types = []
years = []
citys = []
qutoes = []

# 将csv中的数据一次存入到相应的列表中
def read_csv():
    with open('I:\doubanMovieSpider\douban.csv',encoding='utf-8') as f:
        csvRead = csv.reader(f,delimiter=',')
        for row in csvRead:
            rank = row[0]
            name = row[1]
            score = row[2]
            num = row[3]
            dir = row[4]
            act = row[5]
            type = row[6]
            year = row[7]
            city = row[8]
            qutoe = row[9]
            ranks.append(rank)
            names.append(name)
            scores.append(score)
            nums.append(num)
            dirs.append(dir)
            acts.append(act)
            types.append(type)
            years.append(year)
            citys.append(city)
            qutoes.append(qutoe)

# 连接数据库
def connect_db():
    db = pymysql.connect("localhost", "root", "Tan707208", "douban", charset='utf8')
    return db
#将数据插入到数据库中
def print_scv():
    # 将csv数据存入到相应的列表中
    read_csv()
    # 连接数据库
    db = connect_db()
    cur = db.cursor()
    for i in range(250):
        j = i+1
        sql = """INSERT INTO DOUBANMOVIE(RANK,NAME,SCORE,NUM,DIR,ACT,TYPE,YEAR,CITY,QUTOE)
                 VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""\
              %(ranks[j],names[j],scores[j],nums[j],dirs[j],acts[j],types[j],years[j],citys[j],qutoes[j])
        try:
            cur.execute(sql)
            db.commit()
            print("第"+j+"插入成功")
        except:
            print("第"+j+"插入失败")
    db.close()

print_scv()











