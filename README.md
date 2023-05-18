# Phase 3 CLI Project 

## MediMatch
This cli project prompts a user, presumably a sick user, to answer a question about what symptoms they are having. Then, based on chat gpt's idea of the most essential over the counter medications, the user is given instructions on what medicine to take instead of going to the doctor like a responsible person. 


- The directory structure of this project is laid out to separate the database code from the cli code as much as possible. Everything was edited within the lib folder, which also nested our db folder. This folder contained all of the alembic dependencies (migrations folder, alembic.ini, and the models.py and seeds.py folders which were used to populate the drugs.db tables)
-The cli.py folder was where the entire cli interface was run, using helper functions from helper.py. It is kept fairly simple, using mainly click to format and run the code, and the time library's sleep function to prevent all of the script from running simultaneously. 
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── db
    │   ├── models.py
    │   └── seed.py
    |   └── drugs.db
    ├── debug.py
    └── helpers.py
    └── cli.py

The drugs.py contained 3 tables, the Drugs, Symptoms, and Remedies tables
```
Running pipenv install and pipenv shell once forking this repo should give you all the dependencies you need to run the program locally. 