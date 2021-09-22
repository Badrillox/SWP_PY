class FProgram:
    greeting = "Hello"
    cars = ["Audi", "BMW", "Mercedes"]
    nums = [1, 2, 3, 4, 6, 9, 8, 5]
    def shout(text):
        return text.upper() #uppercases the text which is written in - see down below
    print(greeting)
    for x in cars: #looping cars array
        print(x)
    i = 1
    while i < len(nums): #prints nums until i is the number of the len of the array
        print(nums)
        i+=1
    print("Hello Pythonworld")
    print(shout("i am a python programm, loooool"))

    a = 3
    b = 8
    if a < b:
        print(a, b, "A ist kleiner als B")
