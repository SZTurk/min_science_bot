print("👋 Hello! I'm MiniScienceBot. I can answer simple science questions.")
print("Type 'bye' to exit.\n")

while True:
    question = input("❓ Ask me a science question: ")

    if question.lower() == "bye":
        print("👋 Goodbye! Keep exploring science!")
        break

    elif "plants need" in question.lower():
        print("🌱 Plants need sunlight, water, air, and soil to grow.")
    elif "states of matter" in question.lower():
        print("🧊 There are 3 states of matter: solid, liquid, and gas.")
    elif "why do we breathe" in question.lower():
        print("😮 We breathe to take in oxygen and release carbon dioxide.")
    else:
        print("🤔 Sorry, I don't know the answer to that yet.")
