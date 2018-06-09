
def num_encrypt(num):
	num_list = list(str(num))
	for i in [0,1,2,3]:
		num_list.append(str((int(num_list[0])+5)%10))
		num_list.pop(0)
	num_list.reverse()
	result_str = ''.join(num_list)
	return int(result_str)


print("input a integer contains 4 digits")
num = input()
result = num_encrypt(num)
print(result)
