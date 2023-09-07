from sqlalchemy import create_engine;
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, backref
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

engine = create_engine('sqlite:///family.db')

connections = Table(
    'connections',
    Base.metadata,
    Column('individual1_id', ForeignKey('people.id'), primary_key=True),
    Column('individual2_id', ForeignKey('people.id'), primary_key=True),
    Column('relationship_id', ForeignKey('relationships.id'), primary_key=True),
    extend_existing=True,
)


class Person(Base):
    __tablename__ = "people"
    
    id = Column(Integer(), primary_key = True)
    name = Column(String(), index = True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    

    relationships = relationship('Relationship', secondary= connections, back_populates='people')


    def __repr__(self):
        return f'Name : {self.name}'



class Relationship(Base):
    __tablename__ = "relationships"
    
    id = Column(Integer(), primary_key = True)
    type_of_relationship = Column(String(), index = True)

    people = relationship('Person', secondary= connections, back_populates='relationships')


    def __repr__(self):
        return f'Type of Relationship : {self.type_of_relationship}'
        


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key = True)
    name = Column(String())



    family = relationship('Individual', backref=backref('user'))

    def __repr__(self):
        return f'Name : {self.name}'