# 配置数据库
hostname = '127.0.0.1'
port = '3306'
database = 'db01'
username = 'root'
pwd = '123456'
dburl = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(username, pwd, hostname, port, database)