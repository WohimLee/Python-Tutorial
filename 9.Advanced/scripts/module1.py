

print("module1.py is imported.")

class MyClass:
    def printInfo():
        print('Call MyClass.printInfo() in module.py')

def func():
    print("Call func in module.py")

if __name__ == '__main__':
    print("Execute the code: python {}.py".format(__name__))