
class Node():
    """Klasa punktu"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Zwraca scieżkę od punktu startowego do docelowego"""

    # Tworzenie punktu początkowego oraz docelowego
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Inicjalizacja otwartej oraz zamkniętej listy
    open_list = []
    closed_list = []

    # Dodanie punktu startowego do listy otwartej
    open_list.append(start_node)

    while len(open_list) > 0:

        # aktualny punkt
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Usuwa aktualny punkt z listy otwartych i dodaje do zamkniętych
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Punkt docelowy znaleziony
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Zwraca odwróconą scieżkę

        # Tworzy potomków
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Sąsiadujące punkty

            # Pozycja punktu
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Sprawdzamy czy znajduje się na mapie
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Czy można się poruszyć na tę pozycje
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Tworzenie nowego punktu
            new_node = Node(current_node, node_position)

            # Dodanie
            children.append(new_node)

        for child in children:

            # Potomek należy do zamkniętych
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Obliczamy wartość f
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Potomek należy do otwartych
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Dodanie potomka do otwartych
            open_list.append(child)


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()
