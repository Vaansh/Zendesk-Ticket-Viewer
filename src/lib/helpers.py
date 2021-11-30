import os


def get_credentials(path: str) -> list:
    file = open(path)
    data = json.load(file)
    user, password, domain, api_token = data["username"], data["password"], data["domain"], data["api_token"]
    file.close()
    return [user, password, domain, api_token]


def get_string_from_text_file(path: str) -> str:
    file = open(path)
    return file.read()


def render(string_to_render: str, align_to_center: bool = False) -> None:
    print(string_to_render.center(os.get_terminal_size().columns)
          if align_to_center else string_to_render)
