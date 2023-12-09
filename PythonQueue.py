# Creating a list/queue called names
names = []

# Using a for loop to input 10 names into the list/queue called names
for i in range(10):
    acceptedName = input("Enter name: ")
    names.append(acceptedName)

# Printing the list/queue after adding names
print(names)

# Dequeuing each name using a second for loop and print it
while len(names) > 0:
    print(names.pop(0))

# Printing the list/queue again after all names have been dequeued
print(names)
