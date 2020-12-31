import pyautogui
from time import sleep
import murderbridge

# Location: Point(x=324, y=892)
# First: Point(x=713, y=427)
# Second: Point(x=762, y=432)

# All positions relative to the "GridView" button
PRIMARY_RUNE_TYPE_FIRST = (60, -465)
PRIMARY_RUNE_TYPE_OFFSET = (40, 0)

SECONDARY_RUNE_TYPE_FIRST = (390, -465)
SECONDARY_RUNE_TYPE_OFFSET = (50, 0)

def find_on_screen(image, repeat_count=5):
    for i in range(repeat_count):
        location = pyautogui.locateOnScreen(image, confidence=0.9, minSearchTime=1)

        if location:
            return location
    
    print("Could not find", image)
    return None

def moveRel(center, position):
    pyautogui.moveTo(center.x + position[0], center.y + position[1])

def clickRel(center, position):
    moveRel(center, position)
    pyautogui.click()

def compute_offset_position(position, offset, scale=1):
    position = (
        position[0] + offset[0] * scale, 
        position[1] + offset[1] * scale
    )
    return position

if __name__ == "__main__":
    # Get the runes for the given champion
    champ = "Lux"
    runes = murderbridge.get_runes(champ)
    print(runes)

    # Time(s) to wait between pyautogui commands
    pyautogui.PAUSE = 0.5

    # pyautogui.alert('This displays some text with an OK button.')

    # Find the grid button position. All positions are relative to this one
    grid_location = pyautogui.center(find_on_screen("images/GridView.png"))

    # Click on the grid button
    clickRel(grid_location, (0, 0))

    # Select the primary rune type
    primary_type_position = compute_offset_position(PRIMARY_RUNE_TYPE_FIRST, PRIMARY_RUNE_TYPE_OFFSET, runes["primary"])
    clickRel(grid_location, primary_type_position)

    # Select the secondary rune type
    secondary_type_position = compute_offset_position(SECONDARY_RUNE_TYPE_FIRST, SECONDARY_RUNE_TYPE_OFFSET, runes["secondary"])
    clickRel(grid_location, secondary_type_position)

    # while True:
    #     print(pyautogui.position())
    #     sleep(1.0)
