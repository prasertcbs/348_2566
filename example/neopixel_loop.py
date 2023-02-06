# neopixel for MicroPython on ESP32

from machine import Pin
from neopixel import NeoPixel
from time import sleep, sleep_ms
import random

# led_pin=12 # for ESP32 with expansion board
led_pin = 13  # for Wemos D1 R2 (Pin D7=GPIO13)

# led_pin=23 # for KidBright
lights = 24
max_led_brightness = 50  # 0 - 255


def max_brightness(pixel_rgb: tuple, max_bri=50):
    return (
        int(pixel_rgb[0] * max_bri / 255),
        int(pixel_rgb[1] * max_bri / 255),
        int(pixel_rgb[2] * max_bri / 255),
    )


def randcolor(bit=8):
    return (random.getrandbits(bit), random.getrandbits(bit), random.getrandbits(bit))
    # return (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))


rainbow = [
    (126, 1, 0),
    (114, 13, 0),
    (102, 25, 0),
    (90, 37, 0),
    (78, 49, 0),
    (66, 61, 0),
    (54, 73, 0),
    (42, 85, 0),
    (30, 97, 0),
    (18, 109, 0),
    (6, 121, 0),
    (0, 122, 5),
    (0, 110, 17),
    (0, 98, 29),
    (0, 86, 41),
    (0, 74, 53),
    (0, 62, 65),
    (0, 50, 77),
    (0, 38, 89),
    (0, 26, 101),
    (0, 14, 113),
    (0, 2, 125),
    (9, 0, 118),
    (21, 0, 106),
    (33, 0, 94),
    (45, 0, 82),
    (57, 0, 70),
    (69, 0, 58),
    (81, 0, 46),
    (93, 0, 34),
    (105, 0, 22),
    (117, 0, 10),
]

pixels = NeoPixel(Pin(led_pin), lights)


def blue_shade():
    while True:
        for i in range(lights):
            pixels[i] = max_brightness(
                (0, 0, int(255 - i * (256 / lights))), max_led_brightness
            )
            pixels.write()
            sleep(0.1)

        for i in range(lights - 1, 0, -1):
            pixels[i] = max_brightness(
                (int(255 - i * (256 / lights)), 0, 0), max_led_brightness
            )
            pixels.write()
            sleep(0.1)

        for i in range(lights):
            pixels[i] = max_brightness(
                (0, int(255 - i * (256 / lights)), 0), max_led_brightness
            )
            pixels.write()
            sleep(0.1)

        for i in range(lights):
            pixels[i] = max_brightness(randcolor(bit=8), max_led_brightness)
            pixels.write()
            sleep(0.1)

        pixels.fill((0, 0, 0))
        pixels.write()
        sleep(1)


#         for i in range(lights):
#             pixels[i]=(255, 0,int(255-i*(256 / lights)))
#         pixels.write()


def demo1():
    for i in range(lights):
        if i % 2 == 0:
            pixels[i] = (0, 0, 0)
        else:
            pixels[i] = (255, 0, 0)
    pixels.write()

    while True:
        for i in range(lights):
            if i % 2 == 1:
                pixels[i] = randcolor()
            else:
                pixels[i] = (0, 0, 0)
        pixels.write()
        sleep(0.7)
        for i in range(lights):
            if i % 2 == 0:
                pixels[i] = randcolor()
            else:
                pixels[i] = (0, 0, 0)
        pixels.write()
        sleep(0.7)


def loop1(no_lights=24, delay_ms=150, rgb=(255, 0, 0), step=1):
    for i in range(0, no_lights, step):
        # pixels[i]=randcolor()
        pixels[i] = rgb
        pixels.write()
        sleep_ms(delay_ms)


def loop2(no_lights=24, delay_ms=150, rgb=(255, 0, 0), step=-1):
    for i in range(no_lights - 1, -1, step):
        # pixels[i]=randcolor()
        pixels[i] = rgb
        pixels.write()
        sleep_ms(delay_ms)


if __name__ == "__main__":
    pixels.fill((0, 0, 0))
    pixels.write()
    try:
        # blue_shade()
        # demo1()
        for i in range(5):
            loop1(rgb=(0, 255, 0))
            pixels.fill((0, 0, 0))
            pixels.write()
            for j in range(2, 6):
                loop1(rgb=randcolor(), step=j)
                pixels.fill((0, 0, 0))
                pixels.write()
            loop2(rgb=randcolor(), step=-1)
            pixels.fill((0, 0, 0))
            pixels.write()
            # loop2(rgb=(0, 0, 0))
            loop2(rgb=randcolor(), step=-2)
            pixels.fill((0, 0, 0))
            pixels.write()
            # loop2(rgb=(0, 0, 0))
            # pixels.fill((0,0,0))
    except KeyboardInterrupt:
        print("Interrupted, turn off all lights")
        pixels.fill((0, 0, 0))
        pixels.write()
#         for i in range(lights):
#             pixels[i]=(0,0,0)
#         pixels.write()
