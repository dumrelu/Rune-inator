import pyautogui
from time import sleep
import murderbridge
import os

# All positions relative to the "GridView" button
PRIMARY_RUNE_TYPE_FIRST = (60, -465)
PRIMARY_RUNE_TYPE_OFFSET = (40, 0)

PRIMARY_RUNE_FIRST_ROW = (71, -342)
PRIMARY_RUNE_ROW_OFFSET = (0, 90)
PRIMARY_RUNE_3_COLUMNS_OFFSET = (65, 0)
PRIMARY_RUNE_4_COLUMNS_OFFSET = (45, 0)

SECONDARY_RUNE_TYPE_FIRST = (390, -465)
SECONDARY_RUNE_TYPE_OFFSET = (50, 0)

SECONDARY_RUNE_FIRST_ROW = (400, -370)
SECONDARY_RUNE_ROW_OFFSET = (0, 80)
SECONDARY_RUNE_3_COLUMNS_OFFSET = (65, 0)
SECONDARY_RUNE_4_COLUMNS_OFFSET = (45, 0)


SHARDS_FIRST_ROW = (397, -157)
SHARDS_ROW_OFFSET = (0, 45)
SHARDS_COLUMN_OFFSET = (65, 0)


SAVE_BUTTON = (327, -548)

# Hold how many runes are on each row
NUMBER_OF_RUNES = [
    [4, 3, 3, 3],   # Precision
    [4, 3, 3, 4],   # Domination
    [3, 3, 3, 3],   # Sorcery
    [3, 3, 3, 3],   # Resolve
    [3, 3, 3, 3]    # Inspiration
]

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
    champ = pyautogui.prompt("Please enter the name of the champ with no spaces(e.g. for Cho'gath type Chogath). After that select the LoL client and open the rune page editor.")
    if not champ:
        exit(0)
    runes = murderbridge.get_runes(champ)
    print(runes)

    # Time(s) to wait between pyautogui commands
    pyautogui.PAUSE = 0.5

    # pyautogui.alert('This displays some text with an OK button.')

    # Find the grid button position. All positions are relative to this one
    grid_view_image_path = os.path.dirname(__file__) + os.sep + "images" + os.sep + "GridView.png"
    grid_rect = find_on_screen(grid_view_image_path, 15)
    if not grid_rect:
        print("Could not find grid location. Probably the LoL client was not visible on the primary screen")
        exit(1)
    grid_location = pyautogui.center(grid_rect)

    # Click on the grid button
    clickRel(grid_location, (0, 0))

    # Select the primary rune type
    primary_type_position = compute_offset_position(PRIMARY_RUNE_TYPE_FIRST, PRIMARY_RUNE_TYPE_OFFSET, runes["primary"])
    clickRel(grid_location, primary_type_position)

    # Select the secondary rune type
    secondary_type_position = compute_offset_position(SECONDARY_RUNE_TYPE_FIRST, SECONDARY_RUNE_TYPE_OFFSET, runes["secondary"])
    clickRel(grid_location, secondary_type_position)

    # Select the primary runes
    for i in range(4):
        row = compute_offset_position(PRIMARY_RUNE_FIRST_ROW, PRIMARY_RUNE_ROW_OFFSET, i)

        offset = PRIMARY_RUNE_3_COLUMNS_OFFSET
        if NUMBER_OF_RUNES[runes["primary"]][i] == 4:
            offset = PRIMARY_RUNE_4_COLUMNS_OFFSET

        rune_index = runes["primaryValues"][i]
        pos = compute_offset_position(row, offset, rune_index)
        clickRel(grid_location, pos)

    # Select the secondary runes
    for i in range(3):
        row = compute_offset_position(SECONDARY_RUNE_FIRST_ROW, SECONDARY_RUNE_ROW_OFFSET, i)

        rune_type = runes["secondary"]
        if rune_type >= runes["primary"]:
            rune_type += 1

        offset = SECONDARY_RUNE_3_COLUMNS_OFFSET
        if NUMBER_OF_RUNES[rune_type][i + 1] == 4: 
            offset = SECONDARY_RUNE_4_COLUMNS_OFFSET

        rune_index = runes["secondaryValues"][i]
        if rune_index < 0:
            continue
        pos = compute_offset_position(row, offset, rune_index)
        clickRel(grid_location, pos)

    # Select shards
    for i in range(3):
        row = compute_offset_position(SHARDS_FIRST_ROW, SHARDS_ROW_OFFSET, i)
        offset = SHARDS_COLUMN_OFFSET

        pos = compute_offset_position(row, offset, runes["shards"][i])
        clickRel(grid_location, pos)
    
    # Save the runes
    clickRel(grid_location, SAVE_BUTTON)
