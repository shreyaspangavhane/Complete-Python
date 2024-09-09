# import is used to import/used a module
## install module using  CMD =>>   pip install module_name
## to uninstall that module use CMD ==>> pip uninstall module_name 



import math as mt

g=dir(mt)       ## print all the function inside to that math module
print(g)

a=mt.sqrt(16)             ## sqrt ->tell us the square root
print(a)

print(mt.pow(5,3))       # return 5^3 =>> 125




# calender module
import calendar as cd

print(dir(cd))


# print the jan month in 2022 yr 

print(cd.month(2022,1))


print(cd.isleap(2022))    # check the leap yr or not







## import pyroids     -->>    pip install pyroids

import pyroids as py

print(dir(py))

py.launch()            ## launch the game

