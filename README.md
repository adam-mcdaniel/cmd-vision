# cmd-vision
A command line tool for vision processing

## How do I use it?

Run main.py with the instructions you want, in the order that you want.

Here are the available commands:


```
--show NAME
    opens a window named NAME displaying the current image

--resize WIDTH HEIGHT
    resizes the current image

--smooth
    removes specs and closes holes

--blur PERCENTAGE
    blurs PERCENTAGE percent

--blur PERCENTAGE
    blurs PERCENTAGE percent

--bgr
    converts current image to BGR format

--hsv
    converts current image to HSV format

--mask A B C D E F
    masks an image using [A, B, C] as the lower bounds, and [C, D, E] as the upper bounds

--draw_target
    after a mask is applied, this will draw a circle around the largest blob in the masked image
```