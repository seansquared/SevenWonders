import abc

class Card(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def name(self):
        return

    def cost(self):
        return

    def state(self):
        return