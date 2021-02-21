"""                           Estrutura de Dados:
Estrutura de Dados: É o bloco fundamental da ciência da computação e engenharia
de software.
                                   Definição
É um modo particular de armazenamento e organização de dados em um computador para
que possam ser utilzados de maneira eficiente.

                                   Algoritmo
Sequência finita de regras, raciocínios ou operação que aplicado a um conjunto de
dados permite solucionar uma determinada classe de problemas.

                            Eficiência ou Complexidade
O quão bem você utiliza os seus recuros para realizar uma tarefa (Conservação).

                                BIG O Notation
É um mode de classificar o algoritmo pelo seu tempo de execução ou espaço acupado
conforme o nosso input autmenta.
"""

class Node:

    def __int__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
            
        current_node.next = new_node
        return

    def length(self):
        if self.head == None:
            return 0
        current_node = self.head
        total = 0

        while current_node:
            total += 1
            current_node = current_node.next
        return total
    
    def to_list(self):
        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
        return node_data

    def display(self):
        contents = self.head

        if contents is None:
            print("Lista has no element")

            while contents:
                print (contents.data)
                contents = contents.next
            print("--------")

    def reverse_linkedlist(self):
        previous_node = None
        current_node = self.head
        while current_node != None:
            next = current_node.next
            current_node.next = previous_node
            previuous_node = current_node
            current_node = next
        self.head = previous_node

# Test

my_list = LinkedList()
my_list.display()

my_list.append(3)
my_list.append(7)
my_list.append(2)
my_list.append(1)

my_list.display()



print("The total number of of elements are:" + str(my_list.length()))
print(my_list.to_list())
print("-------")

