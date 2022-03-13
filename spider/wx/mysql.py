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


class DailyJiong(Base):
    __tablename__ = 'daily_jiong'
    id = Column(INTEGER(11), primary_key=True)
    title = NotNullColumn(VARCHAR(255), default='')
    article_date = NotNullColumn(INTEGER(11), default=0)
    article_type = NotNullColumn(INTEGER(1), default=0)
    digest = NotNullColumn(VARCHAR(255), default='')
    cover = NotNullColumn(VARCHAR(255), default='')
    content_url = NotNullColumn(VARCHAR(255), default='')
    pic_url = NotNullColumn(VARCHAR(255), default='')
    pic_path = NotNullColumn(VARCHAR(255), default='')
    pic_qiniu_url = NotNullColumn(VARCHAR(255), default='')
    last_show_time = NotNullColumn(INTEGER(11), default=0)
    show_count = NotNullColumn(INTEGER(11), default=0)
    create_time = NotNullColumn(DATETIME)


def add(**kw):
    session.add(DailyJiong(**kw))
    session.commit()


def update(id, **kwargs):
    session.query(DailyJiong).filter_by(id=id).update(kwargs)
    session.commit()


def is_exist_by_content_url(url):
    res = session.query(DailyJiong).filter_by(content_url=url).first()
    return True if res else False


@models_to_list
def get_muti_undownload(count):
    """获取未下载的的文章"""
    return session.query(DailyJiong).filter_by(article_type=1, pic_url="")[0:count]


@models_to_list
def get_muti_unupload(start, end):
    """获取未上传的图片资源"""
    return session.query(DailyJiong).filter(DailyJiong.pic_url != "", DailyJiong.digest != "")[start:end]


@model_to_dict
def get_item_by_id(id):
    return session.query(DailyJiong).filter_by(id=id).first()


def get_random_item(count):
    return


@models_to_list
def get_muti():
    """
    获取资源拼接成文章
    规则：选取5篇文章
    1-今日话题：{head_title}
    2-4个月前随机一篇文章，出现次数低于3（未获取到优先扩大日期+1月，然后扩大出现次数）
    3-3个月篇随机一篇文章，出现次数低于3
    4-2个月前随机一篇文章，出现次数低于3
    5-2个月前随机一篇文章，出现次数低于3
    :return:
    """

    pass


if __name__ == '__main__':
    add(digest="致命打🐔现在你知道小孩使出”吃奶的力气”时妈妈到底有多疼了吧...猫猫推荐:这么大的雨，正常的狗不是应该马")
    session.close()
