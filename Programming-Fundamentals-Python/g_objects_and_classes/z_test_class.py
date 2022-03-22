from g_objects_and_classes import z_class_test

class Person(GreetingByName):
    pass

ivan = Person("Ivan", "Ivanov")
print(ivan.say_hello())