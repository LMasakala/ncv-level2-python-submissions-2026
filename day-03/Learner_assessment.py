from datetime import date
name = input("Please enter your name: ")
year_born = input("Please enter a year you were born: ")

today = date.today()
age = today.year - int(year_born)
if age >= 50:
    print ("Congrats you qualify for seniors discount")
else:
    print ("Sorry try again next year")

print(name, "is: ", age )