from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer

bot = ChatBot("My Bot")

conv = [
    'hello',
    'Hi there',
    'What is your name?',
    'My name is bot , made by anukaal',
    'How are you?',
    'I am good',
    'Thanku',
    'In which city do you live',
    'I live in Bokaro steel city'

]

trainer=ListTrainer(bot)

# Now Training the bot with the help of trainer 

trainer.train(conv)

# answer=bot.get_response("what is your name?")
# print(answer)

print("Talk to bot ")
while True:
    my_question=input()
    if my_question=='exit':
        break
    answer=bot.get_response(my_question)
    print("bot : ",answer)


