mark = input("Enter mark: ")

if mark.isdigit():
    mark = int(mark)
    if mark >=0 and mark <= 100:
        if mark >= 80:
            print ("Outstanding")
        elif mark >=70 and mark <80 :
            print ("Highly Competent")
        elif mark >60 and mark <70 :
            print ("Highly Competent")
        elif mark >50 and mark <60 :
            print ("Competent")
        elif mark >40 and mark <50 :
            print ("Not yet comptent")
        elif mark >0 and mark <40 :
            print ("Not achieved")
else:
    print ("Please enter a valid mark")
        