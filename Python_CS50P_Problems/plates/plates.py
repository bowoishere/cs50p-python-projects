
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (
        2 <= len(s) <= 6
        and s[:2].isalpha()
        and s.isalnum()
        and num_check(s)
    ):

        return True
    else:
        return False


def num_check(s):
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            return s[i:].isdigit()
    return True



main()
