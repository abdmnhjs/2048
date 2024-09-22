import pygame as pg

class Bloc:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__number = 2
        self.__width = width
        self.__height = height
        self.__color = None
        self.__rect = None
        self.__living = True

    def inTheGrind(self):
        return 0 <= self.__x <= 375 and 0 <= self.__y <= 375

    def collisionRight(self, bloc):
        if self.__x + self.__width == bloc.__x and self.__y == bloc.__y:
            return True
        return False

    def collisionLeft(self, bloc):
        if self.__x == bloc.__x + bloc.__width and self.__y == bloc.__y:
            return True
        return False

    def collisionUp(self, bloc):
        if self.__y == bloc.__y + bloc.__height and self.__x == bloc.__x:
            return True
        return False

    def collisionDown(self, bloc):
        if self.__y + self.__height == bloc.__y and self.__x == bloc.__x:
            return True
        return False

    def canFuseRight(self, bloc):
        return self.collisionRight(bloc) and self.__number == bloc.getNumber()

    def canFuseLeft(self, bloc):
        return self.collisionLeft(bloc) and self.__number == bloc.getNumber()

    def canFuseDown(self, bloc):
        return self.collisionDown(bloc) and self.__number == bloc.getNumber()

    def canFuseUp(self, bloc):
        return self.collisionUp(bloc) and self.__number == bloc.getNumber()

    def fuseRight(self, bloc):
        if self.canFuseRight(bloc):
            self.__x = bloc.__x
            self.__number += bloc.getNumber()

    def fuseLeft(self, bloc):
        if self.canFuseLeft(bloc):
            self.__x = bloc.__x
            self.__number += bloc.getNumber()

    def fuseDown(self, bloc):
        if self.canFuseDown(bloc):
            self.__y = bloc.__y
            self.__number += bloc.getNumber()

    def fuseUp(self, bloc):
        if self.canFuseUp(bloc):
            self.__y = bloc.__y
            self.__number += bloc.getNumber()

    def moveRight(self, blocs):
        while self.inTheGrind() and self.__x + self.__width <= 375:
            collision = False
            for bloc in blocs:
                if self.collisionRight(bloc):
                    if self.canFuseRight(bloc):
                        self.fuseRight(bloc)
                        bloc.__living = False
                    collision = True
                    break
            if collision:
                break
            self.__x += 125

    def moveLeft(self, blocs):
        while self.inTheGrind() and self.__x - self.__width >= 0:
            collision = False
            for bloc in blocs:
                if self.collisionLeft(bloc):
                    if self.canFuseLeft(bloc):
                        self.fuseLeft(bloc)
                        bloc.__living = False
                    collision = True
                    break
            if collision:
                break
            self.__x -= 125

    def moveUp(self, blocs):
        while self.inTheGrind() and self.__y - self.__height >= 0:
            collision = False
            for bloc in blocs:
                if self.collisionUp(bloc):
                    if self.canFuseUp(bloc):
                        self.fuseUp(bloc)
                        bloc.__living = False
                    collision = True
                    break
            if collision:
                break
            self.__y -= 125

    def moveDown(self, blocs):
        while self.inTheGrind() and self.__y + self.__height <= 375:
            collision = False
            for bloc in blocs:
                if self.collisionDown(bloc):
                    if self.canFuseDown(bloc):
                        self.fuseDown(bloc)
                        bloc.__living = False
                    collision = True
                    break
            if collision:
                break
            self.__y += 125

    def initSquare(self, window):
        if self.__number == 2:
            self.setColor((50, 100, 255))
        elif self.__number == 4:
            self.setColor((100, 150, 255))
        elif self.__number == 8:
            self.setColor((150, 200, 255))
        elif self.__number == 16:
            self.setColor((200, 220, 255))
        elif self.__number == 32:
            self.setColor((255, 220, 220))
        elif self.__number == 64:
            self.setColor((255, 180, 180))
        elif self.__number == 128:
            self.setColor((255, 140, 140))
        elif self.__number == 256:
            self.setColor((255, 100, 100))
        elif self.__number == 512:
            self.setColor((255, 80, 80))
        elif self.__number == 1024:
            self.setColor((255, 50, 50))
        elif self.__number == 2048:
            self.setColor((255, 0, 0))
        else:
            self.setColor((200, 200, 200))

        self.__rect = pg.Rect(self.__x, self.__y, self.__width, self.__height)
        pg.draw.rect(window, self.__color, self.__rect)

        font = pg.font.SysFont(None, 48)
        text = font.render(str(self.__number), True, (255, 255, 255))
        text_rect = text.get_rect(center=self.__rect.center)

        window.blit(text, text_rect)

    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getColor(self):
        return self.__color
    def getNumber(self):
        return self.__number
    def getRect(self):
        return self.__rect
    def isLiving(self):
        return self.__living

    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y
    def setColor(self, color):
        self.__color = color
    def setNumber(self, number):
        self.__number = number