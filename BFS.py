class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Graph:
    # Ο κατασκευαστής προετοιμάζει ένα κενό λεξικό
    def __init__(self):
        self.al = {}

    " Προσθέτω έναν κόμβο στο γράφημα με την μορφή ενός ζεύγους (κλειδί, τιμή). Το κλειδί είναι ο ίδιος ο κόμβος και η τιμή είναι η λίστα των κόμβων στους οποίους είναι δυνατή η πρόσβαση από αυτόν τον κόμβο. "

    def addNode(self, node, lst):
        self.al[node] = lst

    " bfs & nodes"
    def bfs(self, node):
        print (node.name)
        level = {node: 0}
        
        " Το επίπεδο είναι ένα λεξικό που περιέχει όλους τους κόμβους που επισκέφτηκε και τα επίπεδά τους. Αυτό το λεξικό αναζητείται κάθε φορά που θέλουμε να δούμε αν έχει γίνει επίσκεψη σε έναν κόμβο."

        neighbors = {node: None}

        i = 1  # i κρατά τα levels 

        queue = [node]
        
        " Αυτό θα εκχωρείται ως νέα λίστα σε κάθε επανάληψη. Αυτό θα έχει κ την λίστα των κόμβων δίπλα στον τρέχοντα κόμβο έως ότου κανένας κόμβος δεν μείνει χωρίς επίσκεψη."

        while queue:
            next_node = []
            
            "Το next_node είναι μια προσωρινή λίστα για τη διατήρηση των τιμών που θα γίνουν από το επόμενο que."
 
            for x in queue:
                for v in self.al[x]:
                    if v not in level:
                        print (v.name)
                        level[v] = i
                        neighbors [v] = x
                        next_node.append(v)

            queue = next_node
            i += 1
        return level


if __name__ == '__main__':
    A = Node('A', 1)
    B = Node('B', 2)
    C = Node('C', 3)
    D = Node('D', 4)
    E = Node('E', 5)

    #Γράφος edges
    g = Graph()
    g.addNode(A, [B])
    g.addNode(B, [C])
    g.addNode(C, [D])
    g.addNode(D, [E])
    g.addNode(E, [E])

    g.bfs(A)


 

    #spyrogamiese
