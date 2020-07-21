ge = input("Are you a cigarette addict older than 75 years old").title().strip()
disease = input("Do you have a severe chronic disease").title().strip()
immune = input("Is your immune system too weak").title().strip()

risk = bool((age == "Yes") or (disease == "Yes") or (immune == "Yes"))

if risk :
    print("You are in risk group")

    else:
        print("You are not in risky group")
