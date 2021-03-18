# CSS Transforms, Transitions, and Animations

## **Transforms**

With CSS3 came new ways to position and alter elements. Now general layout techniques can be revisited with alternative ways to size, position, and change elements. All of these new techniques are made possible by the transform property.

***syntax***: 
`-webkit-transform: scale(1.5);`

`-moz-transform: scale(1.5);`

`-o-transform: scale(1.5);`

`transform: scale(1.5);`

### 2D Transforms

![image2D](https://www.vanseodesign.com/blog/wp-content/uploads/2011/11/transform.png)
Elements may be distorted, or transformed, on both a two-dimensional plane or a three-dimensional plane. Two-dimensional transforms work on the x and y axes, known as horizontal and vertical axes. Three-dimensional transforms work on both the x and y axes, as well as the z axis. These three-dimensional transforms help define not only the length and width of an element, but also the depth. We’ll start by discussing how to transform elements on a two-dimensional plane, and then work our way into three-dimensional transforms.

### 3D Transforms


![](https://www.tutorialrepublic.com/lib/images/css3-3d-scale-illustration.png)

Working with two-dimensional transforms we are able to alter elements on the horizontal and vertical axes, however there is another axis along which we can transform elements. Using three-dimensional transforms we can change elements on the z axis, giving us control of depth as well as length and width


## Transitions & Animations

**Transitions**

For a transition to take place, an element must have a change in state, and different styles must be identified for each state. The easiest way for determining styles for different states is by using the :hover, :focus, :active, and :target pseudo-classes.

**Animations**

Transitions do a great job of building out visual interactions from one state to another, and are perfect for these kinds of single state changes. However, when more control is required, transitions need to have multiple states. In return, this is where animations pick up where transitions leave off.

*Animations Keyframes*

To set multiple points at which an element should undergo a transition, use the @keyframes rule. The @keyframes rule includes the animation name, any animation breakpoints, and the properties intended to be animated.

