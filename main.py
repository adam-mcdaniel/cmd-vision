import sys
import cv2, time
from small_vision import *

cmd = sys.argv[1:]


class CMD_Image(Image):
    def __init__(self, image):
        super().__init__(image)
        self.image_type = "BGR"
        self.mask_value = None

    def mask(self, a, b, c, d, e, f):
        self.mask_value = self.get_mask(
            [a, b, c],
            [d, e, f]
        )

        super().mask(
            self.mask_value
        )
        return self

    def draw_target(self):
        super().draw_target(
            self.mask_value
        )
        return self

    def get_target(self):
        return self.get_largest_blob(
            self.mask_value
        )
        
    def convert_to_hsv(self):
        if self.image_type == "BGR":
            self.data = cv2.cvtColor(
                self.data,
                cv2.COLOR_BGR2HSV
            )
        self.image_type = "HSV"
        return self

    def convert_to_bgr(self):
        if self.image_type == "HSV":
            self.data = cv2.cvtColor(
                self.data,
                cv2.COLOR_HSV2BGR
            )
        self.image_type = "BGR"
        return self


def parse(image):
    n = 0
    while True:
        if n >= len(cmd):
            break

        if cmd[n] == "--mask":
            image.mask(
                int(cmd[n+1]),
                int(cmd[n+2]),
                int(cmd[n+3]),
                int(cmd[n+4]),
                int(cmd[n+5]),
                int(cmd[n+6])
                )
            n += 6
        elif cmd[n] == "--resize":
            image.resize(
                (int(cmd[n+1]), int(cmd[n+2]))
                )
            n += 2
        elif cmd[n] == "--show":
            image.show(cmd[n+1])
            n += 1
        elif cmd[n] == "--smooth":
            image.smooth()
        elif cmd[n] == "--draw_target":
            image.draw_target()
        elif cmd[n] == "--blur":
            image.blur(float(cmd[n+1]))
            n += 1
        elif cmd[n] == "--bgr":
            image.convert_to_bgr()
        elif cmd[n] == "--hsv":
            image.convert_to_hsv()
        n += 1

    return image.get_target()


cap = cv2.VideoCapture(0)


while True:
    _, raw = cap.read()
    result = parse(
        CMD_Image(raw)
        )
    
    print(result)

    if escape_key_pressed():
        break