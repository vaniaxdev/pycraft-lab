#store lots data

# data structures
# list, set, tuple, dictionary

# LISTS
people = ["Jack", "Precious", "Licky", "Vania"]
scores = [87, 91, 45, 70, 90, 89, 80, 66, 98]
print(people[0]) # 0 first value
print(scores[0])
print(people[-1]) # -1 is the last value

people.append("Francis") # .append used to add a new text
print(people)
scores.append(68)
print(scores)

people.sort() #Sorts alphabetically
scores.sort() #Sorts from low to high
print(people)
print(scores)

print(scores[0], scores[-1]) #Works after initially sorti
print(sum(scores) / len(scores)) #Calculates average

scores.sort()
#slicing
print(scores)
print(scores[-2:])
print(scores[:3])


print(scores[3:5])


# set-remove duplicates
numbers = {87, 89, 67, 87, 54}
print(numbers)


# Tuple -- immutable data
days = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
print(days)


# Dictionary key + value
person = {"name": "Francis", "city": "Nakuru", "age":20}
print(person["name"])
print(person["city"])

# data structures + algorithms
print(sum(numbers))

watu = [{"name": "Sam", "age":22},
        {"name": "Van", "age":20},
        {"name": "Sly", "age":18}]

print (watu[1]["name"])


# loops

