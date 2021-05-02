# Responsive Web Design

With the growth in mobile Internet usage comes the question of how to build websites suitable for all users. The industry response to this question has become responsive web design, also known as RWD.

## Responsive Overview 

![img](https://hackernoon.com/images/1tjg32bo.jpg)

**Responsive vs. Adaptive vs. Mobile** 

Put simply, responsive is fluid and adapts to the size of the screen no matter what the target device. Responsive uses CSS media queries to change styles based on the target device such as display type, width, height, etc., and only one of these is necessary for the site to adapt to different screens.

Adaptive design, on the other hand, uses static layouts based on breakpoints which don’t respond once they’re initially loaded. Adaptive works to detect the screen size and load the appropriate layout for it – generally you would design an adaptive site for six common screen widths:

- 320
- 480
- 760
- 960
- 1200
- 1600

Mobile means to build a separate website commonly on a new domain solely for mobile users.

## Flexable Layouts

Responsive web design is broken down into three main components, including flexible layouts, media queries, and flexible media. The first part, flexible layouts, is the practice of building the layout of a website with a flexible grid, capable of dynamically resizing to any width. Flexible grids are built using relative length units, most commonly percentages or em units. These relative lengths are then used to declare common grid property values such as width, margin, or padding.

 Fortunately, There are formula to help identify the proportions of a flexible layout using relative values
 `target ÷ context = result`.

 Media Queries Media queries were built as an extension to media types commonly found when targeting and including styles. Media queries provide the ability to specify different styles for individual browser and device circumstances, the width of the viewport or device orientation.

It uses the @media rule to include a block of CSS properties only if a certain condition is true. for example:

`@media only screen and (max-width: 600px) {
 body {
      background-color: lightblue;
      }
}`


In this example, If the browser window is 600px or smaller, the background color will be lightblue.

Flexible Media Media that move and scale with our flexible grid is another key feature of a responsive web design. Flexible Media often give web designers a bit of a headache. Loading in huge, oversized images that we scale down using width and height HTML attributes when we want more space for text content on smaller browsing devices is not a good practice for faster web page load times.

Images, videos, and other media types need to be scalable, changing their size as the size of the viewport changes. One quick way to make media scalable is by using the max-width property with a value of 100%. Doing so ensures that as the viewport gets smaller any media will scale down according to its containers width.