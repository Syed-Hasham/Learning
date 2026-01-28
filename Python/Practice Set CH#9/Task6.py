with open("mine.log") as f:
    c= f.read()
    if("python" in c):
        print("FOUND")
    else:
        print("NOT FOUND")