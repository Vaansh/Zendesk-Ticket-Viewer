from views.view import View


class Controller:
    def __init__(self):
        self.view = View()

    def start_application(self) -> None:
        self.render_header()
        self.render_menu()

    def render_header(self) -> None:
        self.view.render_header()

    def render_menu(self) -> None:
        self.view.render_menu()
