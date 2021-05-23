 class Observavel:
    def __init__(self):
        self._observers = []

    def registrar_observador(self, observer):
        self._observers.append(observer)

    def remover_observador(self, observer):
        self._observers.remove(observer)

    def notificar_observadores(self, data):
        for observer in self._observers:
            observer.atualizar(self, data)