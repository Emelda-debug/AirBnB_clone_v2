#!/usr/bin/python3
""" Creates a new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ create tables"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                format (getenv("HBNB_MYSQL_USER")
                    getenv("HBNB_MYSQL_PWD")
                    getenv("HBNB_MYSQL_DB")
                    getenv("HBNB_MYSQL_HOST")
                    getenv("HBNB_ENV")),
                pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns dictionary
        Return:
            returns dictionary of object
        """
        dic = {}
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
                objs = self.__session.query(cls)
                return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}for clase in lista:
    
    def new(self, obj):
        """adds new element in the table
        """
        self.__session.add(obj)

    def save(self):
        """saves all changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """deletes elements in the table
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """configuring 
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()
