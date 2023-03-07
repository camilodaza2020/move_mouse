import pyautogui
import time

# Get the size of the screen
screenWidth, screenHeight = pyautogui.size()

# Set the size of the square pattern
squareSize = 200

# Calculate the coordinates of the square pattern
left = (screenWidth / 2) - (squareSize / 2)
top = (screenHeight / 2) - (squareSize / 2)
right = left + squareSize
bottom = top + squareSize

# Move the mouse in a square pattern
pyautogui.moveTo(left, top, duration=1)
pyautogui.moveTo(right, top, duration=1)
pyautogui.moveTo(right, bottom, duration=1)
pyautogui.moveTo(left, bottom, duration=1)

# Wait for a few seconds before exiting
time.sleep(10)
