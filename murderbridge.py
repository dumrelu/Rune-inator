from requests_html import HTMLSession

# General
BASE_URL = "https://www.murderbridge.com/Champion/{}"
NTH_STYLE_SELECTOR = "/div[contains(concat(' ',normalize-space(@class),' '),'style-selector')]/div[@role='button'][{}]"

# Primary runes
PRIMARY_RUNES_SELECTOR = "//div[@class='runes-column runes-primary']"
PRIMARY_RUNES_OPTIONS = "//div[@class='rune-primary-options']"
PRIMARY_RUNES_NTH_TYPE = PRIMARY_RUNES_OPTIONS + NTH_STYLE_SELECTOR
PRIMARY_RUNES_NTH_ROW = PRIMARY_RUNES_OPTIONS + "/div[@class='rune-options-row'][{}]"
PRIMARY_RUNES_NTH_ROW_MTH_COL = PRIMARY_RUNES_NTH_ROW + "/div[{}]"

# Secondary runes
SECONDARY_RUNES_SELECTOR = "//div[@class='runes-column runes-secondary']"
SECONDARY_RUNES_OPTIONS = "//div[@class='rune-primary-options-subperk']"
SECONDARY_RUNES_NTH_TYPE = SECONDARY_RUNES_OPTIONS + NTH_STYLE_SELECTOR
SECONDARY_RUNES_NTH_ROW = SECONDARY_RUNES_OPTIONS + "/div[@class='rune-options-row-subperk'][{}]"
SECONDARY_RUNES_NTH_ROW_MTH_COL = SECONDARY_RUNES_NTH_ROW + "/div[{}]"

# Shards
SHARDS_CONTAINER = "//div[@class='stat-shard-right']"
SHARDS_NTH_ROW = SHARDS_CONTAINER + "/div[@class='stat-shard-row'][{}]"
SHARDS_NTH_ROW_MTH_COLUMN = SHARDS_NTH_ROW + "/div[{}]"

def get_runes(championName):
    session = HTMLSession()
    r = session.get(BASE_URL.format(championName))

    result = {}
    result["championName"] = championName

    # Primary runes
    for index in  range(5):
        value = r.html.xpath(PRIMARY_RUNES_NTH_TYPE.format(index + 1))
        
        if len(value) != 1:
            print("Invalid primary rune value")
            exit(1)
        value = value[0]

        for c in value.attrs["class"]:
            if c == "selected":
                result["primary"] = index
                break
    
    if "primary" not in result:
        print("Could not find primary value")
        exit(1)

    # Primary rune values
    result["primaryValues"] = []
    for row in range(4):
        for column in range(4):
            value = r.html.xpath(PRIMARY_RUNES_NTH_ROW_MTH_COL.format(row + 1, column + 1))

            if(len(value) != 1):
                continue
            value = value[0]

            # On murderbridge.com, non-selected runes have a grayscale effect
            #applied and the selected ones have none.
            if len(value.attrs["class"]) == 0:
                result["primaryValues"].append(column)
    
    if len(result["primaryValues"]) != 4:
        print("Number of primary runes != 4")
        exit(1)
    
    # Secondary runes
    for index in  range(4):
        value = r.html.xpath(SECONDARY_RUNES_NTH_TYPE.format(index + 1))
        
        if len(value) != 1:
            print("Invalid secondary rune value")
            exit(1)
        value = value[0]

        for c in value.attrs["class"]:
            if c == "selected":
                result["secondary"] = index
                break
    
    if "secondary" not in result:
        print("Could not find secondary value")
        exit(1)

    # Secondary rune values
    result["secondaryValues"] = []
    for row in range(3):
        result["secondaryValues"].append(-1)
        for column in range(4):
            value = r.html.xpath(SECONDARY_RUNES_NTH_ROW_MTH_COL.format(row + 1, column + 1))
            
            if(len(value) != 1):
                continue
            value = value[0]

            # Same logic as for rows
            if len(value.attrs["class"]) == 0:
                result["secondaryValues"][-1] = column
    
    if len(result["secondaryValues"]) != 3:
        print("Number of secondary runes != 3")
        exit(1)
    
    # Shards
    result["shards"] = []
    for row in range(3):
        for column in range(3):
            value = value = r.html.xpath(SHARDS_NTH_ROW_MTH_COLUMN.format(row + 1, column + 1))

            if(len(value) != 1):
                continue
            value = value[0]

            # Same logic as for rows
            if len(value.attrs["class"]) == 0:
                result["shards"].append(column)


    return result
                

if __name__ == "__main__":
    champName = input("Name of chamption: ")
    runes = get_runes(champName)
    print(runes)