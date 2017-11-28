import pygame

class Button:

    mark = 10

    def __init__(self, text = "", mainColor = (220, 220, 220), borderColor = (0, 0, 0), hoverColor = (172, 220, 247), xPos = 10, yPos = 30, width = None, height = 20):
        self.text = text
        self.xPos = xPos
        self.yPos = yPos
        self.height = height
        self.mainColor = mainColor
        self.borderColor = borderColor
        self.hoverColor = hoverColor
        self.fontName = "Arial"
        self.fontSize = self.height - 6
        self.mouseOver = False
        self.mouseDown = False
        self.mouseState = "off"
        self.clicked = False
        self.pyg = pygame
        self.font = self.pyg.font.SysFont(self.fontName, self.fontSize)
        self.text_width, self.text_height = self.pyg.font.Font.size(self.font, self.text)

        if width == None:
            self.width = self.text_width + 20
            self.width_type = "text"
        else:
            self.width = width
            self.width_type = "user"

        self.buttonUpSurface = self.pyg.Surface((self.width, self.height))
        self.buttonDownSurface = self.pyg.Surface((self.width, self.height))
        self.buttonHoverSurface = self.pyg.Surface((self.width, self.height))
        self.__update__()

    def __update__(self):

        # How should the button look like when the user is performing a keyUp event on this button
        self.buttonUpSurface.fill(self.mainColor)
        self.pyg.draw.line(self.buttonUpSurface, self.borderColor, (2, 0), (self.width - 3, 0), 1)
        self.pyg.draw.line(self.buttonUpSurface, self.borderColor, (2, self.height - 1), (self.width - 3, self.height - 1), 1)
        self.pyg.draw.line(self.buttonUpSurface, self.borderColor, (0, 2), (0, self.height - 3), 1)
        self.pyg.draw.line(self.buttonUpSurface, self.borderColor, (self.width - 1, 2), (self.width - 1, self.height - 3), 1)
        self.buttonUpSurface.blit(self.font.render(self.text, False, (0, 0, 0)),
                                  ((self.width / 2) - (self.text_width / 2), (self.height / 2) - (self.text_height / 2)))

        # How should the button look like when the user is hovering his cursor over the button
        self.buttonHoverSurface.fill(self.hoverColor)
        self.pyg.draw.line(self.buttonHoverSurface, self.borderColor, (2, 0), (self.width - 3, 0), 1)
        self.pyg.draw.line(self.buttonHoverSurface, self.borderColor, (2, self.height - 1), (self.width - 3, self.height - 1), 1)
        self.pyg.draw.line(self.buttonHoverSurface, self.borderColor, (0, 2), (0, self.height - 3), 1)
        self.pyg.draw.line(self.buttonHoverSurface, self.borderColor, (self.width - 1, 2), (self.width - 1, self.height - 3), 1)
        self.buttonHoverSurface.blit(self.font.render(self.text, False, (0, 0, 0)),
                                     ((self.width / 2) - (self.text_width / 2), (self.height / 2) - (self.text_height / 2)))

        # How should the button look like when the user is holding his button down on it
        r, g, b = self.hoverColor
        self.buttonDownSurface.fill((r - 20, g - 20, b - 10))
        self.pyg.draw.line(self.buttonDownSurface, self.borderColor, (2, 0), (self.width - 3, 0), 1)
        self.pyg.draw.line(self.buttonDownSurface, (r - 20, g - 20, b - 10), (2, 1), (self.width - 3, 1), 2)
        self.pyg.draw.line(self.buttonDownSurface, self.borderColor, (2, self.height - 1), (self.width - 3, self.height - 1), 1)
        self.pyg.draw.line(self.buttonDownSurface, self.borderColor, (0, 2), (0, self.height - 3), 1)
        self.pyg.draw.line(self.buttonDownSurface, (r - 20, g - 20, b - 10), (1, 2), (1, self.height - 3), 2)
        self.pyg.draw.line(self.buttonDownSurface, self.borderColor, (self.width - 1, 2), (self.width - 1, self.height - 3), 1)
        self.buttonDownSurface.blit(self.font.render(self.text, False, (0, 0, 0)),
                                    ((self.width / 2) - (self.text_width / 2) + 1, (self.height / 2) - (self.text_height / 2)))

    def draw(self, surface):
        self.__mouse_check__()
        if self.mouseState == "hover":
            surface.blit(self.buttonHoverSurface, (self.xPos, self.yPos))
        elif self.mouseState == "off":
            surface.blit(self.buttonUpSurface, (self.xPos, self.yPos))
        elif self.mouseState == "down":
            surface.blit(self.buttonDownSurface, (self.xPos, self.yPos))

    def __mouse_check__(self):
        _1, _2, _3 = self.pyg.mouse.get_pressed()
        mouse_x, mouse_y = self.pyg.mouse.get_pos()
        if not _1:
            self.mouseState = "off"
        if mouse_x > self.xPos and mouse_x < self.xPos + self.width and mouse_y > self.yPos and mouse_y < self.yPos + self.height and not self.mouseState == "down":
            self.mouseState = "hover"
        if not self.mouseDown and _1 and self.mouseState == "hover":
            self.mouseState = "down"
            self.clicked = True
        if self.mouseState == "off":
            self.clicked = False

    def click(self):
        _1, _2, _3 = self.pyg.mouse.get_pressed()
        mouse_x, mouse_y = self.pyg.mouse.get_pos()
        if mouse_x > self.xPos and mouse_x < self.xPos + self.width and mouse_y > self.yPos and mouse_y < self.yPos + self.height and self.clicked and not _1:
            self.clicked = False
            return True
        else:
            return False

    def set_text(self, text, fontname="Arial", fontsize=None):
        self.text = text
        self.fontName = fontname
        if not fontsize == None:
            self.fontSize = fontsize
        self.font = self.pyg.font.SysFont(self.fontName, self.fontSize)
        self.text_width, self.text_height = self.pyg.font.Font.size(self.font, self.text)
        if self.width_type == "text":
            self.width = self.text_width + 20
        self.buttonUpSurface = self.pyg.Surface((self.width, self.height))
        self.buttonDownSurface = self.pyg.Surface((self.width, self.height))
        self.buttonHoverSurface = self.pyg.Surface((self.width, self.height))
        self.__update__()