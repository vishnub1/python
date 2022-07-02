
    # Data Types in Python
#========================
# int     a=20
# Float   b=20.33
# String
# List
# Tuple
# Dictionary
# Boolean
# Set
#============================

# String  c='vishnu'  or c="vishnu"
z="Hello Python";
print(z[0]);   # H
print(z[1]);   # e
print(z[-1]);  # n
print(z[-4]);  # t

z1=z[1:4];
print(z1); # ell

z2= z[6:]
print(z2);  # python

z3= z[:5]
print(z3);  # Hello

z4 = z*3;
print(z4);  #Hello PythonHello PythonHello Python


x="Python Programming is easy";
l= x.split();
print(l);   # ['Python', 'Programming', 'is', 'easy']

x1= 'Python, Programming, is, easy';
l1= x1.split(',');
print(l1);   # ['Python', ' Programming', ' is', ' easy']

x2= 'Python, Programming, is, easy';
l2= x2.split('n');
print(l2);   # ['Pytho', ', Programmi', 'g, is, easy']


p=['Python', 'is','easy'];
print(type(p));  # <class 'list'>

p1=' '.join(p);
print(p1);  # Python is easy

p2='.'.join(p);
print(p2);  # Python.is.easy

ss='VishnuKant BiraDar';
print(ss.upper());      # VISHNUKANT BIRADAR
print(ss.lower());      # vishnukant biradar
print(ss.capitalize()); # Vishnukant biradar
print(ss.title());      # Vishnukant Biradar
print(ss.find('h'));    # 3
print(ss.rfind('n'));   # 8
print(ss.rfind('B'));   # 11
print(ss.rindex('K'));  # 6
print(ss.split('i'));   #['V', 'shnuKant B', 'raDar']
