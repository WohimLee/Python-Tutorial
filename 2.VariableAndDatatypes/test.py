
class Module:
    pass

class Linear(Module):
    pass

module = Module()
linear = Linear()

print(isinstance(module, Module))
print("module type: ", type(module))
print(isinstance(linear, Module))
print("linear type: ", type(linear))