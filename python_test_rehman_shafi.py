import json
import random


class Test:
    def main(self):
        data = self._read_file('data.txt')
        copy_commands = self._get_data('copy', data)
        copy_commands = [dict(item, **{'_list': 'copy', '_counter': idx+1})
                         for idx, item in copy_commands]

        print(f"copy_commands: {copy_commands}")

        parse_commands = self._get_data('parse', data)
        parse_commands = [dict(item, **{'_list': 'parse', '_counter': idx+1})
                          for idx, item in parse_commands]

        print(f"parse_commands: {parse_commands}")

        functional_commands = [*copy_commands, *parse_commands]

        random_commands = self._get_data(None, data)
        print(f"random_commands: {random_commands}")

        return parse_commands, copy_commands, functional_commands, random_commands

    def _read_file(self, file_name: str):
        with open(file_name, 'r') as file:
            return json.loads(file.read())
        return None

    def _get_data(self, value: str = None, data=None):
        return [x for x in data if x['value'] == value] if value else random.sample(data, 2)


if __name__ == '__main__':
    parse_commands, copy_commands, functional_commands, random_commands = Test().main()

    assert parse_commands == [
        {'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert copy_commands == [
        {'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {
        'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(random_commands) == 2
