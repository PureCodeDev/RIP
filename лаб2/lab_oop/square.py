from lab_oop.rectangle import Rectangle

class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, a_param):
        self.a = a_param
        super().__init__(color_param, self.a, self.a)

    def __repr__(self):
        return '\033[33m{}\033[0m {} цвета со стороной {} площадью {}.'.format(
            Square.get_figure_type(),
            self.fc.colorproperty,
            self.a,
            self.square()
        )
