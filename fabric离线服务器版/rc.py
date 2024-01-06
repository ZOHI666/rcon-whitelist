import os
import sys
import time
import pymysql
import rcon.source as rc
import yaml

DB_HOST = ""  # 数据库主机
DB_USER = ""  # 数据库用户名
DB_PASS = ""  # 数据库密码
DB_DB = ""  # 数据库名称
DB_TABLE = ""  # 数据库表
RC_HOST = ""  # RCON主机
RC_PORT = ""  # RCON端口
RC_PASS = ""  # RCON密码

DELAY = 10

added = []

os.chdir(os.path.dirname(__file__))

def create_config_file():
    """
    创建配置文件
    :return: None
    """
    config_template = {
        "db": {
            "host": DB_HOST,
            "user": DB_USER,
            "password": DB_PASS,
            "database": DB_DB,
            "table": DB_TABLE
        },
        "rcon": {
            "host": RC_HOST,
            "port": RC_PORT,
            "password": RC_PASS
        }
    }
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    with open(config_path, "w") as f:
        yaml.dump(config_template, f)
    print("配置文件创建成功！位于：", config_path)

def load_config():
    """
    加载配置文件
    :return: 配置文件内容或None
    """
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        print("配置文件未找到！")
        return None
    return config

# 判断配置文件是否存在
if not os.path.exists(os.path.join(os.path.dirname(__file__), "config.yaml")):
    create_config_file()

config = load_config()

DB_HOST = config['db']['host']
DB_USER = config['db']['user']
DB_PASS = config['db']['password']
DB_DB = config['db']['database']
DB_TABLE = config['db']['table']
RC_HOST = config['rcon']['host']
RC_PORT = config['rcon']['port']
RC_PASS = config['rcon']['password']

added = []

def main():
    """
    主函数
    :return: None
    """
    while True:
        print("start add")
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_DB, autocommit=1)
        cursor = conn.cursor()
        sql = f"select * from {DB_TABLE}"  # 查询数据库中的记录
        cursor.execute(sql)
        results = cursor.fetchall()  # 获取查询结果
        for result in results:
            print(result)
            username = result[1]  # 获取用户名
            white = result[2]  # 获取权限
            if username not in added and white == 1:  # 如果用户名不在added列表且权限为1
                rcclient = rc.Client(RC_HOST, int(RC_PORT))  # 创建RCON客户端
                rcclient.connect()  # 连接RCON
                rcclient.login(RC_PASS)  # 登录RCON
                res = rcclient.run("easywhitelist add " + username)  # 执行RCON命令
                print(res)
                print(f"add {username} to easywhitelist")
                added.append(username)  # 将用户名添加到added列表
                rcclient.close()  # 关闭RCON客户端
        cursor.close()  # 关闭数据库游标
        conn.close()  # 关闭数据库连接
        print("sleep")
        time.sleep(DELAY)  # 等待DELAY秒

def clean():
    """
    清理函数
    :return: 退出程序
    """
    print('cleaning')
    sys.exit(0)

if __name__ == '__main__':
    try:
        main()  # 运行主函数
    except KeyboardInterrupt:
        clean()  # 运行清理函数
    else:
        messagebox.showinfo("生成成功", "配置文件已生成，路径为：{}".format(os.path.join(os.path.dirname(__file__), "config.yaml")))
