from flask import Flask
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate

from libs.orm import db


app=Flask(__name__)
# 设置密匙
app.secret_key=r'fawferawfavafeaf'
# 连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/weibo_democre'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 每次请求结束后都会自动提交数据库中的变动
db.init_app(app)

# 初始化迁移
manager=Manager(app)
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

@app.route('/')
def home():
    return 'hello world'



if __name__ == '__main__':
    manager.run()
