import os

"""Listkeeper_ans.py

    Manage lists from the files.

"""

__author__ = "maydee"


def menu():
    """Shows the menu and receives the users answer.
    """
    pass


def choice(item_list, is_changed):
    """Searches for the filename file or asks to create new one."""
    pass


def add_element(item_list, is_changed):
    """Add an element to the list"""
    pass


def del_element(item_list, is_changed):
    """Delete an element from the list."""
    pass


def load_item_list(filename):
    """Load the list from the file."""
    pass


def print_list(item_list):
    """Print the list to the console."""
    pass


def save_item_list(filename, item_list, stop_after_save = False):
    """Save the list to the filename file."""
    file = None
    try:
        file = open(filename, 'w', encoding='utf-8')
        file.write("\n".join(item_list))
        file.write("\n")
    except EnvironmentError as err:
        print("Error! Failed to save {filename}: {err}")
    else:
        print("Saved {0} item{1} to {2}".format(len(item_list),'s' if len(item_list) > 1 else '', filename))
        if not stop_after_save:
            print("Press Enter to continue...")
    finally:
        if file is not None:
            file.close()


def get_string(message, name="string", default=None,
               minimum_length=0, maximum_length=80):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length == 0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(
                                     name))
            if not (minimum_length <= len(line) <= maximum_length):
                raise ValueError("{name} must have at least "
                        "{minimum_length} and at most "
                        "{maximum_length} characters".format(
                        **locals()))
            return line
        except ValueError as err:
            print("ERROR", err)


def get_integer(message, name="integer", default=None, minimum=0,
                maximum=100, allow_zero=True):

    class RangeError(Exception): pass

    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = int(line)
            if i == 0:
                if allow_zero:
                    return i
                else:
                    raise RangeError("{0} may not be 0".format(name))
            if not (minimum <= i <= maximum):
                raise RangeError("{name} must be between {minimum} "
                        "and {maximum} inclusive{0}".format(
                        " (or 0)" if allow_zero else "", **locals()))
            return i
        except RangeError as err:
            print("ERROR", err)
        except ValueError as err:
            print("ERROR {0} must be an integer".format(name))


def main():
    pass

main()