# string=str(input('Enter text:'))
# counter1=0
# for i in string:
#     word=string[counter1]
#     if string[counter1]==string[counter1-1]:
#         print(i,counter1)
#     counter1+=1

import re

txt = "boo ann add burr laa bd"
pattern = re.compile(r"(.)\1") 
x = re.findall(pattern, txt)

print(x)
        
            
    # if factor1[0]==factor1[1]:
    #     print(factor1[0],counter+1)
    # if len(factor1)>2:
    #     factor1=''
    #     continue