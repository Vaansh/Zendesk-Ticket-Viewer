import helpers
from views.view import View
from models.requestor import Requestor


class Controller:
    def __init__(self):
        self.view = View()
        self.requestor = Requestor(
            helpers.get_credentials("credentials/credentials.json"))
        self.selected_option = ""

    def start_application(self) -> None:
        self.render_header()

        while self.selected_option != "3":
            self.render_menu()
            self.selected_option = input()

            # if selected_option == "1":

            # if selected_option == "2":

    def render_header(self) -> None:
        self.view.render_header()

    def render_menu(self) -> None:
        self.view.render_menu()
