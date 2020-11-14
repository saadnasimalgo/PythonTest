import json
import random
import os
def main():
    # NOTE: Get all the parse commands
    parse_commands = []
    copy_commands = []
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
        load_parse_data = [parse_commands.append(row.copy()) for row in data 
                                                             if 'function' in row and row['function'] == 'parse']
        print(f"parse_commands: {parse_commands}")

    # NOTE: Get all the copy commands

    with open('data', 'r') as file:
        data = json.loads(file.read())
        load_copy_commands = [copy_commands.append(row.copy()) for row in data 
                                                               if 'function' in row and row['function'] == 'copy']
        print(f"copy_commands: {copy_commands}")

    # NOTE: Put the two lists together and say which list it came from as well as the item number for that list

    parse_commmands_verifier = len(parse_commands)
    copy_commands_verifier = len(parse_commmands_verifier)
    functional_commands = []
    counter = 0
    if parse_commmands_verifier > 0:
        for row in parse_commands:
            counter += 1
            new_row = row.copy()
            new_row['_list'] = 'parse'
            new_row['_counter'] = counter
            functional_commands.append(new_row)
        counter = 0

    if copy_commands_verifier > 0:
        for row in copy_commands:
            counter += 1
            new_row = row.copy()
            new_row['_list'] = 'copy'
            new_row['_counter'] = counter
            functional_commands.append(new_row)
        print(f"functional_commands: {functional_commands}")

    # NOTE: Get random sampling of data
    random_commands = []
    with open('data', 'r') as file:
        data = json.loads(file.read())
        random_commands_data = random.sample(data, 2)
        random_commands.append(random_commands_data)
    print(f"random_commands: {random_commands}")

    return parse_commands, copy_commands, functional_commands, random_commands


if __name__ == '__main__':
    parse_commands, copy_commands, functional_commands, random_commands = main()

    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(random_commands) == 2
