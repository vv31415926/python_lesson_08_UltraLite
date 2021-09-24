'''
1. Написать свой генератор последовательностей, свой тернарный оператор
2. Написать свой декоратор
'''

# тернарный оператор
f = lambda x:  'дед'  if x > 50   else  'пацан'
print(  f(30), f(60))

# Генератор последовательностей ***************************************************
lst = [ [x,x**3] for x in range( 10 ) if x%2 == 0 ]
print('списки:',type(lst))
for v in lst:
    print( v[0], v[1])

dic = {  x : x**3  for x in range( 10 ) if x%2 == 0 }
print('словарь:',type(dic))
for k,v in dic.items():
    print( k, v )

set = {  x**3  for x in range( 10 ) if x%2 == 0 }
print('Множество:',type(set))
for v in set:
    print( v )

# Декоратор ********************************************************************
def show(f):
    def wrapper( *args, **kwargs ):
        print(  '*' * (len(args[0])+4) )
        print( '* '+f( *args, **kwargs )+' *' )
        print('*' * (len(args[0])+4) )
    return wrapper

@show
def getName( s ):
    return s

getName('Валерий')
getName('Вика')