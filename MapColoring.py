regions =  ['delhi', 'chennai', 'mumbai', 'kolkata']
colors = ['red', 'green' , 'blue' , 'yellow']

neighbour = {
    'delhi': ['mumbai', 'chennai'],
    'chennai': ['mumbai', 'kolkata', 'delhi'],
    'mumbai': ['delhi', 'chennai', 'kolkata'],
    'kolkata': ['mumbai', 'chennai']
}

region_color = {}

def validation(region, color):
    for i in neighbour.get(region):
        nb_color = region_color.get(i)
        if nb_color == color:
            return False
    return True

def colorselection(region):
    for color in colors:
        if validation(region, color):
            return color

for region in regions:
    region_color[region] = colorselection(region)

print(region_color)

if not all(region_color.values()):
    print("Insufficient colors, please add more colors")
