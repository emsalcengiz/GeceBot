import random

class GeceBot:
    def __init__(self, name):
        self.name = name
        self.moods = ["happy", "sad", "hungry", "sleepy", "playful"]
    
    def get_mood(self):
        return random.choice(self.moods)

    def respond(self, user_input):
       
        mood = self.get_mood()
        if mood == "happy":
            return f"{self.name} is purring happily, enjoying the moment!"
        elif mood == "sad":
            return f"{self.name} meows sadly and looks out the window... alone."
        elif mood == "hungry":
            return f"{self.name} is meowing for food. It's time to feed her!"
        elif mood == "sleepy":
            return f"{self.name} is curled up, too tired to chat. She'll nap for a while."
        elif mood == "playful":
            return f"{self.name} wants to play! She swats at imaginary things and purrs with joy."

def start_chat():
    print("Hello! I'm Gece, your friendly chatbot. Ready to chat?")
    name = "Gece"
    cat = GeceBot(name)
    
    print(f"{name} is waiting, let's start!")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print(f"Gece: Bye bye! See you later. *meow* :)")
            break
        print(f"{cat.name}: {cat.respond(user_input)}")


if __name__ == "__main__":
    start_chat()

