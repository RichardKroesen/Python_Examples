try:
    file = open("myfile.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    try:
        file.close()
    except NameError:
        pass
