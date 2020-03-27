import builtins
print(dir(builtins))
def outer():
    x='outer x'
    def inner():
        x='inner x'
        print(x)
    inner()
    print(x)
outer()