#!/opt/djenv/bin/python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import column, String, Integer, ForeignKey

engine = create_engine('sqlite:////root/test/devweb/day06/myansible/db.sqlite3', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class HostGroup(Base):
    __tablename__ = 'webansi_hostgroup'
    id = column(Integer, nullable=False, autoincrement=True, primary_key=True)
    group_name = column(String(50))

    def __str__(self):
        return '组：%s' % self.group_name


class Host(Base):
    __tablename__ = 'webansi_host'
    id = column(Integer, primary_key=True)
    hostname = column(String(50))
    ipaddr = column(String(15))
    group_id = column(Integer, ForeignKey('webansi_hostgroup.id'))

    def __str__(self):
        return '%s:%s=>%s' % (self.hostname, self.ipaddr, self.group)


class Module(Base):
    __tablename__ = 'webansi_module'
    id = column(Integer, primary_key=True)
    module_name = column(String(50))

    def __str__(self):
        return '模块:%s' % self.module_name


class Argument(Base):
    __tablename__ = 'webansi_argument'
    id = column(Integer, primary_key=True)
    arg_text = column(String(100))
    module_id = column(Integer, ForeignKey('webansi_module.id'))

    def __str__(self):
        return '%s=>%s' % (self.module, self.arg_text)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
