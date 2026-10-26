marks = []
i =0
mark = int(input("Enter Mark: "))

while mark != -1:
    marks.append(mark)
    mark = int(input("Enter Mark: "))
print(f"Our list has {len(marks)} elements")
    
for x in range(len (marks)):
     print (f"Mark {x+1} is {marks[x]}")
for x in range(len(marks)):
   total = 0
for x in range(len(marks)):
    mark = marks [x]
    total = total + mark
print(f"The sum of all marks = {total}")

avg = total / len(marks)
print(f"The average of all marks = {avg:.2f}")

