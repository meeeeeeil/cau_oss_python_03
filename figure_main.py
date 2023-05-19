# %%

# [fill this line]

myline = figure.line(10)

square = figure.area_square(myline.get_length())
print(square)

myline.set_length(20)
regular_triangle = figure.area_regular_triangle(myline.get_length())
print(regular_triangle)

myline.set_length(30)
circle = figure.area_circle(myline.get_length())
print(circle)