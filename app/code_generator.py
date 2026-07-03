from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import io

class LaetusCode:

    def __init__(self, code_nr: int, canvas_height: int = 20, dpi: int = 300):
        if not isinstance(code_nr, int):
            raise ValueError("The number must be an integer")
        if not 3<= code_nr <=131070:
            raise ValueError("The number must be between 3 and 131070")
        if not isinstance(canvas_height, int):
            raise ValueError("The canvas height must be an integer")
        if not 10 <= canvas_height <= 50:
            raise ValueError("The canvas height must be between 20 and 50 mm.")
        
        # Define the variables:

        self.code_nr = code_nr
        self.dpi = dpi

        #Dimensions of the bars, in mm
        self.narrow = 0.5
        self.wide = 1.55
        self.space = 1.0


        self.text_size = 4
        self.text_gap = 1

        self.canvas_height = canvas_height
        self.bar_height = self.canvas_height - self.text_size - 2 * self.text_gap

        self.code_folder = Path(__file__).resolve().parent / "codes"
        self.font = str(Path(__file__).resolve().parent / "fonts" / "DejaVuSans-Bold.ttf")

    def _to_px(self, mm):
        return int(round(mm*(self.dpi/25.4), 0))
    
    def _encode(self):
        laetus_number = self.code_nr
        laetus_string = ""
        while laetus_number > 0:
            if laetus_number % 2 == 1:
                laetus_string += "N"
                laetus_number = (laetus_number-1)//2
            else:
                laetus_string += "W"
                laetus_number = (laetus_number-2)//2
        
        return laetus_string[::-1]
    
    def _get_bars(self):
        laetus_string = self._encode()
        laetus_bars = []
        x_bar = self.space
        for bar in laetus_string:
            bar_width = self.narrow if bar == "N" else self.wide
            laetus_bars.append((x_bar, bar_width))
            x_bar += (bar_width + self.space)

        return laetus_bars, x_bar
    
    def _create_image(self):
        canvas_height_px = self._to_px(self.canvas_height)
        bar_height_px = self._to_px(self.bar_height)
        bars, canvas_width = self._get_bars()
        canvas_width_px = self._to_px(canvas_width)
        img = Image.new("L", (canvas_width_px, canvas_height_px), color="white")
        draw = ImageDraw.Draw(img)

        for x, width in bars:
            x = self._to_px(x)
            width = self._to_px(width)
            draw.rectangle([x, 0, x + width, bar_height_px], fill="black")

        font = ImageFont.truetype(self.font, self._to_px(self.text_size))
        text = str(self.code_nr)
        text_width = draw.textlength(text=text, font=font)
        x_text = (canvas_width_px - text_width)/2
        draw.text((x_text, bar_height_px + self._to_px(self.text_gap)), text=text, font=font, fill="black")

        return img
    
    def to_jpg(self):
        code_img = self._create_image()
        buffer = io.BytesIO()
        code_img.save(buffer, format="JPEG")
        buffer.seek(0)

        return buffer
    
    def to_png(self):
        code_img = self._create_image()
        buffer = io.BytesIO()
        code_img.save(buffer, format="PNG")
        buffer.seek(0)

        return buffer
    
    def to_jpg_file(self):
        code_img = self._create_image()

        self.code_folder.mkdir(parents=True, exist_ok=True)

        code_img.save(self.code_folder / f"{self.code_nr}.jpg", format="JPEG")

    def to_png_file(self):
        code_img = self._create_image()

        self.code_folder.mkdir(parents=True, exist_ok=True)

        code_img.save(self.code_folder / f"{self.code_folder}.png", format="PNG")
