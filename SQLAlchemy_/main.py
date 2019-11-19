"""
SQLAlchemy 练习
https://docs.sqlalchemy.org/en/13/orm/tutorial.html
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

# echo：是否打开日志
# 数据库文件为/database.db当前路径下的database.db中
# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///database.db', echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()


class User(Base):
    """
    继承Base的类，自动拥有__init__构造函数
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s',fullname='%s',nickname='%s')>" % (
            self.name, self.fullname, self.nickname
        )


if __name__ == '__main__':
    # 创建表
    Base.metadata.create_all(engine)

    # 清空表数据
    # 查询所有数据
    all = session.query(User).all()
    for user in all:
        # 删除一行数据
        session.delete(user)
    User.query().all()
    # 创建一行数据
    ed_user = User(name='ed', fullname='ed jones', nickname='ed nickname')
    # 增加、插入一行数据
    session.add(ed_user)
    # 提交事务
    session.commit()
    # 查询一条数据
    print(session.query(User).filter_by(name='ed').one())
    # 修改、更新数据
    ed_user.nickname = 'new_nickname'
    session.dirty
    print(session.query(User).filter_by(name='ed').one())
    # 提交事务
    session.commit()