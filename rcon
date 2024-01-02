import pymysql
import time
import rcon.source as rc
import sys
DB_HOST="DB_HOST"
DB_USER="DB_USER"
DB_PASS="DB_PASS"
DB_DB="DB_DB"
DB_TABLE="DB_TABLE"
RC_HOST="RC_HOST"
RC_PORT="RC_PORT"
RC_PASS="RC_PASS"
DELAY=10

added=[]
dbmy = pymysql.connect(host=DB_HOST,user=DB_USER,password=DB_PASS,database=DB_DB,autocommit=1)
rcclient=rc.Client(RC_HOST,int(RC_PORT))
rcclient.connect()
rcclient.login(RC_PASS)
cursor = dbmy.cursor()
sql = f"select * from {DB_TABLE}"
def main():
    while True:
        print("start add")
        relnum = cursor.execute(sql)
        result = cursor.fetchone()
        while result is not None:
            print(result)
            username=result[1]
            white=result[2]
            if username not in added and white==1:
                res=rcclient.run("whitelist add "+username)
                print(res)
                print(f"add {username} to whitelist")
                added.append(username)
            result = cursor.fetchone()
        print("sleep")
        relnum = cursor.execute(sql)
        time.sleep(DELAY)
def clean():
    print('cleaning')
    cursor.close()
    dbmy.close()
    rcclient.close()
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        clean()
        sys.exit(0)
