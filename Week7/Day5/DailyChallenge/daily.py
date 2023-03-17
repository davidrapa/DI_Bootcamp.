words = input("Add words separate with coma: ")
word_list = words.split(",")
sorted_list = [word for word in word_list]
sorted_list.sort()
result = ','.join(sorted_list) # you can do directly return ','.join(sorted_list)
print(result)
