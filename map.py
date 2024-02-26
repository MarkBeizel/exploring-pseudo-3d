from settings import *

map_sample = [
    "▬▬▬▬▬▬▬▬▬▬▬▬",
    "▬   ▬      ▬",
    "▬  ▬▬▬▬▬   ▬",
    "▬      ▬   ▬",
    "▬▬▬  ▬     ▬",
    "▬▬▬  ▬   ▬▬▬",
    "▬         ▬▬",
    "▬▬▬▬▬▬▬▬▬▬▬▬",
]

# map = set()
# for n1, row in enumerate(map_sample):
#     for n2, char in enumerate(row):
#         if char == "▬":
#             map.add((n2 * x1, n1 * y1))

map = []
for n1, row in enumerate(map_sample):
    for n2, char in enumerate(row):
        if char == "▬":
            map.append((n2 * x_size2, n1 * y_size2))
            
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
