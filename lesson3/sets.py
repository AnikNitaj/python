userat = {"1","2","3"}

print("1" in userat)

print(userat)

set1 = {1,2,3}
set2 = {3,4,5}

unionRzults = set1.union(set2)

print("union of set1 and set2 using union method",unionRzults)

unionRzults2 = set1 | set2

print("union of set1 and set2 using | operator",unionRzults2)

intersection_result1 = set1.intersection(set2)
print("intersection of set1 abd set2 using intersection method",interrsecion intersection_result1)

intersection_result2 = set1 & set2
print("intersection result using &", intersection_result2)

difference_result1 = set1.difference(set2)
print(difference_result1)

difference_result2 = set1.difference(set2)
print(difference_result2)

symetric_difference_result1 = set1.symmetric_difference(set2)
print(symetric_difference_result1)

symetric_difference_result2 = set1 ^ set2
print(symetric_difference_result2)

my_set = {1,2,3}

print(my_set)

my_set.add(7)
print(my_set)

my_set.add(2)
print(my_set)

my_set.difference(10)