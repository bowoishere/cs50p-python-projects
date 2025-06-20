
def main():
    x, y, z = input("Expression: ").split()

    xf = float(x)
    zf = float(z)

    if y == "+":
        result = xf + zf
    elif y == "-":
        result = xf - zf
    elif y == "*":
        result = xf * zf
    elif y == "/":
        result = xf / zf
    else:
        result = ("Make sure your input are correct!")

    print(result)

main()
