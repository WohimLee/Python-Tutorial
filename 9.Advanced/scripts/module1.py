

print("module1.py is imported.")

class MyClass:
    def printInfo(self):
        print('Call MyClass.printInfo() in module1.py')

def func():
    print("Call func in module1.py")

if __name__ == '__main__':
    print("Execute the code: python {}.py".format(__name__))