def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    normalized = answer.strip().lower()

    right_answer = ["42", "forty-two", "forty two"]
    right_answer = [j.strip().lower() for j in right_answer]

    if normalized in right_answer:
        print("Yes")
    else:
        print("No")


main()
