# Domain Modeling
> HTML DOM methods are actions you can perform (on HTML Elements).
>
> HTML DOM properties are values (of HTML Elements) that you can set or change.




# Model epic fails videos
- Imagine you've been tasked to build a program that models the popularity of epic fail videos. 

# Using Math.random() in JavaScript

***In JavaScript, to get a random number between 0 and 1, use the `Math.random()` function.***

``` ruby
console.log(Math.random())
0.5408145050563944
```

***If you want a random number between 1 and 10, multiply the results of `Math.random` by 10, then round up or down.***
*Use `.floor` to round down to a whole number:*
``` ruby
console.log(Math.floor(Math.random() * 10))
```

*Use `.ceil` to round up to a whole number:*
``` ruby
console.log(Math.ceil(Math.random() * 10))
```

*Use `.round` to round to the nearest whole number:*
``` ruby
console.log(Math.round(Math.random() * 10))
```

<hr>

# HTML TABLES

![](https://cdn.educba.com/academy/wp-content/uploads/2019/10/Create-Tables-in-HTML.png)

## Define an HTML Table


- *The <table> tag defines an HTML table.*
- Each table row is defined with a `<tr>` tag. Each table header is defined with a `<th>` tag. Each table data/cell is defined with a `<td>` tag.
- By default, the text in `<th>` elements are bold and centered.
- By default, the text in `<td>` elements are regular and left-aligned.



***Note:*** The `<td>` elements are the data containers of the table. <br>
- They can contain all sorts of HTML elements; text, images, lists, other tables, etc.


***HTML Table - Add a Border***
```
table, th, td {
  border: 1px solid black;
}
```

***HTML Table - Add Cell Padding***

*Cell padding specifies the space between the cell content and its borders.*

*If you do not specify a padding, the table cells will be displayed without padding.*

- *To set the padding, use the CSS padding property:*

*Example*

```
th, td {
  padding: 15px;
}
```


***HTML Table - Add Border Spacing***
*Border spacing specifies the space between the cells.*

- *To set the border spacing for a table, use the CSS border-spacing property:*

*Example*

```
table {
  border-spacing: 5px;
}
```


## WHAT IS AN OBJECT?

- Objects in JavaScript, just as in many other programming languages, can be compared to objects in real life. 
- The concept of objects in JavaScript can be understood with real life, tangible objects.

- In JavaScript, an object is a standalone entity, with properties and type.
- Object properties are basically the same as ordinary JavaScript variables,<br>
- except for the attachment to objects. The properties of an object define the characteristics of the object. 

- You access the properties of an object with a simple dot-notation:

`objectName.propertyName`

**Example**

``` ruby
var person = {
  firstName: "John",
  lastName : "Doe",
  id       : 5566,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};
```

 The `this` Keyword
In a function definition, this refers to the "owner" of the function.
In the example above, `this` is the ***person object*** that "owns" the ***fullName*** function.
In other words,***this.firstName*** means the ***firstName*** property of this object.
 Read more about the `this` keyword at JS this Keyword.

## Using Built-In Methods

- This example uses the `toUpperCase()` method of the String object, to convert a text to uppercase:

``` ruby
var message = "Hello world!";
var x = message.toUpperCase();
```

- The value of x, after execution of the code above will be:

``` ruby
HELLO WORLD!
```

## *Adding a Method to an Object*

***Example:***
``` ruby
person.name = function () {
  return this.firstName + " " + this.lastName;
};
```
<hr> 





















