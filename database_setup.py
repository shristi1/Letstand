from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    level = Column(Integer, nullable=False)

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    posts = relationship("CategoryPost", backref="category")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'posts' : [posts.serialize for post in self.posts]
        }


class CategoryPost(Base):
    __tablename__ = 'category_post'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    creation_date = Column(DateTime, nullable = False)
    category_id = Column(Integer, ForeignKey('category.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'creation_date' : self.creation_date
        }


engine = create_engine('sqlite:///forum.db')


Base.metadata.create_all(engine)