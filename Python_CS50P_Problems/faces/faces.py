def convert_emoji(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

text = input()

print(convert_emoji(text))
