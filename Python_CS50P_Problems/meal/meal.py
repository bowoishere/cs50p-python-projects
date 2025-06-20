def main():
    meal = input("What time is it? ").strip().lower()
    time = convert(meal)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")


def convert(t):
    t = t.strip()
    if "a.m." in t or "p.m." in t:
        time_part, period = t.split(" ")
        hour, minute = map(int, time_part.split(":"))

        # Konversi ke format 24 jam
        if period == "p.m." and hour != 12:
            hour += 12
        elif period == "a.m." and hour == 12:
            hour = 0
    else:
        hour, minute = map(int, t.split(":"))

    return hour + minute / 60.0


if __name__ == "__main__":
    main()
