#coding:utf-8
import numpy 

f = open('System.txt','r')

for row in f:
    tmp  = row.strip('{}\n') ## system
    
system_list = tmp.split(',')

f.close()

f = open('Input.txt','r')

for row in f:
    tmp  = row.strip('{}\n') ## input
    
input_list = tmp.split(',')
f.close()

print(system_list)
print(input_list)







