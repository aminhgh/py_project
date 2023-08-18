# dict_comprehension

words = ["data","amin","python","instagram","git"]
values = [10,23,45,66,110]
#1
#make dict 
dict_a = {i:j for i,j in zip(words,values) }
print(dict_a)
#2
#filter with no filter :) 
dict_b = {i:j for i,j in zip(words,values) if j>25 }
print(dict_b)
#3 method on 
dict_c = {i.upper():j*2 for i,j in zip(words,values) }
print(dict_c)