class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height
    
  def get_area(self):
    return (self.width * self.height)
    
  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** 0.5)

  def get_picture(self):
    picture = ""
    if self.height > 50 or self.width > 50:
        return ("Too big for picture.")
    else:
      for row in range(self.height):
        for column in range(self.width):
          picture += "*"
        picture += "\n"
      return picture

  def get_amount_inside(self, shape):
    vertical = self.height // shape.height
    horizontal = self.width // shape.width
    return (vertical * horizontal)

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
    
  def __repr__(self):
    return f"Square(side={self.width})"    

  def set_height(self, side):
    self.height = side
    self.width = side

  def set_width(self, side):
    self.height = side
    self.width = side

  def set_side(self, side):
    self.height = side
    self.width = side