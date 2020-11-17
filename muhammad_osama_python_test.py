import json
import random


def open_file():
    """ opening file """
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    return data


def parse_command():
    """
        parse command code first method with list comprehension
    """
    parse_commands = []
    [parse_commands.append(row.copy()) for row in open_file() if 'function' in row and row['function'] == 'parse']
    return parse_commands


def copy_command():
    """ use copy commands method"""
    copy_commands = []
    [copy_commands.append(row.copy()) for row in open_file() if 'function' in row and row['function'] == 'copy']
    return copy_commands


def functional_command():
    """ putting together functional command"""
    functional_commands = []
    counter = 0
    for row in parse_command():
        counter += 1
        new_row = row.copy()
        new_row['_list'] = 'parse'
        new_row['_counter'] = counter
        functional_commands.append(new_row)
    counter = 0
    for row in copy_command():
        counter += 1
        new_row = row.copy()
        new_row['_list'] = 'copy'
        new_row['_counter'] = counter
        functional_commands.append(new_row)

    return functional_commands


def random_command():
    """ putting random command in method"""
    # random_commands = []
    random_commands = random.sample(open_file(), 2)
    return random_commands


def main() -> (dict, dict, dict, dict, ):

    # NOTE: Get all the parse commands
    parse_commands = parse_command()
    print(f"parse_commands: {parse_commands}")

    # NOTE: Get all the copy commands
    copy_commands = copy_command()
    print(f"copy_commands: {copy_commands}")

    # NOTE: Put the two lists together and say which list it came from as well as the item number for that list
    merge_list = [
        {"parse_list": parse_commands,
         "copy_list": copy_commands}
    ]
    print(f" Putting list together: {merge_list}")

    # INFO : Moved functional command in a method
    functional_commands = functional_command()
    print(f"functional_commands: {functional_commands}")

    # NOTE: Get random sampling of data
    random_commands = random_command()
    print(f"random_commands: {random_commands}")

    return parse_commands, copy_commands, functional_commands, random_commands


if __name__ == '__main__':
    parse_commands, copy_commands, functional_commands, random_commands = main()

    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(random_commands) == 2
