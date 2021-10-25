from lab_oop.color import FigureColor
from lab_oop.figure import Figure

class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, w_param, h_param):
        self.w = w_param
        self.h = h_param
        self.fc = FigureColor()
        self.fc.colorproperty = color_param
    def square(self):
        return self.h * self.w

    def __repr__(self):
        return '\033[34m{}\033[0m {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.fc.colorproperty,
            self.w,
            self.h,
            self.square()
            )
