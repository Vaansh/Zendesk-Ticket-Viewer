import os
import json

from typing import List
from prettytable import prettytable


def get_credentials(path: str) -> dict:
    file = open(path)
    data = json.load(file)
    credentials = {}
    credentials["username"], credentials["password"], credentials["subdomain"], credentials[
        "api_token"] = data["username"], data["password"], data["subdomain"], data["api_token"]
    file.close()
    return credentials


def get_string_from_text_file(path: str) -> str:
    file = open(path)
    return file.read()


def render(string_to_render: str, align_to_center: bool = False) -> None:
    print(string_to_render.center(os.get_terminal_size().columns)
          if align_to_center else string_to_render)


def render_ticket(json_list: List[str]) -> None:
    table = PrettyTable("Requested Ticket:")

    for json in json_list:
        table.add_row(
            json["id"],
            json["subject"],
            json["status"],
            json["created_at"],
            json["description"]
        )

    self.render(table)
