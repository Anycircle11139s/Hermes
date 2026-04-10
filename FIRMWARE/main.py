import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_ssd1306
import adafruit_lm75na
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

# 1. Keyboard & State Setup 
keyboard = KMKKeyboard()
is_bright = True  # Track the current brightness state

# 2. Rotary Encoder Setup 
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D0, board.D1, board.D2, False),)

# Volume on rotate
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.NO),), 
]

#  3. I2C & Display Setup 
displayio.release_displays()
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lm75na.LM75NA(i2c)

display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_ssd1306.SSD1306(display_bus, width=128, height=64)

splash = displayio.Group()
display.show(splash)

text_area = label.Label(terminalio.FONT, text="Hermes Initializing", color=0xFFFFFF, x=8, y=30)
splash.append(text_area)

# 4. Brightness Toggle Logic
def toggle_brightness():
    global is_bright
    is_bright = not is_bright
    if is_bright:
        display.contrast(255) # Full Brightness
    else:
        display.contrast(0)   # Dim Mode (lowest visible setting)

# 5. Main Loop 
def update_system(keyboard):
    # Check if encoder button (D2) is pressed to toggle brightness
    try:
        temp = sensor.temperature
        bright_status = "High" if is_bright else "Low"
        text_area.text = f"Temp: {temp:.1f} C\nBrite: {bright_status}"
    except Exception:
        text_area.text = "Sensor Error"

keyboard.before_matrix_scan = update_system

# This listens for the D2 keypress specifically to trigger the toggle function
keyboard.keymap = [[KC.NO]] # Main keys

encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.TRNS),),
]

if __name__ == '__main__':
    keyboard.go()
