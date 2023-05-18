from sqlalchemy import *
from sqlalchemy.orm import *

Base = declarative_base()
engine = create_engine('sqlite:///drugs.db')
Base.metadata.create_all(engine)

class Drug(Base):
    __tablename__ = 'drugs'
    id = Column(Integer(), primary_key=True)
    med_name = Column(String)
    common_name = Column(String)
    symptoms = Column(Integer)

    def __repr__(self):
        return(
            f'Drug(id={self.id}, med_name={self.med_name}, common_name={self.common_name}, symptoms = {self.symptoms})'
        )

class Symptom(Base):
    __tablename__ = 'symptoms'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    type = Column(String())

    def __repr__(self):
        return(
            f'Symptom(id={self.id}, name={self.name}, type = {self.type})'
        )
    
class Remedy(Base):
    __tablename__ = 'remedies'
    id = Column(Integer(), primary_key=True)
    name = Column(String)
    symptoms = Column(Integer), ForeignKey('symptoms.id')

    def __repr__(self):
        return(
            f'Remedy(id={self.id}, name={self.name}, symptoms = {self.symptoms})'
        )