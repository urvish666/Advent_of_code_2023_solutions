
# opening the input file in read mode 
my_file = open("input.txt", "r") 
  
# reading the file 
data = my_file.read() 
  
# replacing end splitting the text  
# when newline ('\n') is seen. 
data = data.split("\n") # thus we converted the text file into a list or array


my_file.close() # closing the txt file


digit_1 = []       #making two seperate lists for storing digits
digit_2 = []

while True:                           # loop for getting the first digit
    for indexes in data:   
        for char in indexes:
            if char.isdigit():
                digit_1.append(char)    #storing it in digit_1 list
                break
        
        
    break


while True:                             # loop for getting the second digit
    for indexes in data:
        for char in indexes[::-1]:      # reversing the string
            if char.isdigit():
                
                
                digit_2.append(char)    # storing it in digit_2
                break
        
    break

# print(digit_1)        
# print(digit_2)

final_list = []                                # final list i.e for combining two digit
for i in range(0, len(digit_1)):
    final_list.append(int(digit_1[i] + digit_2[i]))     #combining two lists and converting it into integer datatype

# print(final_list)

final_ans = 0                       # for removing final addition of the numbers
for index in final_list:
    final_ans = final_ans + index 

print(final_ans)    # printing the final