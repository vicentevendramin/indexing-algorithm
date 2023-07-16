from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.list = list()

    def __len__(self):
        return len(self.list)

    def enqueue(self, value):
        return self.list.append(value)

    def dequeue(self):
        if len(self.list) == 0:
            return None
        return self.list.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self.list) or len(self.list) == 0:
            raise IndexError('Índice Inválido ou Inexistente')
        return self.list[index]
