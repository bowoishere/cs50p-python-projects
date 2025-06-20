def main():
    while True:
        x = input("Fraction: ")

        try:
            num, denom = x.split("/")
            num = int(num)
            denom = int(denom)

            if denom == 0 or num > denom:
                continue

            percentage = round((num / denom) * 100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        except (ValueError, ZeroDivisionError):
            continue


main()
