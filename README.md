# 航班延误预测系统

依赖软件版本：
- python 3.9
- MySql 8
- node 14

请注意软件版本，其他版本未作测试，不能保证正常运行！！！

## 安装MySql数据库

安装任意一种服务器类型数据库即可[MySql下载](https://dev.mysql.com/downloads/mysql/)

推荐：8.0版本的

也可以在百度网盘下载：

链接: [https://pan.baidu.com/s/1jv32CAvll6nE9Ei6Oq7yEw?pwd=jakr](https://pan.baidu.com/s/1jv32CAvll6nE9Ei6Oq7yEw?pwd=jakr)

提取码: jakr 

---

## 恢复备份的数据库

在 Mysql的命令行中

1. 创建一个数据库
```sql
create database if not exists db01;
```

2. 切换到创建的数据库
```sql
use db01;
```

3. 恢复备份表

```sql
source datas/mls.sql
```
注意，这里最好是绝对路径，比如 `E:\github\flight-delay-predict\datas\mls.sql`

---

## 怎么运行

修改 `config.py` 中的数据库配置



1. 安装第三方依赖

python的依赖
```shell
pip install -r requirements.txt
```

node的依赖
```shell
cd web/project/app

npm install
```

2. 运行后端API服务

```shell
python app.py
```

3. 启动Vue前端

```shell
cd web/project/app

npm run serve
```

4. 打开页面

[http://localhost:8080](http://localhost:8080)

这里的端口不一定是这个端口，可能有改变，请注意启动前端页面时候，输出的链接


## 目录结构

- API 这是后端API的目录
- datas 这是存储一些数据的目录
- doc 文档，里面有很多报告
- img 截图目录，基本不用管，没用
- modelTrain 模型训练的目录
- web 前端Vue的项目目录


请想看里面的DOC目录下的文档