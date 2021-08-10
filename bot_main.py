from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer

from tkinter import *

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

# print("Talk to bot ")
# while True:
#     my_question=input()
#     if my_question=='exit':
#         break
#     answer=bot.get_response(my_question)
#     print("bot : ",answer)


main = Tk()

main.geometry("650x650")
main.title("CHAT BOT")

image_given=PhotoImage(file="bot_image/bot_img.png")

photoL = Label(main,image=image_given)
photoL.pack(pady=20)

def ask():
    query = textField.get()
    ans_from_bot=bot.get_response(query)
    messages.insert(END, "you : " + query)
    messages.insert(END, "Bot : " + ans_from_bot)
    textField.delete(0 , END)




frame=Frame(main)

scroll=Scrollbar(frame)

messages=Listbox(frame , width=70 , height=20)

scroll.pack(side=RIGHT , fill=Y)



messages.pack(side=LEFT , fill=BOTH , pady=10)
frame.pack()

# making creating text filed !!!

textField = Entry(main , font=("Dancing Script", 20))

textField.pack(fill=X,pady=10)

button=Button(main,text="Pucheye" , font=("Verana" , 10) , command=ask)

button.pack()



main.mainloop()