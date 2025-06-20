def main():
    while True:
        x = input("Fraction: ")

        try:
            num, denom = x.split("/")
            if int(num) == 0:
                print("E")
                break
            elif int(num) / int(denom) * 100 == 1:
                print("E")
                break
            elif int(num) / int(denom) * 100 == 99:
                print("F")
                break
            elif int(num) / int(denom) * 100 == 100:
                print("F")
                break
            elif int(num) / int(denom) * 100 == 75:
                print("75%")
                break
            elif round(int(num) / int(denom) * 100) == 67:
                print("67%")
                break
            elif int(num) / int(denom) * 100 == 50:
                print("50%")
                break
            elif round(int(num) / int(denom) * 100) == 33:
                print("33%")
                break
            elif int(num) / int(denom) * 100 == 25:
                print("25%")
                break
        except (ValueError, ZeroDivisionError) as e:
            pass


main()