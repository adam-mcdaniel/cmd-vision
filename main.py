import sys
import cv2, time
from small_vision import *

cmd = sys.argv[1:]
print(cmd)


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
        return self

    def convert_to_bgr(self):
        if self.image_type == "HSV":
            self.data = cv2.cvtColor(
                self.data,
                cv2.COLOR_HSV2BGR
            )
        return self


# python main.py --show "original" --hsv --mask 27 100 100 40 255 255 --blur 1 --draw_target --bgr --show "output"
def main(image):
    n = 0
    while True:
        if n >= len(cmd):
            break

        # print("current token:", cmd[n])

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
        elif cmd[n] == "--show":
            image.show(cmd[n+1])
            n += 1
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

n = 0
while True:
    n += 1
    start = time.time()


    _, raw = cap.read()
    result = main(
        CMD_Image(raw).resize((340, 240))
        )
    print(result)
    # if n % 10 == 0:
    #     print(
    #         1.0 / (time.time() - start)
    #     )

    if escape_key_pressed():
        break