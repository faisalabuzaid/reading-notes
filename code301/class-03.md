# MUSTACHE and FLEXBOX

## Javascript Templating Language and Engine— Mustache.js with Node and Express

**Mustache**

Mustache can be used for HTML, config files, source code - anything. It works by expanding tags in a template using values provided in a hash or object.

We call it "logic-less" because there are no if statements, else clauses, or for loops. Instead there are only tags. Some tags are replaced with a value, some nothing, and others a series of values. This document explains the different types of Mustache tags.

Tags are indicated by the double mustaches. {{person}} is a tag, as is {{#person}}. In both examples, we'd refer to person as the key or tag key.

If you intend you use mustache with Node and Express, you can use mustache-express. Mustache Express lets you use Mustache and Express together easily.

mustache.js is an implementation of the mustache template system in JavaScript. It is often considered the base for JavaScript templating.



`Mustache.render(“Hello, {{name}}”, { name: “Sherlynn” });`

`// returns: Hello, Sherlynn`

**Flexbox**

Flexbox is a one-dimensional layout method for laying out items in rows or columns. Items flex to fill additional space and shrink to fit into smaller spaces. In other words, Flexbox Layout aims at providing a more efficient way to lay out, align and distribute space among items in a container, even when their size is unknown and/or dynamic.

***display***

- This defines a flex container; inline or block depending on the given value.
- It enables a flex context for all its direct children.
- .container { display: flex; /* or inline-flex */ }

![image](https://res.cloudinary.com/practicaldev/image/fetch/s---5GvwQgk--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/1zojafmjmuo2p7vmnxcs.jpeg)