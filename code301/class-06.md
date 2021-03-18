# Class 6 Reading
# Object Literals

The object literal is one of the most popular patterns for creating objects in JavaScript because of its simplicity. ES6 makes the object literal more succinct and powerful by extending the syntax in some ways.

It is very common to create an object using an object literal when you want to transfer a series of structured, related data items in some manner, for example sending a request to the server to be put into a database. Sending a single object is much more efficient than sending several items individually, and it is easier to work with than an array, when you want to identify individual items by name.

The simplest way to create an object literal is to assign an empty object to a variable. For example: var foo = {}; That is it. In that one line, you have created an object literal. Now, that object is empty.

 # Document object model


![image](https://www.conceptdraw.com/solution-park/resource/images/solutions/dom-tree/SOFTWARE-DEVELOPMENT-DOM-Tree-Dom-Tree-Mindmap.png)


## The Document Object Model (DOM) ##
is a cross-platform and language-independent interface that treats an XML or HTML document as a tree structure wherein each node is an object representing a part of the document. The DOM represents a document with a logical tree. Each branch of the tree ends in a node, and each node contains objects.

- A Web page is a document. This document can be either displayed in the browser window or as the HTML source. But it is the same document in both cases. Also it represents that same document so it can be manipulated. The DOM is an object-oriented representation of the web page, which can be modified with a scripting language such as JavaScript.

- The DOM was designed to be independent of any particular programming language, making the structural representation of the document available from a single,

-This guide is about the objects and the actual things you can use to manipulate the DOM hierarchy. There are many points where understanding how these work can be confusing. For example, the object representing the HTML form element gets its name property from the HTMLFormElement interface but its className property from the HTMLElement interface. In both cases, the property you want is in that form object.

-But the relationship between objects and the interfaces that they implement in the DOM can be confusing, and so this section attempts to say a little something about the actual interfaces in the DOM specification and how they are made available.
 