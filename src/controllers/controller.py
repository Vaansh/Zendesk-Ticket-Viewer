import sys
import lib.helpers as helpers
from views.view import View
from models.requestor import Requestor
from models.ticket import Ticket
from typing import Any, List


class Controller:
    def __init__(self):
        self.view = View()
        self.credentials = helpers.get_credentials("credentials/credentials.json")
        self.requestor = Requestor(
            self.credentials["username"], self.credentials["password"], self.credentials["subdomain"]
        )

    def start_application(self) -> None:
        self.render_header()

        selected_option = ""

        while selected_option != "3":
            self.render_menu()
            selected_option = self.receive_input()

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
        self.render_ticket_prompt_input()
        selected_ticket_option = self.receive_input()
        self.request(selected_ticket_option)
        self.handle_subticket_request()

    def handle_tickets_request(self) -> None:
        selected_tickets_option = ""
        page_number = 1

        while selected_tickets_option != "4":
            self.render_tickets_submenu()
            selected_tickets_option = self.receive_input()

            if selected_tickets_option == "1":
                # TODO: user input for tickets [prev page]
                page_number -= 1
                print(self.requestor.request())
            elif selected_tickets_option == "2":
                # TODO: user input for tickets [next page]
                page_number += 1
                print(self.requestor.request())
            elif selected_tickets_option == "3":
                break
            elif selected_tickets_option == "4":
                self.exit_application()
            else:
                self.render_incorrect_input()

    def handle_subticket_request(self) -> None:
        subticket_option = ""
        self.render_ticket_submenu()

        subticket_option = self.receive_input()
        if subticket_option == "1":
            self.handle_ticket_request()
        elif subticket_option == "2":
            return
        elif subticket_option == "3":
            self.exit_application()
        else:
            self.render_incorrect_input()

    def request(self, ticket_id: str) -> None:
        ticket = self.requestor.request(ticket_id)

        if ticket:
            if type(ticket) is str:
                self.handle_request_error(ticket)
            else:
                self.render_table(ticket)
        else:
            self.render_incorrect_id()

    def handle_request_error(self, ticket: str) -> None:
        if ticket == "err_api_unavailable":
            self.render_error_api_unavailable()
        elif ticket == "err_bad_request":
            self.render_error_bad_request()
        else:
            self.render_unkown_error()

    def receive_input(self) -> Any:
        user_input = input()
        helpers.render("")
        return user_input

    def render_header(self) -> None:
        self.view.render_header()

    def render_menu(self) -> None:
        self.view.render_menu()

    def render_ticket_prompt_input(self) -> None:
        self.view.render_ticket_prompt_input()

    def render_table(self, tickets: List[Ticket]) -> None:
        self.view.render_table(tickets)

    def render_ticket_submenu(self) -> None:
        self.view.render_ticket_submenu()

    def render_tickets_submenu(self) -> None:
        self.view.render_tickets_submenu()

    def render_incorrect_input(self) -> None:
        self.view.render_incorrect_input()

    def render_exit_screen(self) -> None:
        self.view.render_exit_screen()

    def render_unkown_error(self) -> None:
        self.view.render_unkown_error()

    def render_error_api_unavailable(self) -> None:
        self.view.render_error_api_unavailable()

    def render_error_bad_request(self) -> None:
        self.view.render_error_bad_request()

    def render_incorrect_id(self) -> None:
        self.view.render_incorrect_id()

    def exit_application(self) -> None:
        self.render_exit_screen()
        sys.exit()
