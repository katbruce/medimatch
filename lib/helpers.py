import click
import time
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from db.models import Remedy, Symptom, Drug
session_maker = sessionmaker(bind=create_engine('sqlite:///drugs.db'))

def welcome():
    print("\n\n\n\n\n\n")
    click.echo(click.style("Welcome to Medi-Match", fg='red', bold=True, blink=True ))
    click.pause
    time.sleep(2)
    click.echo("\n\n")
    click.echo("I'm assuming you're not doing too great if you're on here...")
    click.pause
    time.sleep(2)
    click.echo("\n\n")
    click.echo("What is your name?")
    
def get_rems():
    time.sleep(1)
    click.echo("Have you tried to...")
    
    with session_maker() as session:
        remedy_records = session.query(Remedy).all()
        for remedy in remedy_records:
            time.sleep(2)
            click.echo(remedy.name)
        time.sleep(2.5)
        click.echo("Okay, if none of those work we have some other options.")
        time.sleep(1)
        symptom_check = session.query(Symptom).all()
        for symp in symptom_check:
            x = str(symp.id) + " " + symp.name
            click.echo(x)
            time.sleep(0.5)
        value = input("Please enter the number of your most pressing symptom...")

        this_symptom = session.query(Symptom).filter(Symptom.id==value).first().name
        the_drugs = session.query(Drug).filter(Drug.symptoms == value).first().common_name
        click.echo('So you have a bad case of the: '+this_symptom)
        time.sleep(1.5)
        click.echo("That's rough, buddy.")
        time.sleep(1.5)
        click.echo("Here's what you should take: ")
        click.echo(click.style(the_drugs, fg='red', bold=True))

    

def get_symptom(name):
    click.echo(f"Okay, {name}, let's see what's wrong here...")
    time.sleep(1)
    get_rems()
    
