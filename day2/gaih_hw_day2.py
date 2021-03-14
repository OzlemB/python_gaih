#create a list and swap the second half of the list with 
#the first half of the list and print this list on the screen

list = [1,2,3,4,5,6,7,8,9,10]
print(list)
a = list[0:5]
b = list[5:10]
reverse_list = []
reverse_list = b + a
print(reverse_list)