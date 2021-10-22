try:
        a =int(input("1-shi san:"))
        b =int(input("2-shi san:"))
        c =int(input("3-shi san:"))
except:
        print("Error")
        exit()

def my_func(n1,n2,n3):
        if((a==b)or(a==c)or(b==c)):
                print('yes')
        else:
                print('no')
my_func(a,b,c)

