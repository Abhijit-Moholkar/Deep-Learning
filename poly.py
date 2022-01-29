
# regular expression

# to find a pattren in string
# 're' module is must



"""
import re
s = 'bdvdf2v1b1f2BFRGHF12GFN2FSMHM12G12FSM2M1H12'
m  = re.finditer('12',s)

for i in m :

    #print(i)
   
    print(i.start())


"""









# predefined chracter classes

# for only digit d
'''
import re
s = 'bad5 gejgfehj 5dfebg uehfjue5  afdvj bvaa  afbv  9 fdvn6 d 3d 3'

m=re.finditer('\d',s)

for  i in m:
    print(i)


'''












# except number  -  use D
'''
import re

m=re.finditer('\D','bad  ,   !@afdvj bvaa  afbv  9 fdvn6 d 3d 3')
for  i in m:
    print(i)


'''








# FOR ONLY SPACE s
'''
import re

m=re.finditer('\s','bad  afdvj bvaa  afbv  9 fdvn6 d 3d 3')

x = 0
for  i in m:
    x+=1
    print(i)

print(x)
'''









# except space use  S
'''
import re



m=re.finditer('\S','bad  afdvj bvaa  afbv  9 fdvn6 d 3d 3')

for  i in m:
    print(i)
  




'''

# for only no and alphabet

import re

m=re.finditer('[^a-zA-Z]','bad  AHGVGF vdjgh afdvj#$@@@!!!!! bvaa  afbv  9 fdvn6 d 3d 3')
for  i in m:
    print(i)








# for space and special chracter
'''
import re

m=re.finditer('\W','bad  afdvj bvaa&$$@@!@#$%^&*  afbv  9 fdvn6 d 3d 3')
for  i in m:
    print(i)

'''







# for excatly one 'a'

'''
import re

m=re.finditer('a','baaadAaaadSaafdvj bvaa  afbv  9 fdvn6 d 3d 3')
for  i in m:
    print(i)

'''









# for at least one 'a+'
'''
import re

m=re.finditer('a+','baaaaaaaaaaadAaaadSaafdvj bvaa  afbv  99 99 fdvn6 d 3d 3')
for  i in m:
    print(i)
'''





# a*
'''
import re

m=re.finditer('a*','baaadAaaadSaafdvj bvaa  afbv  9 fdvn6 d 3d 3')
for  i in m:
    print(i)

'''



# match()- it checks  ppttern at the beigning of the string

'''
import re

m=re.match('9','abaaadAaaadSaafdvj bvaa  afbv  9 fdvn6 d 3d 3')


if m == None:
    print('not found')
else:
    print('match found')

'''

#full match use full matching
'''
import re
s = input('enter your password:-')

m=re.fullmatch(s,'123456')

if m != None:
    print('match found')
else:
    print('not found')
'''







#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
# mobile no

import re

n=input('eneter mobile no-+91-')

no=re.fullmatch ('[6-9]\d{9}',n)

if no!=None:
    print('valid no')
    
else:
    print('not valid')
'''

 












































































