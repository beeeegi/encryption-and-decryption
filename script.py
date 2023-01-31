import sys

def reading():
    with open(sys.argv[2]) as file:
        lines = file.read()
    return lines

def encode(string):
    result= ""
    file = open(sys.argv[2], "w")

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
    file = open(sys.argv[2], "w")
    
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
    match arguments:
        case 1:
            print("aklia moqmedebis argumenti")
        case 2:
            print("aklia failis argumenti")
        case 3:
            action = sys.argv[1]
            file = sys.argv[2]
            if not file:
               return print("miutitet faili argumentshi")
            try:
                open(sys.argv[2])
            except:
                return print("msgavsi faili ar arsebobs")
            match action:
              case "-E":
                print("- Enkodingis operacia warmatebit shesrulda")
                encode(reading())
              case "-D":
                print("- Dekodingis operacia warmatebit shesrulda")
                decode(reading())
              case _:
                print("shemoitanet argumenti [-E] an [-D]")
        case _:
            print("sheamowmet argumentebi")

main()
