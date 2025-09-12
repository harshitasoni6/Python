# class : 
# blue print for creating object
# or
# self-defined datatype
# Eg.: All datatype are within classes in python 


# class
# -->data/attribute/property
# -->behaviour/method


# Eg. Car is class. then,
# property : color,name,brand,topspeed
# behavior : accelerate(),brake(),start()


# object : instance, created as many times as you want
# everything in python is an object.
# Python gives us 'object literal' for built in type


# Constructor: whenever we create/construct an object of class, 
# there is an inbuilt method (__init__) which is called,
#  which is known as constructor.
# Special method called itself.


# self: self is the reference to the object created of our class
# It is passed whenever we are calling any method.
# Only an object can access or helpful in connecting attribute inside the class.


# attribute : characteristic associated to a type (object)
# method : functions associated to a type (object)


# Access Modifier:
# We can choose to provide access
# to our various by making them public or private.
# Normally, we make all the data members private. 


# What if we actually to access some data member or change their classes?
# Ans=> We make getter & setter for the same use case.
# This binding together of attributes and methods is very useful in achieving security and checks.


# pillars of OOP:

# 1.Encapsulation: The binding of our data memebers/attribute and
# method in single unit is known as Encapsulation.
#Static Property/variables
# For many use cases, we need static properties instead of instance.
# They are defined outside method at the class level.
# Own by class majorly but accessible by object.
# We can have static methods as well decorated with @staticmethod.


# 2.Inheritance: parent => child 
# gives us major benefit of code reusalibity.
# We inherit,
# ->non-private attribute
# ->non-private methods
# ->Constructor (& other magic method)
# We cannot access private attributes or methods of our parent class.
# Parent cannot inherit child properties, only child can inherit child property.
#Types of Inheritance:
# Simple,Heirarichal,Multilevel,Multiple,Hybrid 
# Super keyword:
# Super() keyword is used to access method of parent from our child class.
# cannot be used outside
# can only access methods and not attribute.
# Multiple inheritance:
# not allowed in Java
# ambiguity solved in the order of inheritance.Get properties of both parent.
# MRO(Method resolution order) is followed in resolving ambiguity.

#3.Polymorphism: 
# poly => multiple/many
# morph => shape/form
# In simple words,polymorphism is when a single entity can take multiple form.
# In python, we can achieve polymorphism by below:
# 1.Method Overloading
# 2.Method Overriding
# 3.Operator overloading
# major benefit is that code becomes a lot clean to read and work upon.

# Method Overloading
# Method overloading refers to defining multiple methods within the same class
# that share the same name but have different parameters. 
# Python does not directly support traditional method overloading 
# as found in some other languages (like Java or C++), 
# where methods with the same name but different signatures can coexist. 
# Due to Python's dynamic typing, the interpreter simply replaces earlier 
# definitions of a method with later ones if they share the same name within a class. 

# Method overriding
# Method overriding is an ability of any object-oriented programming language 
# that allows a subclass or child class to provide a specific implementation 
# of a method that is already provided by one of its super-classes or parent classes.
# When a method in a subclass has the same name, the same parameters or signature, 
# and same return type(or sub-type) as a method in its super-class, 
# then the method in the subclass is said to override the method in the super-class.

# Operator Overloading
# Operator Overloading means giving extended meaning beyond their predefined operational meaning. 
# For example operator + is used to add two integers as well as join two strings and merge two lists.
# It is achievable because '+' operator is overloaded by int class and str class.
# You might have noticed that the same built-in operator 
# or function shows different behavior for objects of different classes,
# this is called Operator Overloading. 


# 4.Abstraction
# mean hidden
# fundamental concept of OOPs that involve hiding 
# complex implementation details and 
# showing only essential feature.
# eg. Phone calling: you can take or make call 
# without knowing logic behind it.

# Abstract method and class 
# from abc import ABC, abstractmethod
# we have to ensure 2 things 
# 1.Inherit abc class
# 2.Should have an abstract method
# So abstract classes are useful when we have a 
# group of related object that should share a common feature 
# but should/will have different implementation.
# Help in preparing a blueprint for other classes.