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

def make_card():
    title = input('Title of Card: ')
    content = input('Content of Card: ')
    card = Card(title=title, content=content, correct = 0, incorrect = 0)
    card.save()

def start_game(amountOfCards):
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
        card.save()

def show_cards():
    cards = Card.select()
    counter = 1
    for card in cards:
        print("----------------------")
        print(f"[ Card {counter} ]:")
        print(f"Card: {card.title}")
        print(f"Content: {card.content}")
        print("----------------------\n")
        counter = counter + 1

choice = 0

while choice != "5":
    choice = input('Choose an option\n1 - Show all cards\n2 - Make a card\n3 - Test knowledge\n4 - Delete Card\n5 - Exit\nChoice: ')
    if choice == "1":
        show_cards()
    elif choice == "2":
        make_card()
    elif choice == "3":
        amountOfCards = int(input('How many cards would you like to study? '))
        start_game(amountOfCards)
    elif choice == "4":
        title = input("Enter the title of the card you want to delete: ")
        card = Card.get(Card.title == title)
        card.delete_instance()
        print(f"Deleted Card {title}")
    elif choice == "5":
        print("Thank you for using flashcards")
        print("")
        print("Here is your current flashcards score (Correct/Incorrect)")
        cards = Card.select()
        for card in cards:
            print(f"Flashcard Title: {card.title}")
            print(f"Correct: {card.correct}")
            print(f"Incorrect: {card.incorrect}\n")
