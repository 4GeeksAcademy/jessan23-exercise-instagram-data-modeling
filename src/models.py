import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

    

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id= Column(Integer, primary_key = True) 
    user_to_id = Column(Integer)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key = True)
    username= Column(String (100), nullable=False)
    firstname = Column(String (100), nullable=False)
    lastname = Column(String (100), nullable=False )
    email = Column (String(100), nullable=False )
    follower_id = Column(Integer, ForeignKey('follower.id'))
    follower = relationship ("Follower")

class Comment (Base):
    __tablename__ = 'comment'
    id = Column(Integer,primary_key = True)
    comment_text= Column(String (100), nullable=False)
    autor_id = Column(Integer )
    post_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id= Column (Integer, ForeignKey('post.id'))
    post= relationship("Post")


class Post (Base):
    __tablename__ = 'post'
    id = Column(Integer,primary_key = True)
    user_id= Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Media (Base):
    __tablename__ = 'media'
    id = Column(Integer,primary_key = True)
    type= Column(Enum, nullable=False)
    url = Column (String(300), nullable=False )
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
