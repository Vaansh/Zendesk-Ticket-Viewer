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
        self.ticket_options = {
            1: 'Enter ticket number',
            2: 'Go back',
            3: 'Exit',
        }
        self.tickets_options = {
            1: 'Previous page',
            2: 'Next page',
            3: 'Go back',
            4: 'Exit',
        }

    def render_header(self, main_menu_header: bool = True) -> None:
        helpers.render(render.logo())
        helpers.render(render.application_name())
        if main_menu_header:
            helpers.render("\n:=== MAIN MENU OPTIONS ===:\n")

    def render_menu(self) -> None:
        helpers.render(self.display_message)
        for menu_option in self.menu_options:
            print(str(menu_option), self.menu_options[menu_option], sep=": ")

    def render_ticket_submenu(self) -> None:
        for ticket_option in self.ticket_options:
            print(str(ticket_option),
                  self.ticket_options[ticket_option], sep=": ")

    def render_exit_screen(self) -> None:
        print("Thank you for using this application.")

    def render_incorrect_input(self) -> None:
        print("Your input was not recognized. Please ensure you enter the option presented correctly.")

    # def render_table():
