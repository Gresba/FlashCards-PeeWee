from peewee import *

db = PostgresqlDatabase('flashcards', user='apple', password='', host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Card(BaseModel):
    title = CharField()
    content = CharField()
    correct = IntegerField()
    incorrect = IntegerField()

db.drop_tables([Card])
db.create_tables([Card])

def makeCard():
    title = input('Title of Card')
    content = input('Content of Card')
    card = Card(title='f{title}', content='f{content}')
    card.save()

def startGame(amountOfCards):
    cards = Card.select().limit(amountOfCards)
    print(cards)

choice = input('Make a card or test knowledge?`\n1 - Make a card\n2 - Test knowledge\nChoice: ')

if choice == "1":
    makeCard()
elif choice == "2":
    amountOfCards = int(input('How many cards would you like to study? '))
    startGame(amountOfCards)
