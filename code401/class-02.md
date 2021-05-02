# JQuery

jQuery is a fast, lightweight, and feature-rich JavaScript library that is based on its motto "write less, do more". jQuery is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, and animation much simpler.

All the power of jQuery is accessed via JavaScript, in order to use jQuery, the first thing you need to do is include the jQuery script in your page just like other scripts. You can download a copy of the jQuery library from www.jquery.com, or, as an alternative, you can include it from a CDN (Content Delivery Network), like Google or Microsoft.

**jQuery Benefits**

- You can easily select elements to perform manipulation.
You can easily create effect like show or hide elements, sliding transition, and so on.
- You can easily create complex CSS animation with fewer lines of code.
- You can easily manipulate DOM elements and their attributes.
- You can easily implement Ajax to enable asynchronous data exchange between client and server.
- You can easily traverse all around the DOM tree to locate any element.
- You can easily perform multiple actions on an element with a single line of code.
- You can easily get or set dimensions of the HTML elements.
The list does not end here, there are many other interesting things that you can do with jQuery.

#### If you're not familiar with jQuery, you might be wondering what makes jQuery so special. There are several advantages why one should opt for jQuery:

1. SIMPLE SELECTORS:  Selecting the elements through a typical JavaScript approach could be very painful, but the jQuery works like a magic here. The ability of making the DOM elements selection simple and easy is one of the most powerful feature of the jQuery.

2. COMMON TASKS IN LESS CODE: 
jQuery considerably simplifies the common JavaScript tasks. Now you can easily create feature rich and interactive web pages with fewer lines of codes.

3. CROSS-BROWSER COMPATIBILITY: 
    
    jQuery is created with modern browsers in mind and it is compatible with all major modern browsers such as Chrome, Firefox, Safari, Internet Explorer, etc. A jQuery statement typically starts with the dollar sign ($) and ends with a semicolon (;). In jQuery, the dollar sign ($) is just an alias for jQuery.

jQuery Selectors `$` is used to select (query) HTML elements and perform "actions" on them. Basic syntax is:

`$("selector").action()`


The $ accesses jQuery.
The (selector) finds HTML elements.
The action() is then performed on the element(s).
jQuery holds refrence to the selected elements, basically what it is doing is storing the location a piece of information in the browser's memory. The jQuery object is an array-like object because it stores a list of the elements in the same order that they appear in the HTML document (unlike other objects where the order of the properties is not usually preserved).

Caching Jquery Selections in Variables Each time you use a selector in jQuery the DOM is searched for elements that match your query. Doing this too often or repeatedly will decrease performance. If you refer to a specific selector more than once you should add it to the cache by assigning it to a variable:

var nav = $('#navigation');
nav.show();
This would replace:

$('#navigation').show();
LOOPING With jQuery, when a selector returns multiple elements, you can update all of them using the one method. There is no need to use a loop.

Chaining If you want to use more than one jQuery method on the same selection of elements, you can list several methods at a time using dot notation to separate each one, as shown below.

METHODS TO RETRIEVE INFROMATION FROM THE DOM CANNOT BE CHAINED

jQuery's .ready() method checks that the page is ready for your code to work with.

Example: $(document).ready(function() { // your script goes here }); .load() is replaced by .on()

A shortcut for ready event method on document object: $(function() {// your script goes here});

Getting Element Content

.html() is used to retrieve info from a jQuery selection, it retrieves only the HTML inside the FIRST element in the matched set, along with any descendants.

.text() is used to retreive the text from a jQuery selection, it returns the content from every element in the jQuery selection, along with the text from any descendants.

Updating Elements Here are four methods that update the content of all elements in a jQuery selection:

1. .html()

Get the HTML contents of the first element in the set of matched elements or set the HTML contents of every matched element.

2. .text()

Get the combined text contents of each element in the set of matched elements, including their descendants, or set the text contents of the matched elements.

3. .replaceWith()

Replace each element in the set of matched elements with the provided new content and return the set of elements that was removed.

4. .remove()

Remove the set of matched elements from the DOM.

Inserting Elements *Inserting new elements involves two steps: *Create the new elements in a jQuery object *Create new jQuery objects to hold text and markup *Use a method to insert the content into the page

Once you have a variable holding the new content, you can use the following methods to add the content to the DOM tree:

5. .before()

This method inserts content before the selected element(s) .

6. .prepend()

This method inserts content inside the selected element(s), after the opening tag

7. .after()

This method inserts content after the selected element(s).

.append()

This method inserts content inside the selected element(s), before the closing tag

Getting and Setting CSS properties The .css() method lets you retrieve and set the values of CSS properties.

To GET the value of a CSS property, you indicate which property you want to retrieve in parentheses. If the matched set contains more than one element, it will return the value from the first element. For example:

var backgroundColor = $('li').css('background-color');

To SET the values of a CSS property, you specify the property name as the first argument in the parentheses, then a comma, followed by its value as the second argument. This will update every element in the matched set. You can also specify multiple properties in the same method using object literal notation. For example:

`$('li').css('background-color', '#272727');`

***To set a value in pixels, do:***

`$('li').css('padding-left', '+=20');`

Working with each element in a selection: .each() allows you to perform one or more statements on each of the items in the selection of elements that is returned by a selector, like a loop. this or $(this) uses the this keyword to create a new jQuery selection containing the current element. It allows you to use jQuery methods on the current element.

Event Methods JQuery provides an efficient way to handle events. Events occur when the user performs an action, such as clicking an element, moving the mouse, or submitting a form. When an event occurs on a target element, a handler function is executed.