import lib.helpers as helpers


def logo() -> str:
    return helpers.get_string_from_text_file("src/lib/data/logo.txt")


def application_name() -> str:
    return helpers.get_string_from_text_file("src/lib/data/application_name.txt")
