# Declare a tuple with Groucho. Print type and the tuple.

one_marx = ("Groucho",)
print(one_marx)
print(type(one_marx))

# Declare a tuple "Groucho", "Chico", "Harpo". Assign the tuple to variables a, b and c
marx_tuple = ("Groucho", "Chico", "Harpo")
a,b,c = marx_tuple
print(f"a = {a} , b = {b} and c = {c}")

print(marx_tuple)


# Declare two variables password = "swordfish" and icecream as "tuttifruti"
# Interchange them.

password = "swordfish"
icecream = "tuttifruti"

print(f"Before swap : password = {password} and Icecream = {icecream} ")
icecream,password = password,icecream

print(f"Icecream = {icecream} and Password = {password}")

# 9:20 .
marx_list = ["Groucho", "Chico", "Harpo"]
print(tuple(marx_list))


# Combine using + Remember the first thing should end with , if it is ony one item.
# Combine Groucho as first item with Chido and Harpo.
my_combination = ('Groucho',) +( 'Chico', 'Harpo')
print(my_combination)

# new_combination
new_combination = ("Groucho", ) + ("Chico", "Harpo")
print(new_combination)


# Duplcate items with * .
# Triplicate yada .
triplate = ("yada") * 3
print(triplate)

# Looping u can use for in. Loop fresh out of ideas.
words = ("fresh", "out", "of","ideas")
for word in words:
    print(word)

# Adding to a tuple. Add tuples Fee, Fie , Foe with Flop.  You can
# do it with + sign.

t1 = ("Fee", "Fie", "Foe")
print(id(t1))
t2 = ("Flop",)
t1 += t2
print( id(t1) )

# Convert String cat to list of characters.
print(list("cat"))

# Convert 'a/b//c/d///e' . Split the String with // sign and
splitime = "a/b//c/d///e"
print(splitime.split("//"))

# Negative Indexes count from backward. From -ve sign.
# Declare marxes as list of 'Groucho', 'Chico', 'Harpo' and print all of them using -ve indexes.
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[-1])


# You can use slice expresson using [0:2] From the list "Groucho", "Chico", "Harpo". Get first two using slice opeator.
marxes = ["Groucho", "Chico", "Harpo"]
print(marxes[0:2])

# Print from start to end in increments of 2. USe the same list.
print(marxes[::2])

# To reverse the list. You can use :: and -1 . This will not change the original list. Increments can be -ve.
print(marxes[::-1])

# Functions on list. revers, append  and insert. 10:19
# reverse will modify the list permenantly .
# append can add a member to the end of the list.
# insert will add the position.
# For the list "Groucho", "Chico", "Harpo" add Zeppo to the end.
# For the list  "Groucho", "Chico", "Harpo"  add Gummo betwen Harpo and Zeppo.

marxes = ["Groucho", "Chico", "Harpo"]
marxes.append("Zeppo")
print(marxes)

# For the list marxes = ["Groucho", "Chico", "Harpo"]
# Add Gummo between Chico and Harpo.
marxes = ["Groucho", "Chico", "Harpo"]
marxes.insert(2,"Gummo")
print(marxes)

# Time at 10:10
# Duplicate the list "blah" , three times.
print(["blah"] * 3)

# Combine the lists using extend, + or +=
# Add the lists 'Groucho', 'Chico', 'Harpo', 'Zeppo' and 'Gummo', 'Karl' using all hte
# Three operators.

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo' ]
others = ['Gummo', 'Karl']

marxes.extend(others)
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo' ]
others = ['Gummo', 'Karl']
marxes += others
print(marxes)

# Changing items with slice. You can use slice operator to do assignment.
# Delcare the array 1,2,3,4 . Between 1 to 3 assign 8 , 9
numbers = [1,2,3,4]
numbers[1:3] = [8,9]
print(numbers)

# Right side of the slice, can have more numbers.
# Betwen 1 to 3 slice, assign 7,8,9
numbres = [1,2,3,4]
numbers[1:3] = [7,8,9]
print(numbers)

# Offset will fit in. For numebrs 1,2,3,4 assign wat? between 1 to 3.
numbers = [1,2,3,4]
numbers[1:3] = 'wat?'
print(numbers)


# Delete an item with del on the main block.
# 'Groucho', 'Chico', 'Harpo', 'Gummo' .. From this array delete Chico
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo']
del(marxes[1])
print(marxes)
# Delate an item with remove()
#  Declare an array 'Groucho', 'Chico', 'Harpo'. called marxes.
# Remove Groucho
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.remove("Groucho")
print(marxes)

# pop() and pop(index) will remove the element and also collect the element.
# Declare the array marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
# Use pop to remove with an index.
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
# Remove Chico and print
popped = marxes.pop(1)
print(marxes)
print(f"Popped = {popped}")


# Find Item's Offset by value with index()
# For the array marxes ['Groucho', 'Chico', 'Harpo', 'Zeppo']
# Find the index of Chico . USe index method.
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index("Chico"))

# Test for a value with in operator. Check if Groucho is in marxes.
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print("Groucho" in marxes)

# Count occurences of a Value with count() function.
# For the array 'cheeseburger', 'cheeseburger', 'cheeseburger' count the
# Number of occurences in that array. USe count function.

snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count("cheeseburger"))

# Use join to join all the strings in the list.
# For the list 'Harry', 'Hermione', 'Ron', use ' * ' to join the array and make it as string.
friends = [ 'Harry', 'Hermione', 'Ron'  ]
print(' * '.join(friends))

# Array can be sorted with sort and sorted functions. sort function
# sorts with sort in place sort and reverse=True will sort it in revres.
# sorted will return new array.

numbers = [2, 1, 4.0, 3]
print(sorted(numbers))
print(numbers)

# Sort the numbers in revers order. using sort
numbers.sort(reverse=True)
print(numbers)

# For the array 'Groucho', 'Chico', 'Harpo',  print it's length.
marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes))

#  Copying the values of the array. 11:35
# Use copy() method.
# use list slice operation.
# For the array 1,2,3 use copy , list or slice operator to make a copy

a =[1,2,3]
b = a.copy()
print(b)
c = list(a)
print(c)
d = a[:]
print(d)

# Copy vs deep copy. copy will create another array, but changing one will change other.
# Deep copy will

a = [1,2,[8,9]]
b = a.copy()
print(b)
c = list(a)
print(c)
d = a[:]
print(d)

a[2][1] = 10
# Both changed.
print(a)
print(b)

# For deep copy use copy.deepcopy method. For the array [1,2,[8,9]],
# make a deep copy change 9 to 10 and print both a and b.
a = [1,2,[8,9]]
print(a)
import  copy
b = copy.deepcopy(a)
# print(b)
a[2][1] = 10
print(a)
print(b)


# for in to iterate over the list.
# To break out of the loop use break. using if statemetn will also continue to break.
# Declare cheeses as 'brie', 'gjetost', 'havarti' .
 # lopp over and print the cheese. if cheese start with g, Print
 # I won't eat anything that starts with 'g' and break out of the for loop.

cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith("g"):
        print("I won't eat anything that starts with 'g'")
        break
    else:
        print(cheese)


# You can also use for / else. If the beaak statement doesn't get executed,
# else block will be executed.
# Declare cheeses as an empty array.
# Looping print This shop haas some lovely {cheese}
# and the break. If break is not executed, print This is not much of the cheese shop, is it?

cheeses =[]
for cheese in cheeses:
    print(f"This is lovely {cheese}")
    break
else:
    print("This is not much of the cheese shop, is it?")

# zip function is applied to all the lists.
# For each corresponding element in the list, a tuple is created.
# Declare days as follows days = ["Monday", "Tuesday", "Wednesday", "Thursday"]
# fruits as 'banana', 'orange', 'peach'
# drinks as 'coffee', 'tea', 'beer' and desserts as 'tiramisu', 'ice cream', 'pie', 'pudding'
# zip is performed on the shortest list.
# Should print the result in the following format . Monday : drink coffee - eat banana - enjoy tiramisu

days =["Monday", "Tuesday", "Wednesday", "Thursday"]
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(f"{day} : drink {drink} - eat {dessert} - enjoy {dessert}")


# List Compreshension. Will generated the New list.
# general rule is [expression for item  in iterable if condition]
# [number for number in range(1,6)]

# Question for number in 1, 6
double_numbers = [ number * 2 for number in range(1,6)]
print(double_numbers)

# For range of 1,100 print all even numbers. Use list comprehensions.
even_numbers = [ i for i in range(1,100) if i % 2 == 0 ]
print(even_numbers)

# More complicated list comprehensions.
# for range of 1  to 4 and for columns in 1 to 3.
# Get all the cells, Use two loops within to genrate output like this.
#(1, 1) , (1, 2), (2, 1), (2,2), (3,1), (3,2)

rows = range(1,4)
cols = range(1,3)
cells = [
    (row,col) for row in rows for col in cols
]
for cell in cells:
    print(cell)

# Lists can be delcared within the lists
# Example. ['hummingbird', 'finch'], ['dodo', 'passenger pigeon', 'Norwegian Blue'], 'macaw',
# [3, 'French hens', 2, 'turtledoves']
# declare a list as ['hummingbird', 'finch'],
#     ['dodo', 'passenger pigeon', 'Norwegian Blue'],
#     "macaw",
#     [3, 'French hens', 2, 'turtledoves']
#
all_lists = [
    ['hummingbird', 'finch'],
    ['dodo', 'passenger pigeon', 'Norwegian Blue'],
    "macaw",
    [3, 'French hens', 2, 'turtledoves']
]
print(all_lists[3][1])










