import lib.helpers as helpers
import lib.ascii as render


class View:
    def __init__(self):
        pass

    def render_header(self) -> None:
        helpers.render(render.logo())
        helpers.render(render.application_name())
