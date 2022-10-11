def student(name):
    marks = {'Andy':88,'Amy':66,'James':90,'Jules':55,'Arthur':77}
    for names, grades in marks.items():
        if names == name:
            print(grades)
student('James')

