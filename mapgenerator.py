from random import randint
def generate():
    def writing(filename,x,y,e):
        for string in range(y-1):
            for symbol in range(x-1):
                filename.write(str(randint(0,e)))
                filename.write(" ")
            filename.write(str(randint(0,e)))               
            filename.write("\n")
        for symbol in range(x-1):
            filename.write(str(randint(0,e)))
            filename.write(" ")
        filename.write(str(randint(0,e)))

    with open("land.txt", "w") as file:
        writing(file,16,16,0)