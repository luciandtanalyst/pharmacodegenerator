from pathlib import Path

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
    
