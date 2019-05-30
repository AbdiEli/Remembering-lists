# Simple way of creating lists
courses= ["OM", "BF", "Macroeconomics", "PS", "OB","International Trade"]
print(courses[0])
print(courses[2])

# Changing/updating the first value in the list above from OM to PM/Project Management
courses[0]= "PM"
print ("First value now is " + courses[0])

# Adding new values to the end of the list as always
courses.append ("PM")
print(courses[-1])

# Removing a value from the list
courses.remove("OM")
print(courses[0])

profs[3] = "Wan"
print(profs[3])
# Updating lists
profs=["Nekhai", "Arora", "Thompson", "Thompson"]
profs.remove("Thompson")
print (profs[-1])

# Creative method to remove values from a list
guests = (str("Abdu", "Yahya", "Matt", "Kai"))
counter=0
while counter != "Zeli":
    print(guests)
    not done

# Using index function in lists, it returns the index in a list
guests = ["Abdu", "Yahya", "Matt", "Kai", "Darshan"]
print (guests.index("Kai"))

# Displaying list values

# option 1 for looping through a list
nbrValueInList = len(guests)
# "len" function helps count the number of values in a list and display values based on the count
for steps in range (nbrValueInList):
    print(guests[steps])

# option 2 for looping through a list    
for currentguest in guests:
    print (currentguest)

# Sort the list in alphabetical order
guests.sort()
for guest in guests:
    print(guests)

# Challenge
guests = []
name = "  "
while name.upper() != "DONE":
    name = input("Please enter the name of the guests attending the party!(Enter Done if no more names): ")
    if name.upper() != "DONE":
        guests.append(name)
# if name == "Done":
#guests.remove("DONE")    


guests.sort()
for guest in guests:
    print(guest)
           