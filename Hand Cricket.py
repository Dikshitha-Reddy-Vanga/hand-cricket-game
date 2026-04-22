import random

def toss():
    print("TOSS TIME!")
    choice = input("Choose Odd or Even: ").lower()
    user_num = int(input("Enter a number between 1 and 6: "))
    ai_num = random.randint(1, 6)

    print(f"AI chose: {ai_num}")

    if (user_num + ai_num) % 2 == 0:
        result = "even"
    else:
        result = "odd"

    if choice == result:
        decision = input("You won the toss! Choose Bat or Bowl: ").lower()
        return decision
    else:
        print("AI won the toss!")
        ai_decision = random.choice(["bat", "bowl"])
        print(f"AI chooses to {ai_decision}")
        return "bowl" if ai_decision == "bat" else "bat"


def batting(player):
    score = 0
    print(f"\n{player} is batting!")
    while True:
        user = int(input("Enter your number (1-6): "))
        ai = random.randint(1, 6)
        print(f"AI bowled: {ai}")

        if user == ai:
            print("OUT!")
            break
        score += user
        print(f"Score: {score}")
    return score


def bowling(player):
    score = 0
    print(f"\n{player} is bowling!")
    while True:
        user = int(input("Enter your bowl number (1-6): "))
        ai = random.randint(1, 6)
        print(f"AI played: {ai}")

        if user == ai:
            print("AI is OUT!")
            break
        score += ai
        print(f"AI Score: {score}")
    return score


# MAIN GAME
print("🏏 WELCOME TO HAND CRICKET 🏏")

first_choice = toss()

if first_choice == "bat":
    user_score = batting("You")
    print(f"\nYour total score: {user_score}")
    ai_score = bowling("You")
else:
    ai_score = bowling("You")
    print(f"\nAI total score: {ai_score}")
    user_score = batting("You")

print("\n🏆 MATCH RESULT 🏆")
if user_score > ai_score:
    print("🎉 You Win!")
elif user_score < ai_score:
    print("😢 AI Wins!")
else:
    print("🤝 It's a Tie!")
