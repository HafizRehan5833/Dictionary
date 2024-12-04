#Use a dictionary to count the occurrences of each word in the string "hello world hello python world".


user_input=input("Enter the string: ")

word_list=user_input.split()
#split is use to break bigger strings or a line into several small strings


word_count={}

for word in word_list:
    word_count[word]=word_count.get(word,0)+1



print(word_count)

