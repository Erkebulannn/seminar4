a =int(input("1-shi san:"))
b =int(input("2-shi san:"))
c =int(input("3-shi san:"))

def my_func(n1,n2,n3):
        if((n1==n2)or(n1==n3)or(n2==n3)):
                print('yes')
        else:
                print('no')
my_func(a,b,c)

