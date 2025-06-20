def main():

    data = {
        ".gif" : "image/gif",
        ".jpg" : "image/jpeg",
        ".jpeg" : "image/jpeg",
        ".png" : "image/png",
        ".pdf" : "application/pdf",
        ".txt" : "text/plain",
        ".zip" : "application/zip"
    }

    call = input("File name: ").lower().strip()
    if "." in call:
        trim = "." + call.rsplit(".", 1)[-1]
    else:
        trim =""


    if trim in data:
        print(data[trim])
    else:
        print("application/octet-stream")


main()
