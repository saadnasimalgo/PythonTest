import json
import random
import pytest

class Commands:
    def __init__(self,file_name,random_index):
        with open(file_name,'r') as file:
            self.data = json.loads(file.read())

        #Initializing the commands
        self.parse_commands = []
        self.copy_commands = []
        self.functional_commands = []
        self.random_commands = []

        #Populating the commands
        self.create_parse_commands()
        self.create_copy_commands()
        self.create_functional_commands()
        self.create_random_commands(random_index)

    def create_parse_commands(self):
        self.parse_commands = [row.copy() for row in self.data if 'function' in row and row['function'] == 'parse']
        print(f"parse_commands: {self.parse_commands}")

    def create_copy_commands(self):
        self.copy_commands = [row.copy() for row in self.data if 'function' in row and row['function'] == 'copy']
        print(f"copy_commands: {self.copy_commands}")

    def create_random_commands(self, random_index):
        self.random_commands = random.sample(self.data, random_index)
        print(f"random_commands: {self.random_commands}")

    def create_functional_commands(self):
        #This is still a better approach, for better readability and understanding
        counter = 0
        for row in self.parse_commands:
            counter += 1
            new_row = row.copy()
            new_row['_list'] = 'parse'
            new_row['_counter'] = counter
            self.functional_commands.append(new_row)
        counter = 0
        for row in self.copy_commands:
            counter += 1
            new_row = row.copy()
            new_row['_list'] = 'copy'
            new_row['_counter'] = counter
            self.functional_commands.append(new_row)
        print(f"functional_commands: {self.functional_commands}")
class Test:
    def __init__(self,file_name,random_index):
        self.random_index = random_index
        self.test_cmds = Commands(file_name,random_index)
    def test_parse(self,cmd,parse_cmds):
        assert self.test_cmds.parse_commands==parse_cmds
    def test_copy(self,copy_cmds):
        assert self.test_cmds.copy_commands==copy_cmds

    def test_functional(self,functional_cmds):
        assert self.test_cmds.functional_commands==functional_cmds
    def test_random(self,num):
        assert len(self.test_cmds.random_commands)==self.random_index

def main(file_name,random_index) -> (Commands, ):
    # NOTE: Create Commands Object
    cmds = Commands(file_name=file_name,random_index=random_index)
    return cmds

if __name__ == '__main__':
    random_index = 1
    file_name = 'data.txt'
    cmds = main(file_name,random_index)
    assert cmds.parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert cmds.copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert cmds.functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(cmds.random_commands) == random_index
