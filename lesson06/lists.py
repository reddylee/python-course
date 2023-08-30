users = ['Reddy', 'Peppa', 'George']

data = ['Reddy', 50, True]

emptylist = []

print("Reddy" in emptylist)

print(users[0])
print(users[-2])

print(users.index('George'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Vivian')
print(users)

users += ['Ellen']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

users.extend(data)
print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)

users[1:3] = ['Robert', 'JPJ']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

# users[1:2] = ['reddy']
# users.sort()
# print(users)

# users.sort(key=str.lower)
# print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))
mylist = list([1, "Neil", True])
print(mylist)

# Tuples

mytuple = tuple(('Reddy', 50, True))
anothertuple = (1, 4, 2, 8)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)


print(anothertuple.count(2))
