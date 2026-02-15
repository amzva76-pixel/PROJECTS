print("Enter marks obtained in four subjects")

math = int(input("maths:"))
english = int(input("english:"))
science = int(input("science:"))
urdu = int(input("urdu:"))

sum = math+english+science+urdu
print("Sum of math,english,science,urdu")
print(sum)
perc = (sum/400)*100

print("end percentage Mark =")
print(perc)