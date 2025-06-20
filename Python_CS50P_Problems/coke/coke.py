
def main():
    price = 50
    while price > 0:
        print(f"Amount Due: {price}")
        
        coin = int(input("Insert Coin: "))

        if coin in [25, 10, 5] :
            price -= coin
        else:
            print("Receive US cents only!")
            continue

    print(f"Change Owed: {abs(price)}")


main()
