
from PIL import Image, ImageFont, ImageDraw, ImageTk

import textwrap

try:
    from Tkinter import Label
except ImportError:
    from tkinter import Label
    
def truetype_font(font_path, size):
    return ImageFont.truetype(font_path, size)

class CustomFont_Label(Label):
    def __init__(self, master, text, foreground="black", truetype_font=None, font_path=None, family=None, size=None, **kwargs):   
        if truetype_font is None:
            if font_path is None:
                raise ValueError("Font path can't be None")
                
            # Initialize font
            truetype_font = ImageFont.truetype(font_path, size)
        
        width, height = truetype_font.getsize(text)

        image = Image.new("RGBA", (width, height), color=(0,0,0,0))
        draw = ImageDraw.Draw(image)

        draw.text((0, 0), text, font=truetype_font, fill=foreground)
        
        self._photoimage = ImageTk.PhotoImage(image)
        Label.__init__(self, master, image=self._photoimage, **kwargs)


class CustomFont_Message(Label):
    def __init__(self, master, text, width, foreground="black", truetype_font=None, font_path=None, family=None, size=None, **kwargs):   
        if truetype_font is None:
            if font_path is None:
                raise ValueError("Font path can't be None")
                
            # Initialize font
            truetype_font = ImageFont.truetype(font_path, size)
    
        lines = textwrap.wrap(text, width=width)

        width = 0
        height = 0
        
        line_heights = []
        for line in lines:
            line_width, line_height = truetype_font.getsize(line)
            line_heights.append(line_height)
            
            width = max(width, line_width)
            height += line_height

        image = Image.new("RGBA", (width, height), color=(0,0,0,0))
        draw = ImageDraw.Draw(image)

        y_text = 0
        for i, line in enumerate(lines):
            draw.text((0, y_text), line, font=truetype_font, fill=foreground)
            y_text += line_heights[i]

        self._photoimage = ImageTk.PhotoImage(image)
        Label.__init__(self, master, image=self._photoimage, **kwargs)

if __name__ == "__main__":
    try:
        from Tkinter import Tk
    except ImportError:
        from tkinter import Tk
        
    root = Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))

    lorem_ipsum ="""This font is not installed but still works on the PC"""

    # Use your font here: font_path
    CustomFont_Label(root, text="This is a text", font_path="H:\\Computer Resources\\PortableApps\\Launcher\\Phenomena-Regular.ttf", size=40).pack()
    CustomFont_Message(root, text=lorem_ipsum, width=40, font_path="H:\\Computer Resources\\PortableApps\\Launcher\\Phenomena-Regular.ttf", size=40).pack(pady=(30,0))
    
    root.mainloop()
