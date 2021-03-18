# Key Concepts in Positioning Elements

***Building Blocks***
> CSS treats each HTML element as if it is in its own box. This box will either be a block-level box or an inline box.
> Block-level boxes start on a new line and act as the main building blocks of any layout, while inline boxes flow between surrounding text. You can control how much space each box takes up by setting the width of the boxes (and sometimes the height, too). To separate boxes, you can use borders, margins, padding, and background colors.


***Block-level elements***
> start on a new line
*Examples include:*
`<h1>` `<p>` `<ul>` `<li>`


***Inline elements***
> flow in between surrounding text
*Examples include:*
`<img>` `<b>` `<i>`



# Controll ing the Position of Elements:
***The position Property***
The `position` property specifies the type of positioning method used for an element.

There are five different position values:

- static
- relative
- fixed
- absolute
- float

> Elements are then positioned using the top, bottom, left, and right properties. However, these properties will not work unless the `position` property is set first. They also work differently depending on the position value.


> CSS has the following positioning schemes that allow you to control <br>
> the layout of a page: normal flow, relative positioning, and absolute <br>
> positioning. You specify the positioning scheme using the position <br>
> property in CSS. You can also float elements using the float property. <br>


![](https://www.gurukulzone.com/css/images/d.png)


## 1-Normal flow


*HTML elements are positioned static by default.*

*Static positioned elements are not affected by the top, bottom, left, and right properties.*

*An element with` position: static;` is not positioned in any special way; it is always positioned according to the normal flow of the page:*

`This <div> element has position: static;`

*Example*

``` ruby
div.static {
  position: static;
  border: 3px solid #73AD21;
}
```

## 2-Relative Positioning


*An element with position: relative; is positioned relative to its normal position.*

*Setting the top, right, bottom, and left properties of a relatively-positioned element will cause it to be adjusted away from its normal position. Other content will not be adjusted to fit into any gap left by the element.*

*This <div> element has position: relative;*

*Example*

``` ruby
div.relative {
  position: relative;
  left: 30px;
  border: 3px solid #73AD21;
}
```

## 3-Absolute positioning


> An element with `position: absolute;` is positioned relative to the nearest positioned ancestor (instead of positioned relative to the viewport, like fixed).
> When the position property is given a value of absolute, the box is taken out of normal flow and no longer affects the position of other elements on the page. (They act like it is not there.)

*Example:-*
``` ruby
div.relative {
  position: relative;
  width: 400px;
  height: 200px;
  border: 3px solid #73AD21;
}

div.absolute {
  position: absolute;
  top: 80px;
  right: 0;
  width: 200px;
  height: 100px;
  border: 3px solid #73AD21;
}
``` 

<hr>

``` ruby
h1 {
position: absolute;
top: 0px;
left: 500px;
width: 250px;}
p {
width: 450px;}
```


<hr>


To indicate where a box should be positioned, you may also need to use <br>
box offset properties to tell the browser how far from the top or bottom <br>
and left or right it should be placed. 


## 1-Fixed Positioning


> An element with `position: fixed;` is positioned relative to the viewport, which means it always stays in the same place even if the page is scrolled. The top, right, bottom, and left properties are used to position the element.

``` ruby 

div.fixed {
  position: fixed;
  bottom: 0;
  right: 0;
  width: 300px;
  border: 3px solid #73AD21;
}
```



## 2-Floating Elements


> The float property allows you to take an element in normal flow and place it as far to the left or right of the containing element as possible. Anything else that sits inside the containing element will flow around the element that is floated.


*Example:*
``` ruby 
blockquote {
float: right;
width: 275px;
font-size: 130%;
font-style: italic;
font-family: Georgia, Times, serif;
margin: 0px 0px 10px 10px;
padding: 10px;
border-top: 1px solid #665544;
border-bottom: 1px solid #665544;}
```


<hr>

 ## Creating multip-column layouts with floats


> Many web pages use multiple columns in their design. This is achieved by using a <div> element to represent each column. The following three CSS properties are used to position the columns next to each other:

***width***
*This sets the width of the columns.*
***float***
*This positions the columns next to each other.*
***margin***
*This creates a gap between the columns.*


## Screen Sizes

![](https://www.seobility.net/en/wiki/images/6/6f/Media-Queries.png)

> Different visitors to your site will have different sized screens that show different amounts of information, so your design needs to be able to work on a range of different sized screens.

## Screen Resolution
> Resolution refers to the number of dots a screen shows per inch. Some devices have a higher resolution than desktop computers and most operating systems allow users to adjust the resolution of their screens.

## How to Create a Fixed-Width Layout with CSS
> A "fixed-width" layout is one in which the layout of the page is contained within a wrapper that doesn't adjust its size when the width of the browser changes.



## Liquid layout example

![](https://uxstepbystep.com/wordpress/wp-content/uploads/2017/02/example-liquid-layout.jpg)

*Combination liquid and fixed layouts*
> Similar to liquid layouts, except one or more of the containers on the page have fixed widths.



## Multiple Style Sheets

***link***
On this page you can see the other technique for including multiple style sheets. Inside the `<head>` element is a separate `<link>` element for each style sheet.







