import array as arr
a=arr.array("i",[1,3,5,3,7,9,3])
print("this is the orignal array:"+str(a))

print("number of occurences of the number 3 in the array is:"+str(a.count(3)))
a.reverse()
print(str(a))