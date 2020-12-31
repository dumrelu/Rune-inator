import pyautogui
import murderbridge

def find_on_screen(image, repeat_count=5):
    for i in range(repeat_count):
        location = pyautogui.locateOnScreen(image, minSearchTime=1)

        if location:
            return location
    
    print("Could not find", image)
    return None

if __name__ == "__main__":
    # TODO: is this necessary?
    pyautogui.PAUSE = 2.5
    # pyautogui.alert('This displays some text with an OK button.')

    
    location = find_on_screen("images/GridView.png")
    print("Location:", location)
