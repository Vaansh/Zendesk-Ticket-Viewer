import utils.helpers as helpers


def logo() -> str:
    return helpers.get_string_from_text_file("utils/data/logo.txt")


def application_name() -> str:
    return helpers.get_string_from_text_file("utils/data/application_name.txt")
