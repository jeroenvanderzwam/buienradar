import requests
import string
import os

letters = string.ascii_lowercase[:-3]

for letter in letters:
    r = requests.get(f'https://www.buienradar.nl/resources/images/icons/weather/30x30/{letter}.png')
    r2 = requests.get(f'https://www.buienradar.nl/resources/images/icons/weather/30x30/{letter}{letter}.png')
    
    open(f'png/{letter}.png', 'wb').write(r.content)
    open(f'png/{letter}{letter}.png', 'wb').write(r2.content)
