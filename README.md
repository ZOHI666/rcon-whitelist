# 注意事项 #
 本软件适用于fabric离线服务器1.17.1-1.20.2，或正版服务器1.9+

 准备：

1，非正版验证服务器请下载[easywhitelist MOD](https://www.mcmod.cn/class/9265.html)后再使用此软件，正版验证服务器无需理会

2，请将正式版的zip文件下载解压后再进行操作

## 使用方法 ##
1，首先要在我的世界服务器开启rcon功能并且配置rcon。

可以查看此教程进行配置https://www.zhihu.com/question/381405552

2，配置MySQL数据库的数据表，结构如下

![结构](https://img.jiahewufwq.space/images/2024/01/02/-2024-01-02-215059.png)

 ##### 注： 将数据表中的white默认改为0既可以添加玩家审核期功能，软件只会同步添加值为1的玩家的白名单

3，开始配置配置文件

配置文件位于解压文件的\dist\rc\_internal\config.yaml中，请使用文本编辑器打开config.yaml文件，并开始下面的编辑教程

您需要更改配置文件中的一下项目

```
db:
  database: ''
  host: ''
  password: ''
  table: ''
  user: ''
rcon:
  host: ''
  password: ''
  port: ''
```

以下是写法示例

```
db:
  database: 'sql' //数据库名称
  host: '127.0.0.1' //数据库地址
  password: '123456' //数据库连接密码
  table: 'wl' //数据表名称
  user: 'mysql' //数据库用户
rcon:
  host: '127.0.0.1' //服务器地址
  password: '123456' //服务器rcon连接密码
  port: '25575' //服务器rcon端口
```

至此，配置结束，可以运行程序了

请运行解压目录中的start.exe程序

之后会更新带ui的程序版本，不用再自己配置配置文件

最后看看我的MC服务器吧：），https://www.jiahewu.top
