class Pilha:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def reverter_string(string):
    pilha = Pilha()
    for caractere in string:
        pilha.push(caractere)

    string_invertida = ""
    while not pilha.is_empty():
        string_invertida += pilha.pop()

    return string_invertida


# Testando o programa
entrada = input("Digite uma string: ")
string_invertida = reverter_string(entrada)
print("String invertida:", string_invertida)
