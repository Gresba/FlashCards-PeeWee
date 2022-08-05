from peewee import *

db = PostgresqlDatabase('flashcards', user='apple', password='', host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Card(BaseModel):
    title = CharField()
    back = CharField()
    correct = IntegerField()
    incorrect = IntegerField()
