import sys

def reading():
    with open('file.py') as file:
        lines = file.read()
    return lines

def encode(string):
    result= ""
    file = open("file.py", "w")

    for char in string:
        if(char.isupper()):
            result+= char.lower()
        elif(char.islower()):
            result += char.upper()
        elif(char == " "):
            result += " "
    file.write(result)
    print(f"- Enkodingis shedegi: {result}")

def decode(string):
    result= ""
    file = open("file.py", "w")
    
    for char in string:
        if(char.islower()):
            result += char.upper()
        elif(char.isupper()):
            result += char.lower()
        elif(char == " "):
            result += " "
    file.write(result)
    print(f"- Dekodingis shedegi: {result}")


arguments = len(sys.argv)

def main():
    if(arguments == 1):
        print("aklia moqmedebis argumenti")
    elif(arguments == 2):
        print("aklia failis argumenti")
    elif(arguments == 3):
        action = sys.argv[1]
        file = sys.argv[2]
        if(file == "file.py"):
            if(action == "-E"):
                print("- Enkodingis operacia warmatebit shesrulda")
                encode(reading())
            elif(action == "-D"):
                print("- Dekodingis operacia warmatebit shesrulda")
                decode(reading())
            else:
                print("shemoitanet argumenti [-E] an [-D]")
        else:
            print("miutitet faili argumentshi")
    else:
        print("sheamowmet argumentebi")


main()