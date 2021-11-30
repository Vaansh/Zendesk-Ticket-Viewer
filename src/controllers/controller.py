import sys

import lib.helpers as helpers
from views.view import View
from models.requestor import Requestor


class Controller:
    def __init__(self):
        self.view = View()
        self.credentials = helpers.get_credentials(
            "credentials/credentials.json")
        self.requestor = Requestor(
            self.credentials["username"],
            self.credentials["password"],
            self.credentials["subdomain"])

    def start_application(self) -> None:
        self.render_header()

        selected_option = ""

        while selected_option != "3":
            self.render_menu()
            selected_option = input()

            if selected_option == "1":
                self.handle_tickets_request()

            elif selected_option == "2":
                self.handle_ticket_request()

            else:
                self.render_incorrect_input()

        self.exit_application()

    # TODO: code to render multiple tickets + flip through pages

    def handle_ticket_request(self) -> None:
        selected_ticket_option = ""

        while selected_ticket_option != "3":
            self.render_ticket_submenu()
            selected_ticket_option = input()

            if selected_ticket_option == "1":
                # TODO: user input for ticket
                print(self.requestor.request())

            elif selected_ticket_option == "2":
                break

            elif selected_ticket_option == "3":
                self.exit_application()

            else:
                self.render_incorrect_input()

    def handle_tickets_request(self) -> None:
        selected_tickets_option = ""

        while selected_tickets_option != "4":
            self.render_tickets_submenu()
            selected_tickets_option = input()

            if selected_tickets_option == "1":
                # TODO: user input for tickets [prev page]
                print(self.requestor.request())

            elif selected_tickets_option == "2":
                # TODO: user input for tickets [next page]
                print(self.requestor.request())

            elif selected_tickets_option == "3":
                break

            elif selected_tickets_option == "4":
                self.exit_application()

            else:
                self.render_incorrect_input()

    def render_header(self) -> None:
        self.view.render_header()

    def render_menu(self) -> None:
        self.view.render_menu()

    def render_ticket_submenu(self) -> None:
        self.view.render_ticket_submenu()

    def render_tickets_submenu(self) -> None:
        self.view.render_tickets_submenu()

    def render_exit_screen(self) -> None:
        self.view.render_exit_screen()

    def render_incorrect_input(self) -> None:
        self.view.render_incorrect_input()

    def exit_application(self) -> None:
        self.render_exit_screen()
        sys.exit()
