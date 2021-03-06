import json
import os
from typing import List

from models.ticket import Ticket
from prettytable import PrettyTable


def get_credentials(path: str) -> dict:
    file = open(path)
    data = json.load(file)
    credentials = {}
    credentials["username"], credentials["password"], credentials["subdomain"], = (
        data["username"],
        data["password"],
        data["subdomain"],
    )
    file.close()
    return credentials


def get_string_from_text_file(path: str) -> str:
    file = open(path)
    return file.read()


def render(string_to_render: str, align_to_center: bool = False) -> None:
    print(string_to_render.center(os.get_terminal_size().columns) if align_to_center else string_to_render)


def render_table(tickets: List[Ticket], page: int = None, page_count: int = None) -> None:
    table = PrettyTable(["ID", "Subject", "Status", "Created At"])

    table.hrules = 1
    table.vrules = 1
    table.header = True

    for ticket in tickets:
        table.add_row(
            [
                ticket.id,
                ticket.subject,
                ticket.status,
                ticket.created_at,
            ]
        )

    render(table)
    render(("Page number: " + str(page) + "/" + str(page_count) + "\n") if (page and page_count) else ("\n"))
