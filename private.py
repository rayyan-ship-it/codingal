class myclass:
    __privatevar=27;
def __privMeth(self):
    print("im inside my class")
def hello(self):
    print("private variable value:",myclass.__privatevar)
foo=myclass()
foo.hello()
foo.__privMeth
