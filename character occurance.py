string = input("Please enter a word: ")
char = input("Please enter a character: ")
count = 0
i = 0
while(i < len(string)):
    if (string[i] == char):
        count += 1
    i = i + 1
print("The total number of times " , char, " has occurred is: ", count)