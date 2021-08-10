class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector - X : {self.x}, Y : {self.y}"

    def __len__(self):
        return 1

    def __call__(self, *args, **kwargs):
        

    def __del__(self):
        print("object being deconstructed")





