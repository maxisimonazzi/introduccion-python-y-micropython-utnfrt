import framebuf


class MENU:

    def __init__(self, oled, internal_var=None):
        self.oled = oled
        self.width = oled.width
        self.height = oled.height
        self.justify = {"left": 0, "center": 1, "right": 2}
        self.font = None
        self.internal_var = internal_var

    def setFont(self, font):
        self.font = font._FONT

    def setInternalVar(self, var):
        self.internal_var = var

    def leftText(self, text, y, x_init=None):
        if x_init:
            x = x_init
        else:
            x = 0
        self.oled.text(text, x, y)

    def centerText(self, text, y, x_init=None):
        if x_init:
            x = int((x_init - len(text)*8)/2)
        else:
            x = int((self.width - len(text)*8)/2)

        self.oled.text(text, x, y)

    def rightText(self, text, y, x_init=None):
        if x_init:
            x = int((x_init - len(text)*8))
        else:
            x = int((self.width - len(text)*8))

        self.oled.text(text, x, y)

    def openIcon(self, icon_id):

        with open(f'icons/{icon_id}.pbm', "rb") as file:
            file.readline()
            file.readline()
            file.readline()
            icon = bytearray(file.read())

        return framebuf.FrameBuffer(icon, 128, 64, framebuf.MONO_HLSB)

    def infoIcon(self, icon_id, invert=False):
        info = []
        with open(f'icons/{icon_id}.pbm', "rb") as file:
            file.readline()
            xy = file.readline()
            x = int(xy.split()[0])
            y = int(xy.split()[1])
            icon = bytearray(file.read())

            if invert:
                for i in range(len(icon)):
                    icon[i] = ~icon[i]

            icon = framebuf.FrameBuffer(icon, x, y, framebuf.MONO_HLSB)
            info = [x, y, icon]

        return info

    def text(self, string, x0=0, y0=0, color=0xffff, bgcolor=0, colors=None):

        if self.font:
            buffer = self.oled
            font = self.font

            if colors is None:
                colors = (color, color, bgcolor, bgcolor)

            x = x0
            for c in string:

                if not ord(c) in font.keys():
                    c = "?"

                row = y0
                _w, * _font = font[ord(c)]
                for byte in _font:
                    unsalted = byte
                    for col in range(x, x + _w):
                        color = colors[unsalted & 0x03]
                        if color is not None:
                            buffer.pixel(col, row, color)
                        unsalted >>= 2
                    row += 1
                x += _w

        else:
            self.oled.text(string, x0, y0, color)


class MENU_OPTIONS(MENU):

    def __init__(self, oled, x_init=0, y_init=0, width_menu=128, height_option=8, partial_update=False):
        super().__init__(oled)
        self.options = []
        self.width = width_menu
        self.x_init = x_init
        self.y_init = y_init
        self.height = height_option
        self.in_menu = False
        self.partial_update = partial_update
        self.index_navigate_y = 0
        self.max_index_navigate_y = 0
        self.index_select = None

    def add_option(self, text: str, action: callable):
        self.options.append((text, action))
        self.max_index_navigate_y = len(self.options)-1

    def draw(self, width=None, height=None):

        if width == None:
            width = self.width

        if height == None:
            height = len(self.options)*8

        if self.partial_update:
            self.oled.fill_rect(
                self.x_init, self.y_init, width, height, 0)
        else:
            self.oled.fill(0)

        self.in_menu = True

        for i, item in enumerate(self.options):
            y = self.y_init + i*8
            if i == self.index_navigate_y:
                self.on_select(item[0], y)
            else:
                self.oled.text(item[0], self.x_init, y, 1)

        self.oled.show()

    def navigate_up(self):
        self.index_navigate_y -= 1
        if self.index_navigate_y < 0:
            self.index_navigate_y = 0

        if self.max_index_navigate_y == 0:
            return

        self.draw()

    def navigate_down(self):
        self.index_navigate_y += 1
        if self.index_navigate_y >= self.max_index_navigate_y:
            self.index_navigate_y = self.max_index_navigate_y

        if self.max_index_navigate_y == 0:
            return

        self.draw()

    def on_select(self, text, y):
        self.oled.fill_rect(self.x_init, y, self.width, self.height, 1)
        self.oled.text(text, self.x_init, y, 0)

    def select_option(self):
        self.in_menu = False
        action = self.options[self.index_navigate_y][1]
        action()


class MENU_ICONS(MENU):

    def __init__(self, oled, x_init=0, y_init=0, n_icons_x=1, n_icons_y=1, separate=0, partial_update=True):
        super().__init__(oled)
        self.options = []
        self.width = 0
        self.height = 0
        self.x_init = x_init
        self.y_init = y_init
        self.in_menu = False
        self.partial_update = partial_update
        self.index_navigate_x = 0
        self.index_navigate_y = 0
        self.max_index_navigate_x = n_icons_x - 1
        self.max_index_navigate_y = n_icons_y - 1
        self.separate = separate
        self.index_select = None

    def add_option(self, icon_name: str, action: callable, row: int, col: int):

        self.options.append((icon_name, action, row, col))
        self.get_dimensions_menu()

    def get_dimensions_menu(self):
        self.width = 0
        self.height = 0

        for option in self.options:
            icon_name = option[0]
            row = option[2]
            for _ in range(row):
                info = self.infoIcon(icon_name)
                self.width += info[0]

        for option in self.options:
            icon_name = option[0]
            col = option[3]
            for _ in range(col):
                info = self.infoIcon(icon_name)
                self.width += info[1]

    def draw(self):

        if self.partial_update:
            self.oled.fill_rect(
                self.x_init, self.y_init, self.width, self.height, 0)
        else:
            self.oled.fill(0)

        self.in_menu = True
        y_init = self.y_init
        x_init = self.x_init

        start = 0

        while start < len(self.options):

            for option in self.options[start:start + self.max_index_navigate_x+1]:
                name_icon = option[0]
                width, height, icon = self.infoIcon(name_icon)

                if self.index_navigate_x == option[2] and self.index_navigate_y == option[3]:
                    self.on_select(name_icon, x_init, y_init, width, height)

                else:
                    self.oled.blit(icon, x_init, y_init)

                x_init += width + self.separate

            x_init = 0
            y_init += height
            start += self.max_index_navigate_x+1

        self.oled.show()

    def navigate_up(self):
        self.index_navigate_y -= 1
        if self.index_navigate_y < 0:
            self.index_navigate_y = 0

        if self.max_index_navigate_y == 0:
            return

        self.draw()

    def navigate_down(self):
        self.index_navigate_y += 1
        if self.index_navigate_y >= self.max_index_navigate_y:
            self.index_navigate_y = self.max_index_navigate_y

        if self.max_index_navigate_y == 0:
            return

        self.draw()

    def navigate_left(self):
        self.index_navigate_x -= 1
        if self.index_navigate_x < 0:
            self.index_navigate_x = 0

        if self.max_index_navigate_x == 0:
            return

        self.draw()

    def navigate_right(self):
        self.index_navigate_x += 1
        if self.index_navigate_x >= self.max_index_navigate_x:
            self.index_navigate_x = self.max_index_navigate_x

        if self.max_index_navigate_x == 0:
            return

        self.draw()

    def on_select(self, icon_name, x_0, y_0, x_f, y_f,):
        self.oled.fill_rect(x_0, y_0, x_f, y_f, 1)
        icon = self.infoIcon(icon_name, invert=True)
        self.oled.blit(icon[2], x_0, y_0)

    def select_option(self):
        self.in_menu = False
        for option in self.options:
            if option[2] == self.index_navigate_x and option[3] == self.index_navigate_y:
                action = option[1]
                action()
                return


class NAVIGATE_MENU():
    def __init__(self, menu_list):
        self.menu_list = menu_list

    def navigate(self, direction: str):

        for menu in self.menu_list:
            if menu.in_menu:
                if direction == "up":
                    menu.navigate_up()
                    # print(menu.index_navigate_y)
                elif direction == "down":
                    menu.navigate_down()
                    # print(menu.index_navigate_y)
                elif direction == "left":
                    menu.navigate_left()
                    # print(menu.index_navigate_x)
                elif direction == "right":
                    menu.navigate_right()
                    # print(menu.index_navigate_x)
                else:
                    print("error de navegación")

    def select(self):

        for menu in self.menu_list:
            if menu.in_menu:
                menu.select_option()
                return

