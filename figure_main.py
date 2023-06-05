# %%

"""
area_rectangle, area_right_triangle, area_ellipse 함수들에서
예외 발생 시 0이하의 값은 입력할 수 없습니다를 출력하도록 변경!
"""
class line:
    """
    line class는 선의 길이들에 대해 저장하고 있는 클래스이다.
    변수로는 외부에서 접근 불가능한 __width와 __height가 있으며,
    해당 변수를 수정하고 접근하기 위해
    set_length와, get_length 메소드를 제공한다.
    """
    __width = 0
    __height = 0
    def __init__(self, width, height):
        """ 생성자 초기 width와 height 값을 입력
        Args:
            width   (int or float): 초기 선의 가로 길이
            height  (int or float): 초기 선의 세로 길이
        """
        self.__width = width
        self.__height = height

    def set_length(self, width, height):
        """선의 길이를 수정
        Args:
            width   (int or float): 수정하고자 하는 가로 길이
            height  (int or float): 수정하고자 하는 세로 길이
        """
        self.__width = width
        self.__height = height

    def get_length(self):
        """객체가 저장하고 있는 선의 길이를 반환
        Returns:
            int or float: 저장하고 있는 서느이 길이
        """
        return self.__width, self.__height
    
    def area_rectangle(width, height):
        """ 길이를 입력받아 직사각형의 넓이를 구하는 함수
        Args:
            width   (int or flaot): 밑변의 길이
            height  (int or float): 높이의 길이
        Returns:
            int or float: 직사각형의 넓이를 반환
        """
        if width <= 0 or height <=0: raise ValueError
        return width * height
    
    def area_ellipse(width, height):
        """길이를 입력받아 타원의 넓이를 구하는 함수
        Args:
            width   (int or float): 짧은쪽 반지름 길이
            height  (int or float): 긴쪽 반지름 길이
        Returns:
            int or float: 직각삼각형의 넓이를 반환
        """
        if width <= 0 or height <= 0: raise ValueError
        return width * height / 2
    
import figure

myline = figure.line(10, 20)

width, height = myline.get_length()
try:
    rectangle = figure.area_rectangle(width, height)
    print(rectangle)
except ValueError:
    pritn("please input positive number for width and height")
# implement exception handler
rectangle = figure.area_rectangle(width, height)
print(rectangle)

myline.set_length(20, 30)
width, height = myline.get_length()
# implement exception handler
triangle = figure.area_right_triangle(width, height)
print(triangle)

myline.set_length(30, 40)
width, height = myline.get_length()
# implement exception handler
ellipse = figure.area_ellipse(width, height)
print(ellipse)