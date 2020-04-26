from serialize import load

from abilities.waker import Waker


class Adjutant(object):

    def __init__(self, path):
        self.path = path
        self.memory = self.load_memory()
        self.abilities = {'waker': Waker(path.joinpath('waker_ip_dict.json'))}
        self.instructions = self.load_instructions()

    def parse_order(self, text):
        text = text.split(' ')
        text = text[1:-1]
        print(text)
        if text[0] in self.instructions.keys():
            try:
                return self.instructions[text[0]](*text[1:])
            except:
                return "I could not execute your order"
        else:
            return "I could not understand your order"

    def load_memory(self):
        return load(str(self.path.joinpath('memory.json')))

    def load_instructions(self):
        instructions = {}
        for ability, executor in self.abilities.items():
            instructions.update(executor.list_instructions())

        return instructions
