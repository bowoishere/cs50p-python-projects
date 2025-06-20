def main():
    greet = input("Greeting: ").strip().lower()

    responses = {
        "hello": 0,
        "hello, newman": 0,
        "hey": 20,
        "how you doing?": 20,
        "how's it going": 20,
        "what's happening?": 100,
        "what's up?": 100
    }

    print(f"${responses.get(greet, 100)}")

main()
