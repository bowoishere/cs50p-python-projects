
def main():
    i = input("Input: ")
    o = ""
    vowels = "aiueoAIUEO"
    for char in i:
        if char in vowels:
            o += ""
        else:
            o += char
            continue

    print(f"Output: {o}")

main()
