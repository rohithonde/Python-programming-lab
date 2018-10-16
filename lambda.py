y=lambda x:x*x*x
print(y(5)) 

z=lambda a,b:a*b
print(z(5,6))

x=lambda a,b,c:a+b+c
print(x(1,2,3))

print("filter using lambda") 

my_list=[1,2,3,4,5]
m=filter(lambda i:i%2==0,my_list)  #syntax
new_list=list(m) 
print(new_list) 
