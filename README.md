# 注意事项 #
 本软件适用于fabric离线服务器1.17.1-1.20.2，或正版服务器1.9+

 准备：非正版验证服务器请下载[easywhitelist MOD](https://www.mcmod.cn/class/9265.html)后再使用此软件，正版验证服务器无需理会

## 使用方法 ##
1，首先要在我的世界服务器开启rcon功能并且配置rcon。

可以查看此教程进行配置https://www.zhihu.com/question/381405552

2，配置MySQL数据库，结构如下

![结构](https://img.jiahewufwq.space/images/2024/01/02/-2024-01-02-215059.png)

 ###### 注： 将数据表中的white默认改为0既可以添加玩家审核期功能，软件只会同步添加值为1的玩家的白名单

3，开始配置py文件

您需要更改代码中的一下项目

```DB_HOST="DB_HOST" //数据库地址
DB_USER="DB_USER" //数据库用户名
DB_PASS="DB_PASS" //数据库密码
DB_DB="DB_DB" //数据库名
DB_TABLE="DB_TABLE" //数据表名
RC_HOST="RC_HOST" //服务器rcon地址
RC_PORT="RC_PORT" //服务器rcon端口
RC_PASS="RC_PASS" //服务器rcon密码
```

以下是写法示例

```DB_HOST="127.0.0.1" //数据库地址
DB_USER="ZOHI" //数据库用户名
DB_PASS="123456" //数据库密码
DB_DB="sql" //数据库名
DB_TABLE="wl" //数据表名
RC_HOST="127.0.0.1" //服务器rcon地址
RC_PORT="25575" //服务器rcon端口
RC_PASS="123456" //服务器rcon密码
```

4,配置完成后请在终端中安装此程序所需要用到的python库

pymysql：

```
pip install pymysql
```

rcon：

```
pip install rcon
```

至此，配置结束，可以运行程序了

之后会更新带ui的程序版本，不用再自己配置源代码

如果想要工作人员帮忙配置源代码的，可以联系QQ：1241826692，需要赞助5RMB，或者进入我的服务器免费申请源代码配置，服务器官网https://www.jiahewu.top
