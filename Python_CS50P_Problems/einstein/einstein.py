def Energy():
    c = 3 * (10**8)
    print("Welcome to energy calculator".title())
    m = int(input("Enter your m: "))
    E = m * (c**2)
    print(f"The result of your m is:{E}")

Energy()
