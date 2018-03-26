# -*-coding:utf-8 -*-
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 创建对象基类
Base = declarative_base()


# 定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()

# 创建新的user对象
new_user = User(id='5', name='Jerry')

session.add(new_user)

session.commit()

session.close()

session = DBSession()
user = session.query(User).filter(User.id == '5').one()
print('type:', type(user))
print('name:', user.name)
session.close()
