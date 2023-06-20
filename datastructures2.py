#TUPLES
cars = ("Mercedes", "Subaru", "Outback", "BMW","Pagani", "Supra", "Challenger")
print(cars[1])
print(cars[5])
print(cars[1:4])
print(cars[2:])
#cars[2] = "Prado" This is not possible
for gari in cars:
    print(gari)



#LISTS
cities = ["London", "Rome","Paris", "Osaka","Tokyo","Nairobi"]
print(cities[1:])
print(cities[1:4])
print(cities[2:])
#In lists you can edit information unlike tuples
cities[0]= "Dubai"
print(cities)
cities.sort(reverse=True)
print(cities)
cities.append("Nakuru")
print(cities)
cities.remove("Rome")
print(cities)
cities.pop(1)
print(cities)
cities.reverse()
print(cities)

 #Using a while loop and without sorting a list print the following
# list in reverse order:
print("--------------------------------------------")
mylist= ["Steve", "Kerubo","Austin","Mike","Gerry","Judy","Michelle"]
mylist.reverse()
mylist.sort()
index = 0
listlength = len(mylist)
while index < listlength:
    print(mylist[index])
    index += 1
#This is how the assignment should have been done





##Start by asking the user how many names he/she has
#numbersOfNames = int(input("How many names do you have?\n"))
#Write a loop to receive the names and append them on the list
#receivedNames = []
#for i in  range(0,numbersOfNames):
    #name = input("Enter name" +str((i+1))+"\n")
    #receivedNames.append(name)

#for i in range(0, numbersOfNames):
   #print(receivedNames[i])





#DICTIONARIES
print("---------------------------")
students = {"ADM1":"Allan", "ADM2":"Hans", "ADM3":"Cecil"}
print(students["ADM2"])
print(students.keys())
print(students.values())
for i in students.keys():
    print(i)

for i in students.values():
    print(i)




#SETS
print("-----------------------------------")
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 1,11,2,5}
print(numbers)