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
            1: 'Enter ticket ID number',
        }
        self.tickets_options = {
            1: 'Previous page',
            2: 'Next page',
            3: 'Go back',
            4: 'Exit',
        }
        self.ticket_sub_options = {
            1: 'Enter another ticket ID number',
            2: 'Go back',
            3: 'Exit'
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

    def render_ticket_prompt_input(self) -> None:
        for ticket_option in self.ticket_options:
            helpers.render(self.ticket_options[ticket_option] + ":")

    def render_ticket_submenu(self) -> None:
        for ticket_sub_option in self.ticket_sub_options:
            print(str(ticket_sub_option),
                  self.ticket_sub_options[ticket_sub_option], sep=": ")

    def render_tickets_submenu(self) -> None:
        for tickets_option in self.tickets_options:
            print(str(tickets_option),
                  self.tickets_options[tickets_option], sep=": ")

    def render_exit_screen(self) -> None:
        helpers.render("Thank you for using this application.")

    def render_incorrect_input(self) -> None:
        helpers.render(
            "Your input was not recognized. Please ensure you enter the option presented correctly.")

    def render_incorrect_id(self) -> None:
        helpers.render("Invalid Id.")

    # def render_table():
