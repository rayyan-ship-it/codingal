import array as arr
array_num=arr.array("i",[1,3,5,3,7,9])
print("orginal array:"+str(array_num))
print("the number of occurences of the number 3 is"+str(array_num.count(3)))
array_num.reverse()
print("reverse the order of items")
print(str(array_num))