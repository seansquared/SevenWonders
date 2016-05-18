import abc

class Card(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def type(self):
        return

    def cost(self):
        return

    def state(self):
        return 