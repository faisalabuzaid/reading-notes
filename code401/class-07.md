
## Understanding Scope
In programming, the scope of a name defines the area of a program in which you can unambiguously access that name, such as variables, functions, objects, and so on. A name will only be visible to and accessible by the code in its scope. Several programming languages take advantage of scope for avoiding name collisions and unpredictable behaviors. Most commonly, you’ll distinguish two general scopes:

1. Global scope: The names that you define in this scope are available to all your code. 
2. Local scope: The names that you define in this scope are only available or visible to the code within the scope.

## Global
When you try to assign a value to a global name inside a function, you create a new local name in the function scope. you can define a list of names that are going to be treated as global names by use a global statement.

The statement consists of the global keyword followed by one or more names separated by commas. You can also use multiple global statements with a name (or a list of names). All the names that you list in a global statement will be mapped to the global or module scope in which you define them.

The global statement can be used to modify global names from almost any place in your code, as you’ll see in The global Statement. Modifying global names is generally considered bad programming practice because it can lead to code that is:

**Difficult to debug:** Almost any statement in the program can change the value of a global name.
**Hard to understand:** You need to be aware of all the statements that access and modify global names.
**Impossible to reuse:** The code is dependent on global names that are specific to a concrete program.


## The nonlocal 

With a nonlocal statement, you can define a list of names that are going to be treated as nonlocal. nonlocal names can be accessed from inner functions, but not assigned or updated.

the nonlocal statment consists of the nonlocal keyword followed by one or more names separated by commas. These names will refer to the same names in the enclosing Python scope.