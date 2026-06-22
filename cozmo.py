import pycozmo
import pyautogui
import toml
import time
from PIL import Image, ImageOps, ImageEnhance

config = toml.load("config.toml")

cozmo = pycozmo.Client(enable_procedural_face=False)
cozmo.start()
cozmo.connect()
print("Waiting for cozmo...")
cozmo.wait_for_robot()

# assuming cozmo is now connected
print("Found a cozmo!")
cozmo.set_head_angle(16)

fpsCount = 0

while True:
    start = time.time()
    for _ in range(config["Screenshots"]["fps"]):
        frameScreenshot = pyautogui.screenshot().convert("L")
        frameScreenshot = ImageEnhance.Brightness(frameScreenshot).enhance(0.5)
        frameScreenshot = ImageEnhance.Contrast(frameScreenshot).enhance(2.5)
        # frameScreenshot = ImageOps.autocontrast(frameScreenshot)
        frameScreenshot.thumbnail((123, 32), Image.Resampling.LANCZOS)

        toPrint = Image.new("L", (128, 32), 0)
        h = round((128 - frameScreenshot.width) / 2)
        w = round((32 - frameScreenshot.height) / 2)
        toPrint.paste(frameScreenshot, (h, w))


        frame = toPrint.point(lambda p: 255 if p > 30 else 0).convert("1")

        toPrint.save("toPrintLog.png")
        frame.save("frameLog.png")

        cozmo.display_image(frame)
        frameCount += 1

    elapsed = time.time() - start
    print(f"Frames played {frameCount}, played in {elapsed:.2f} seconds, fps: {frameCount / elapsed:.1f} fps")
    fpsCount = 0
