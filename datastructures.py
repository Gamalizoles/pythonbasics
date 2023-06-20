#TUPLES
cars = ("Mercedes", "Subaru", "Outback", "BMW","1", "40", "1")
print(cars[1])
print(cars[3])
print("----------------")

for gari in cars:
    print(gari)
print("-------------")

slicedcars = cars[1:5]
for j in slicedcars:
    print(j)


#LISTS
cities = ["London", "Rome","Paris", "Osaka","Tokyo"]
for i in cities:
    print(i)
print("------------------")
cities.sort(reverse=True)
for s in cities:
    print(s)
print("----------------------")
slicedcities = cities[2:]
for sc in slicedcities:
    print(sc)


#DICTIONARIES
print("---------------------------")
students = {"ADM1":"Allan", "ADM2":"Hans", "ADM3":"Cecil"}
print(students["ADM2"])
for std in students.values():
    print(std)

for stdkey in students.keys():
    print(stdkey, "-------------", students[stdkey])


#SET
print("-----------------------------------")
numbers = {1,2,3,4,5,6,7,8,1}
for n in numbers:
    print(n)

 #Using a while loop and without sorting a list print the following
# list in reverse order:
print("--------------------------------------------")
mylist= ["Steve", "Kerubo","Austin","Mike","Gerry","Judy","Michelle"]
n = len(mylist) -1
while n>=1:
    print(mylist[n])
    n -=1



