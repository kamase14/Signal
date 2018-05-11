#coding:utf-8
import numpy as np 

f = open('System.txt','r')

for row in f:
    tmp  = row.strip('{}\n') ## system
    
system_list = np.array(tmp.split(','),dtype=float)

f.close()

f = open('Input.txt','r')

for row in f:
    tmp  = row.strip('{}\n') ## input
    
input_list = np.array(tmp.split(','),dtype=float)
f.close()


print(input_list)
print(system_list)


output = np.convolve(system_list,input_list,mode='full')

print(output)








