#!/usr/bin/env python3
from models import Drug, Symptom, Remedy
from sqlalchemy import *
from sqlalchemy.orm import *
Base = declarative_base()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///drugs.db')
    Base.metadata.create_all(engine)
    session_maker = sessionmaker(bind=create_engine('sqlite:///drugs.db'))
    
    meds = [
        Drug(id=1,med_name="acetaminophen", common_name="tylenol", symptoms = 1),
        Drug(id=2,med_name = "ibuprofin", common_name="advil", symptoms = 2),
        Drug(id=3,med_name="naproxen", common_name="aleve", symptoms= 2),
        Drug(id=4,med_name="diphenhydramine", common_name="benadryl", symptoms = 3),
        Drug(id=5,med_name= "cetitizine", common_name="zyrtec", symptoms= 3),
        Drug(id=6,med_name="Lataradine", common_name="claritin", symptoms= 3),
        Drug(id=7,med_name="bismuth sublacylate", common_name= "pepto-bismol", symptoms= 4),
        Drug(id=8,med_name = "calcium carbonate", common_name= "tums", symptoms = 5),
        Drug(id=9,med_name= "loperamide", common_name="imodium",symptoms= 6),
        Drug(id=10,med_name = "omeprazole", common_name="prilosec", symptoms = 7),
        Drug(id=11,med_name="dextromethorphan", common_name="robitussin", symptoms=8),
        Drug(id=12,med_name="pseudoephedrine", common_name="sudafed", symptoms=9),
        Drug(id=13,med_name="guaifenesin", common_name = "mucinex", symptoms = 9),
    ]
    with session_maker() as session:
        for item in meds:
            session.add(item)
        session.commit()
    
    symps = [
        Symptom(id=1, name="fever", type="cold"),
        Symptom(id=2, name = "pain", type="multi-use"),
        Symptom(id=3, name = "allergies", type= "seasonal"),
        Symptom(id=4, name="tummy hurt", type="IBS"),
        Symptom(id=5, name="indigestion", type="IBS"),
        Symptom(id=6, name= 'diarrhea', type='IBS'),
        Symptom(id=7, name="heartburn", type="IBS"),
        Symptom(id=8, name="cough", type="cold"),
        Symptom(id=9, name="congestion", type="cold")
    ]
    
    with session_maker() as session:
        for item in symps:
            session.add(item)
        session.commit()

    remedies = [
        Remedy(id=1, name= "Drink plenty of fluids.", symptoms = "all"),
        Remedy(id=2, name= "Get some rest", symptoms="all"),
        Remedy(id=3, name = "You could just take some Nyquil and end it all", symptoms = "all")
    ]

   
    with session_maker() as session:
        for item in remedies:
            session.add(item)
        session.commit()
    
    
