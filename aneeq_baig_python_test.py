import json
import random


def parse(data) -> list:
    parsing = [row for row in data if 'function' in row and row['function'] == 'parse']
    return parsing


def copy(data) -> list:
    copying = [row for row in data if 'function' in row and row['function'] == 'copy']
    return copying


def functional(par: list, cop: list) -> list:
    func = []
    counter = 0
    for row in par:
        counter += 1
        new_row = row.copy()
        new_row['_list'] = 'parse'
        new_row['_counter'] = counter
        func.append(new_row)
    counter = 0
    for row in cop:
        counter += 1
        new_row = row.copy()
        new_row['_list'] = 'copy'
        new_row['_counter'] = counter
        func.append(new_row)
    return func


def random(data) -> list:
    rand = random.sample(data, 2)
    return rand


def main() -> (dict, dict, dict, dict,):
    # NOTE: Get all the parse commands
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
        par = parse(data)
        # NOTE: Get all the copy commands
        cop = copy(data)
        # NOTE: Put the two lists together and say which list it came from as well as the item number for that list
        fun = functional(par, cop)
        # NOTE: Get random sampling of data
        ran = random(data)

    return par, cop, fun, ran


if __name__ == '__main__':
    parse_commands, copy_commands, functional_commands, random_commands = main()

    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert functional_commands == [
        {'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1},
        {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(random_commands) == 2
