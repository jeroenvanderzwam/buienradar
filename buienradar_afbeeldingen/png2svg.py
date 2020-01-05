import os
from base64 import b64encode

def png_to_svg():
    for file in os.listdir("png"):
        if file.endswith(".png"):

            startSvgTag = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
            <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
            "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
            <svg version="1.1"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            width="30px" height="30px" viewBox="0 0 30 30">"""

            endSvgTag = """</svg>"""

            with open(f'png/{file}', 'rb') as png:
                base64data = b64encode(png.read()).decode('utf-8').replace('\n','')
                base64String = f'<image xlink:href="data:image/png;base64,{base64data}" width="30" height="30" x="0" y="0" />'

                with open(f'svg/{os.path.splitext(file)[0]}.svg','w') as f:
                    f.write( startSvgTag + base64String + endSvgTag)

png_to_svg()
