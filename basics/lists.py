
friends = ["tom", "lisa", "albert" , "oscar" , "toby"]

# print list
print(friends)

# access index
print(friends[1])

# specify a range
print(friends[2:])
print(friends[1:3])

# modify list
friends[1] = "mike"
print(friends[1])

# combine lists
nums = [1, 2, 3, 4, 5, 5]
new_friends = friends.copy()
new_friends.extend(nums)
print(new_friends)

# add to end of a list
friends.append("tommy")
print(friends)

# add to specific index
friends.insert(1, "johnny")
print(friends)

# remove element
friends.remove("tom")
print(friends)

# remove last elemejnt
friends.pop()
print(friends)

# find index of a value
print(friends.index("oscar"))

# number of times a value appears
friends.append("oscar")
print(friends.count("oscar"))
print(friends.count("alex"))

# sorting
friends.sort()
print(friends)

# reverse list
friends.reverse()
print(friends)

# copy a list
friends2 = friends.copy()