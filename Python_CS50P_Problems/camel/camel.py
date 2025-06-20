def main():
    subject = input("camelCase: ")
    hasil = ""

    for i in subject:
        if i.isupper():
            hasil += "_" + i.lower()
        else:
            hasil += i

    print(f"snake_case: {hasil}")




main()
