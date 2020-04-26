from wakeonlan import send_magic_packet
from serialize import load, dump

class Waker(object):

    def __init__(self, path):
        self.path = path
        self.ip_dict = self.load_ip_dict()

    def load_ip_dict(self):
        if self.path.exists():
            return load(str(self.path))
        else:
            return {}

    def dump_ip_dict(self):
        dump(self.ip_dict, str(self.path))

    def add_ip(self, name, ip):
        self.ip_dict.update({name: ip})
        print(self.ip_dict)
        self.dump_ip_dict()
        return "Added %s:%s to IP memory" % (name, ip)

    def wake(self, name):
        send_magic_packet(self.ip_dict[name])
        return "I sent magic packet to %s" % self.ip_dict[name]

    def list_instructions(self):
        my_instructions = {
            'remember': self.add_ip,
            'wake': self.wake
        }

        return my_instructions
