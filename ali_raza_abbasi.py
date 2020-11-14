import json
import random
import pytest

def append_commands(row, counter, value):
    new_row = row.copy()
    new_row['_list'] = value
    new_row['_counter'] = counter
    return new_row


def main() -> (dict, dict, dict, dict, ):
    # NOTE: Get all the parse commands
    with open('./data.txt', 'r') as file:
        data = json.loads(file.read())

    parse_commands = [row for row in data if 'function' in row and row['function'] == 'parse']
    print(f"parse_commands: {parse_commands}")

    # NOTE: Get all the copy commands
    copy_commands = [row for row in data if 'function' in row and row['function'] == 'copy']
    print(f"copy_commands: {copy_commands}")

    # NOTE: Put the two lists together and say which list it came from as well as the item number for that list
    functional_commands = [append_commands(row, index+1, 'parse') for index, row in enumerate(parse_commands)]
    functional_commands += [append_commands(row, index+1, 'copy') for index, row in enumerate(copy_commands)]

    print(f"functional_commands: {functional_commands}")

    # NOTE: Get random sampling of data
    random_commands = random.sample(data, 2)
    print(f"random_commands: {random_commands}")

    return parse_commands, copy_commands, functional_commands, random_commands

# parameterized test case
@pytest.mark.parametrize("test_input,expected")
def test_eval(test_input, expected):
    assert eval(str(test_input)) == expected


if __name__ == '__main__':
    parse_commands, copy_commands, functional_commands, random_commands = main()
    
    test_eval(parse_commands, [{'function': 'parse', 'help': 'file help', 'value': 'file'}])
    test_eval(copy_commands, [{'function': 'copy', 'help': 'copy help', 'value': 'file'}])
    test_eval(functional_commands, [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}])
    test_eval(len(random_commands), 2)

    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(random_commands) == 2
