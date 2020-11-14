import json
import random

functional_commands = []
def main() -> (dict, dict, dict, dict, ):
    # NOTE: Get all the parse commands
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    for row in data:
        if 'function' in row and row['function'] == 'parse':
            parse_commands=row
        if 'function' in row and row['function'] == 'copy':
            copy_commands=row

    print(f"parse_commands: {parse_commands}")
    print(f"copy_commands: {copy_commands}")

    random_commands = random.sample(data, 2)
    print("Printing random commands : ", random_commands)

    parse_commands_ap = parse_commands
    parse_commands_ap['_list'] = 'parse'
    parse_commands_ap['_counter'] = 1
    copy_commands_ap = copy_commands
    copy_commands_ap['_list'] = 'copy'
    copy_commands_ap['_counter'] = 1


    functional_commands.append(parse_commands_ap)
    functional_commands.append(copy_commands_ap)
    print("Printing Funcitonal commands : ", functional_commands)
    return parse_commands, copy_commands, functional_commands, random_commands

if __name__ == '__main__':
    parse_commands, copy_commands, functional_commands, random_commands = main()

    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1},
                                   {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(random_commands) == 2


    # assert parse_commands == {'function': 'parse', 'help': 'file help', 'value': 'file'} # list (dictionary within a list)
    nn = {'function': 'copy', 'help': 'copy help', 'value': 'file'}
    print(type(copy_commands), type(nn))
    # assert copy_commands <= nn
    assert copy_commands == nn
    assert copy_commands == {'function': 'copy', 'help': 'copy help', 'value': 'file'}