#!/opt/djenv/bin/python

import json

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:////root/test/devweb/day06/myansible/db.sqlite3'
)

Session = sessionmaker(bind=engine)
Base = declarative_base()


class HostGroup(Base):
    __tablename__ = 'webansi_hostgroup'
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(50), nullable=False, unique=True)

    def __str__(self):
        return "组: %s" % self.group_name


class Host(Base):
    __tablename__ = 'webansi_host'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(50), nullable=False, unique=True)
    ipaddr = Column(String(15), nullable=False, unique=True)
    group_id = Column(Integer, ForeignKey('webansi_hostgroup.id'))

    def __str__(self):
        return "%s: %s" % (self.hostname, self.ipaddr)


if __name__ == '__main__':
    session = Session()

    result = dict()

    qset = session.query(HostGroup.group_name, Host.ipaddr).join(Host)

    for group, ip in qset:
        if group not in result:
            result[group] = {}
            result[group]['hosts'] = []

        result[group]['hosts'].append(ip)

    print(json.dumps(result))
    session.close()
