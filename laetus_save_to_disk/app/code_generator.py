from PIL import Image, ImageDraw, ImageFont
import os

class LaetusCode:

    def __init__(self, number: int, canvas_height: int=200):

        if not (isinstance(number, int)):
            raise ValueError("The number must be an integer.")
        if not 3 <= number <= 131070:
            raise ValueError("The number must be between 3 and 131070.")
        
        if not (isinstance(canvas_height, int)):
            raise ValueError("The image height must be an integer.")
        if not 20 <= canvas_height <= 200:
            raise ValueError("The height must be between 20 and 200 pixels.")
        
        self.number = number
        self.canvas_height = canvas_height
        self.bar_height = 2*(canvas_height//3)

        self.narrow = 5
        self.wide = 15
        self.space = 10


    def laetus_string(self):
        laetus_number = self.number
        laetus_string = ""
        while laetus_number > 0:
            if laetus_number % 2 == 1:
                laetus_string += "N"
                laetus_number = (laetus_number-1)//2
            else:
                laetus_string += "W"
                laetus_number = (laetus_number-2)//2

        self.code_width = 10 + sum(self.narrow+self.space if bar == "N" else self.wide+self.space for bar in laetus_string)

        return (laetus_string[::-1], self.code_width)

    
    def draw_code(self):
        string, canvas_witdh = self.laetus_string()
        img = Image.new("L", (canvas_witdh, self.canvas_height), color="white")
        draw = ImageDraw.Draw(img)
        height = self.bar_height
        x_bar = self.space

        for bar in string:
            if bar == "N":
                draw.rectangle([x_bar, 0, x_bar+self.narrow, height], fill="black")
                x_bar += (self.narrow+self.space)
            else:
                draw.rectangle([x_bar, 0, x_bar+self.wide, height], fill="black")
                x_bar += (self.wide+self.space)
        
        #Draw the number
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", self.canvas_height//4)
        text = str(self.number)
        text_width = draw.textlength(text=text, font=font)      #find the length of the text
        x_text = (canvas_witdh-text_width)/2                    #find the x coordinate to start the text drawing
        draw.text((x_text, self.bar_height+5), text=text, fill="black", font=font)

        #img.show()
        os.makedirs("./codes", exist_ok=True)
        try:
            img.save(f"./codes/{self.number}.jpg", "JPEG")
            return (0, f"Barcode {self.number} successfully saved as a JPG image.")
        except Exception as err:
            return (1, f"Error saving file: {err}")
