from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship, backref 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# class Connection(Base):
#     __tablename__ = 'connections'

#     individual1_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
#     individual2_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
#     relationship_id = Column(Integer, ForeignKey('relationships.id'), primary_key=True)
#     users_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

#     # Define relationships to other tables if needed
#     individual1 = relationship('Person', foreign_keys=[individual1_id])
#     individual2 = relationship('Person', foreign_keys=[individual2_id])
    
   

#     def __init__(self, individual1_id, individual2_id, relationship_id, users_id):
#         self.individual1_id = individual1_id
#         self.individual2_id = individual2_id
#         self.relationship_id = relationship_id
#         self.users_id = users_id     


# class Person(Base):
#     __tablename__ = "people"

#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     user_relashionship= Column(String)

#     relationships = relationship(
#         'Relationship',
#         secondary='connections',
#         primaryjoin=(Connection.individual1_id == id),
#         secondaryjoin=(Connection.individual2_id == id),
#         back_populates='people',
#         foreign_keys=[Connection.individual1_id, Connection.individual2_id]
#     )


# class Relationship(Base):
#     __tablename__ = "relationships"

#     id = Column(Integer, primary_key=True)
#     type_of_relationship = Column(String, index=True)

#     people = relationship(
#         'Person',
#         secondary='connections',
#         primaryjoin=(Connection.relationship_id == id),
#         secondaryjoin=(Connection.individual1_id == id),
#         back_populates='relationships',
#         foreign_keys=[Connection.relationship_id, Connection.individual1_id]
#     )
    
    

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)

#     family = relationship('Person', backref=backref('users'))
