import datetime
import webbrowser


def show_help():
    print("\n===== AVAILABLE COMMANDS =====")
    print("hello")
    print("time")
    print("date")
    print("google")
    print("youtube")
    print("search <topic>")
    print("help")
    print("exit")
    print("==============================")


print("=" * 50)
print("         VOICE ASSISTANT")
print("=" * 50)
print("Hello! I am your Voice Assistant.")
show_help()

while True:
    command = input("\nEnter Command: ").lower().strip()

    if command == "hello":
        print("Hello! How can I help you?")

    elif command == "time":
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print("Current Time:", current_time)

    elif command == "date":
        current_date = datetime.date.today()
        print("Today's Date:", current_date)

    elif command == "google":
        print("Opening Google...")
        webbrowser.open("https://www.google.com")

    elif command == "youtube":
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif command.startswith("search"):
        query = command[6:].strip()

        if query:
            print("Searching for:", query)
            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )
        else:
            print("Please enter a topic to search.")

    elif command == "help":
        show_help()

    elif command == "exit":
        print("Goodbye! Have a great day.")
        break

    else:
        print("Command not recognized.")
        print("Type 'help' to see available commands.")