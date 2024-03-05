from settings import *

map_sample = [
    "◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘",
    "◘ □ ◘              ◘",
    "◘   ◘◘◘    ◘◘◘     ◘",
    "◘ G ◘ ◘    ◘◘◘     ◘",
    "◘   ◘◘◘    ◘◘◘  G  ◘",
    "◘          ◘◘◘     ◘",
    "◘          ◘◘◘     ◘",
    "◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘",
    "◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘",
    "◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘",
    "◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘",
    "◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘",
    "◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘",
    "◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘",
    "◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘",
    "◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘",
    "◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘",
    "◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘",
    "◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘",
    "◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘",
]

# map = set()
# for n1, row in enumerate(map_sample):
#     for n2, char in enumerate(row):
#         if char == "▬":
#             map.add((n2 * x1, n1 * y1))

map = []
for n1, row in enumerate(map_sample):
    for n2, char in enumerate(row):
        if char == "◘":
            map.append((n2 * x_size2, n1 * y_size2))

G = []
for n1, row in enumerate(map_sample):
    for n2, char in enumerate(row):
        if char == "G":
            G.append((5 * n2 * x_size3 + 80, 5 * n1 * x_size3 + 80))

mapx = []
mapy = []
for xy in map:
    for x, y in map:
        mapx.append(x)
        mapy.append(y)
            
            # ТЕСТ IDLE
# map_sample = [
#     "▬▬▬▬▬▬▬▬▬▬▬▬",
#     "▬          ▬",
#     "▬          ▬",
#     "▬          ▬",
#     "▬          ▬",
#     "▬          ▬",
#     "▬          ▬",
#     "▬▬▬▬▬▬▬▬▬▬▬▬",
# ]

# map = set()
# for n1, row in enumerate(map_sample):
#     for n2, char in enumerate(row):
#         if char == "▬":
#             map.add((n2 * 800, n1 * 800))

# for x, y in map:
#       print(x, y,)
