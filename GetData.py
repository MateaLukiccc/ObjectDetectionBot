from mss import mss # An ultra fast cross-platform multiple screenshots module in pure python using ctypes.
import keyboard
import time

keyboard.wait("space")
image_count = 0

while not keyboard.is_pressed("q"):
    with mss() as screen_shot:
        filename = screen_shot.shot(mon=2, output=f".\ImageData\Toadled-{image_count}.png") # mon=2 -> second monitor
        print(filename)
        image_count += 1
        time.sleep(1) 