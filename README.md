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

--bgr
    converts current image to BGR format

--hsv
    converts current image to HSV format

--mask A B C D E F
    masks an image using [A, B, C] as the lower bounds, and [C, D, E] as the upper bounds

--draw_target
    after a mask is applied, this will draw a circle around the largest blob in the masked image
```

## Examples

Resizing an image

```
python3 main.py --resize 320 240 --show "Resized image"
```

Blurring and smoothing an image
```
python3 main.py --resize 320 240 --blur 0.7 --smooth --show "Blurred and smoothed image"
```

Converting to HSV and masking an image
```
python3 main.py --resize 320 240 --hsv --mask 60 40 40 90 255 255 --bgr --show "Masked image"
```

Converting to HSV, masking an image, and drawing a target
```
python3 main.py --resize 320 240 --hsv --mask 60 40 40 90 255 255 --draw_target --bgr --show "Masked image"
```

Converting to HSV, masking an image, smoothing an image, blurring an image, and drawing a target
```
python3 main.py --resize 320 240 --hsv --mask 60 40 40 90 255 255 --smooth --blur 0.2 --draw_target --bgr --show "Masked image"
```

Showing the original image, converting to HSV, masking an image, smoothing an image, blurring an image, and drawing a target
```
python3 main.py --resize 320 240 --show "Original image" --hsv --mask 60 40 40 90 255 255 --smooth --blur 0.2 --draw_target --bgr --show "Masked image"
```