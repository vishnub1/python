print("hello");

# identity operators
a=3
b=3.4
print(a);
print(b);
print(a is b); # False
print(a is not b) #True


c=5
d=5
print(c is d) #True
print(c is not d) #alse


x=10
print(type(x) is int); #True

x1='hello';
y1='hello';
print(x1 is y1); #True

print('---------------')
x2=[1,2,3,4];
y2=[1,2,3,4];
print(x2 is y2); #False

print('---------------')
x3=(1,2,3,4);
y3=(1,2,3,4);
print(x3 is y3); #True

