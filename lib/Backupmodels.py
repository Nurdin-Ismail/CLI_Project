# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
# from sqlalchemy.orm import sessionmaker, relationship, backref 
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# connections = Table(
#     'connections',
#     Base.metadata,
#     Column('individual1_id', Integer, ForeignKey('people.id'), nullable=False),
#     Column('individual2_id', Integer, ForeignKey('people.id'), nullable=False),
#     Column('relationship_id', Integer, ForeignKey('relationships.id'), primary_key=True),
#     Column('users_id', Integer, ForeignKey('users.id'), primary_key=True)
# )       


# class Person(Base):
#     __tablename__ = "people"

#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     user_id = Column(Integer, ForeignKey('users.id'))

#     relationships = relationship(
#         'Relationship',
#         secondary='connections',
#         primaryjoin=(connections.c.individual1_id == id),
#         secondaryjoin=(connections.c.individual2_id == id),
#         back_populates='people',
#         foreign_keys=[connections.c.individual1_id, connections.c.individual2_id]
#     )


# class Relationship(Base):
#     __tablename__ = "relationships"

#     id = Column(Integer, primary_key=True)
#     type_of_relationship = Column(String, index=True)

#     people = relationship(
#         'Person',
#         secondary='connections',
#         primaryjoin=(connections.c.relationship_id == id),
#         secondaryjoin=(connections.c.individual1_id == id),
#         back_populates='relationships',
#         foreign_keys=[connections.c.relationship_id, connections.c.individual1_id]
#     )

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)

#     family = relationship('Person', backref=backref('users'))
