import lib.helpers as helpers
import lib.ascii as render


class View:
    def __init__(self):
        self.display_message = "Please Enter a Number from the Menu:"
        self.menu_options = {
            1: 'View all tickets',
            2: 'View a ticket',
            3: 'Exit',
        }

    def render_header(self) -> None:
        helpers.render(render.logo())
        helpers.render(render.application_name())
        helpers.render("\n:=== MAIN MENU OPTIONS ===:\n")

    def render_menu(self) -> None:
        helpers.render(self.display_message)

        for menu_option in self.menu_options:
            print(str(menu_option), self.menu_options[menu_option], sep=": ")

    # def render_table():
