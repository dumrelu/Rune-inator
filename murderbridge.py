from requests_html import HTMLSession

BASE_URL = "https://www.murderbridge.com/Champion/{}"
PRIMARY_RUNES_SELECTOR = "//div[@class='runes-column runes-primary']"
PRIMARY_RUNES_OPTIONS = "//div[@class='rune-primary-options']"
PRIMARY_RUNES_NTH_ROW = PRIMARY_RUNES_OPTIONS + "/div[@class='rune-options-row'][{}]"
PRIMARY_RUNES_NTH_ROW_MTH_COL = PRIMARY_RUNES_NTH_ROW + "/div[{}]"

def get_runes(championName):
    session = HTMLSession()
    r = session.get(BASE_URL.format(championName))

    result = {}
    result["championName"] = championName

    # Find the primary runes
    result["primary"] = []
    for row in range(4):
        for column in range(3):
            value = r.html.xpath(PRIMARY_RUNES_NTH_ROW_MTH_COL.format(row + 1, column + 1))

            if(len(value) != 1):
                print("Could not find rune value")
                exit(1)
            value = value[0]

            # On murderbridge.com, non-selected runes have a grayscale effect
            #applied and the selected ones have none.
            if len(value.attrs["class"]) == 0:
                result["primary"].append(column)
    if len(result["primary"]) != 4:
        print("Number of primary runes != 4")
        exit(1)
    
    return result
                

if __name__ == "__main__":
    runes = get_runes("lux")
    print(runes)