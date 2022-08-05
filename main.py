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

db.create_tables([Card])

def makeCard():
    title = input('Title of Card: ')
    content = input('Content of Card: ')
    card = Card(title=title, content=content, correct = 0, incorrect = 0)
    card.save()

def startGame(amountOfCards):
    cards = Card.select().limit(amountOfCards)
    for card in cards:
        answer = input(f"Card Title: {card.title}: What is the content? ")
        if(answer == card.content):
            print('Correct!')
            card = Card.get(Card.title == card.title)
            card.correct = card.correct + 1
        else:
            print('Incorrect!')
            card = Card.get(Card.title == card.title)
            card.incorrect = card.incorrect + 1

choice = input('Make a card or test knowledge?`\n1 - Make a card\n2 - Test knowledge\nChoice: ')

if choice == "1":
    makeCard()
elif choice == "2":
    amountOfCards = int(input('How many cards would you like to study? '))
    startGame(amountOfCards)
