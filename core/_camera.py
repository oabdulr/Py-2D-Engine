from utilties._v2 import v2

class camera:
    def __init__(self, rad: int, position: v2 = v2(500, 500)) -> None:
        '''Cannot be asked to do math for a square view, a radius / distance check will do'''
        self.rad_view = rad
        self.__position = position

    
    def get_position(self) -> v2:
        return self.__position
    
    def set_position(self, pos: v2):
        self.__position = pos
    
    def set_rel_position(self, pos: v2):
        self.__position += pos
        print(self.__position)