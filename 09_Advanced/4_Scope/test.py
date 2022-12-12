

def outer():
    num = 10
    def inner():
        nonlocal num
        num = 100
        print(num)
    
    inner()
    print(num)

outer()
