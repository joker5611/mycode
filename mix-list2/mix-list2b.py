#!/usr/bin/env python3

# this is a list we want to augment
proto = ['ssh', 'http', 'https']

# this is a list we want to augment a bit differently
protoa = ['ssh', 'http', 'https']

# print the first list we created
print(proto)

# change our first list
proto.append('dns') # this line will add 'dns' to the end of our list

# perform the same change operation on our second list
protoa.append('dns') # this line will add 'dns' to the end of our list

# display on the screen our first list
print(proto)

# display on the screen our second list (they both look the same)
print(protoa)

# create a new list of information
proto2 = [ 22, 80, 443, 53 ] # a list of common ports

# perform DIFFERENT change operations on our two lists
# first we perform the EXTEND method
# list.extend()
proto.extend(proto2) # pass proto2 as an argument to the extend method -- then print result
# display how proto was augmented by extend
print("\nThis is what list.extend() did to our list.\nExtend iterated through proto2, and added each element to the end of our list (fancy way of saying it combined the lists).")
print (proto)

# no we will perform the APPEND method
# list.append()
protoa.append(proto2) # pass proto2 as an argument to the append method -- then print result
print("\nThis is what list.append() did to our list.\nAppend opens up a SINGLE slot at the end of the list.")
print (protoa)

# print the value of 22 from proto
# this is just index 4 we want to display
print(proto[4])

# print the value of 22 from protoa
# this is select index 4 (which is a list) then select item 0 from that list
print(protoa[4][0])

