import Figure 
f = Figure

circle = f.Circle(200, 30, 150)
square = f.Square(-200, 30, 100)
rectangle = f.Rectangle(4, 4, 70, 100)
triangle = f.Triangle(-75, -23, 50, 80, 90)
pentagon = f.Pentagon(100, -20, 50)
hexagon = f.Hexagon(10, 150, 50)
ellipse = f.Ellipse(-48, 65, 30, 45)

circle.drawing_figure('#FF6611', '#887766')
square.drawing_figure('#D5713F', '#F80000')
rectangle.drawing_figure('#FC74FD', '#B32428')
triangle.drawing_figure('#BB8B54', '#F75E25')
pentagon.drawing_figure('#B0C4DE', '#FF7E93')
hexagon.drawing_figure('#915F6D', '#C9A0DC')
ellipse.drawing_figure('#FFBF00', '#FFFACD')


print("S circle: ", circle.get_area())
print("P circle: ", circle.get_perimetr())
###(╯°□°）╯︵ ┻━┻
print("S square: ", square.get_area())
print("P square: ", square.get_perimetr())
###(╯°□°）╯︵ ┻━┻
print("S rectangle: ", rectangle.get_area())
print("P rectangle: ", rectangle.get_perimetr())
###(╯°□°）╯︵ ┻━┻
print("S triangle: ", triangle.get_area())
print("P triangle: ", triangle.get_perimetr())
###(╯°□°）╯︵ ┻━┻
print("S pentagon: ", pentagon.get_area())
print("P pentagon: ", pentagon.get_perimetr())
###(╯°□°）╯︵ ┻━┻
print("S hexagon: ", hexagon.get_area())
print("P hexagon: ", hexagon.get_perimetr())
###(╯°□°）╯︵ ┻━┻
print("S ellipse: ", ellipse.get_area())
print("P ellipse: ", ellipse.get_perimetr())
###(╯°□°）╯︵ ┻━┻