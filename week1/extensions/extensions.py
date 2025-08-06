def ext():
    x = input("File name: ")
    user = x.strip().lower()
    if ".gif" in user:
        print  ("image/gif")
    elif ".jpeg" in user or ".jpg" in user:
        print  ("image/jpeg")
    elif ".png" in user:
        print  ("image/png")
    elif ".pdf" in user:
        print  ("application/pdf")
    elif ".txt" in user:
        print  ("text/plain")
    elif ".zip" in user:
        print  ("application/zip")
    else:
        print ("application/octet-stream")

ext()
