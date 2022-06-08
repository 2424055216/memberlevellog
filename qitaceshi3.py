class Exampleclass:
    counter = 0

    def __init__(self, val=1):
        self.__first = val
        Exampleclass.counter += 1


example_1 = Exampleclass()
example_2 = Exampleclass(2)
example_3 = Exampleclass(4)

print(Exampleclass.__dict__)

print(example_1.__dict__, example_1.counter)
print(example_2.__dict__, example_2.counter)
print(example_3.__dict__, example_3.counter)
