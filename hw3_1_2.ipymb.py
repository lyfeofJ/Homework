marks = {'Andy':88,'Amy':66,'James':90,'Jules':55,'Arthur':77}
def avg(grades):
    final = 0
    for grade in marks.values():
        final += grade
    return final/len(marks)
print(avg(marks.values))