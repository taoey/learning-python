import logging
from functools import partial

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, class_mapper
from sqlalchemy import create_engine, Column, DATETIME
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, pymysql

# ------------------------------mysql初始化--------------------------------------

Base = declarative_base()
engine = create_engine("mysql+pymysql://root:123456@47.98.165.192:3366/wx_gzh?charset=utf8mb4")
Session = sessionmaker(bind=engine)
NotNullColumn = partial(Column, nullable=False, server_default='')

session = Session()  # 全局session


def model2dict(model):
    if not model:
        return {}
    fields = class_mapper(model.__class__).columns.keys()
    return dict((col, getattr(model, col)) for col in fields)


def model_to_dict(func):
    def wrap(*args, **kwargs):
        ret = func(*args, **kwargs)
        return model2dict(ret)

    return wrap


def models_to_list(func):
    def wrap(*args, **kwargs):
        ret = func(*args, **kwargs)
        return [model2dict(r) for r in ret]

    return wrap


def tuples_first_to_list(func):
    def wrap(*args, **kwargs):
        ret = func(*args, **kwargs)
        return [item[0] for item in ret]

    return wrap


# -------------------------------业务逻辑----------------------------------


class Vmgirls(Base):
    __tablename__ = 'vmgirls'
    id = Column(INTEGER(20), primary_key=True)
    title = NotNullColumn(VARCHAR(300), default='')
    author = NotNullColumn(VARCHAR(128), default=0)
    url = NotNullColumn(VARCHAR(300), default='')
    tag = NotNullColumn(VARCHAR(100), default='')
    view_num = NotNullColumn(INTEGER(11), default=0)
    like_num = NotNullColumn(INTEGER(11), default=0)
    status = NotNullColumn(INTEGER(1), default=0)


def add(**kw):
    try:
        session.add(Vmgirls(**kw))
        session.commit()
    except Exception as e:
        print(kw, e)
        session.rollback()


def update(id, **kwargs):
    session.query(Vmgirls).filter_by(id=id).update(kwargs)
    session.commit()


@models_to_list
def get_unsave(count):
    return session.query(Vmgirls).filter_by(status=0)[0:count]



if __name__ == '__main__':
    data = {"title":"hello"}
    add(**data)
    session.close()
