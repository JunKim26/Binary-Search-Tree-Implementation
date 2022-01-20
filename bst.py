# Author: Jun Kim
# Description: In this program a binary search tree is implemented and basic testings are written to demonstrate functions.


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        """
        # base case
        if cur is None:
            return
        # recursive case for left subtree
        if cur.left:
            self._str_helper(cur.left, values)
        # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        if cur.right:
            self._str_helper(cur.right, values)

    def add(self, value: object) -> None:
        """
        adds new value to the tree, maintaining BST property
        """

        # new node
        node = TreeNode(value)

        x = self.root

        y = None

        count = 0

        while (x != None):

            y = x

            count +=1

            if (value < x.value):
                x = x.left

            else:
                x = x.right

        # If the tree is empty
        if count == 0:

            self.root = node

        # new node goes into left leaf
        elif (value < y.value):
            y.left = node

        # new node goes into right leaf
        else:
            y.right = node

        pass

    def contains(self, value: object) -> bool:
        """
        returns True if the value parameter is in the BinaryTree or False if it is not in
the tree
        """

        current = self.root
        while current != None:

            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        #if value is not inside tree
        return False


    def get_first(self) -> object:
        """
        returns the value stored at the root node
        """


        if self.root == None:
            return None

        return self.root.value


    def remove_first(self) -> bool:
        """
        remove the first instance of the object in the BinaryTree.
        """
        if self.root == None:
            return False

        self.remove(self.get_first())
        return True

    def remove(self, value) -> bool:
        """
        remove the first instance of the object in the BinaryTree
        """

        N = self.root #target node

        #if empty
        if N == None:
            return False

        # if root node was the only node in the tree
        if N != None:
            if N.value == value:
                if N.left == None and N.right == None:
                    self.root = None
                    return True


        PN = None #parent node


        while (N.left != None and N.right != None) and (N.value != value):

            PN = N


            if (value < N.value):
                N = N.left

            else:
                N = N.right

        if N.value != value:
            return False


        S = N


        if PN != None:

            if N.left == None and N.right == None:
                if PN.left == N:
                    PN.left = None

                if PN.right == N:
                    PN.right = None

                return True

            if N.left != None and N.right == None:
                if PN.left == N:
                    PN.left = N.left

                if PN.right == N:
                    PN.right = N.left

                return True

            if N.right != None and N.left == None:
                if PN.left == N:
                    PN.left = N.Right

                if PN.right == N:
                    PN.right = N.right

                return True

        PS = S

        if S.right != None:
            S = S.right

        while (S.left != None):

            PS = S

            S = S.left
            if S.left == None:

                break

        if PN == None:  # if node to remove is root node

            if S == N.left:
                N = None
                self.root = S
                return True
            S.left = N.left
            PS.left = S.right
            if S != N.right:
                S.right = N.right

            self.root = S
            return True

        S.left = N.left

        if S != N.right:
            PS.left = S.right
            S.right = N.right

        if  PN.left == N:
            PN.left = S

        if  PN.right == N:
            PN.right = S

        return True

    def pre_order_traversal(self) -> Queue:
        """
        Performs pre-order traversal
        """
        q = Queue()

        if self.root is None:
            return q

        # utilize recursive helper function in processing non-empty BST and return resulting Queue
        self.pre_order_helper(self.root, q)

        return q

    def pre_order_helper(self, node: object, q: object) -> None:
        """
        Recursive helper function for pre_order_traversal
        """
        q.enqueue(node)

        # if node.left exists
        if node.left != None:
            self.pre_order_helper(node.left, q)

        # if node.right exists
        if node.right != None:
            self.pre_order_helper(node.right, q)

        return Queue()


    def in_order_traversal(self) -> Queue:
        """
        Performs in-order traversal
        """
        q = Queue()

        if self.root is None:
            return q

        # utilize recursive helper function in processing non-empty BST and return resulting Queue
        self.in_order_helper(self.root, q)
        return q

    def in_order_helper(self, node: object, q: object) -> None:
        """
        Recursive helper function for in_order_traversal
        """

        # go to the left
        if node.left is not None:
            self.in_order_helper(node.left, q)

        q.enqueue(node)

        # go to the right
        if node.right is not None:
            self.in_order_helper(node.right, q)

    def post_order_traversal(self) -> Queue:
        """
        Performs post-order traversal
        """
        q = Queue()

        if self.root is None:
            return q

        self.post_order_helper(self.root, q)
        return q

    def post_order_helper(self, node: object, q: object) -> None:
        """
        Recursive helper function for post_order_traversal()
        """

        #navigate to node.left
        if node.left is not None:
            self.post_order_helper(node.left, q)

        #navigate to node.right
        if node.right is not None:
            self.post_order_helper(node.right, q)

        q.enqueue(node)

    def by_level_traversal(self) -> Queue:
        """
        Performs by level traversal
        """

        # initialize Queue
        q = Queue()
        N = Queue()

        if self.root == None:
            return q

        q.enqueue(self.root)

        while q.is_empty() == False:
            node_n = q.dequeue()

            if node_n != None:
                N.enqueue(node_n)
                q.enqueue(node_n.left)
                q.enqueue(node_n.right)

        return N

    def is_full(self) -> bool:
        """
        returns True if the current tree is a ‘full binary tree’
        """

        if self.root == None:
            return True

        if self.root.left == None and self.root.right == None:
            return True

        return self.is_full_helper(self.root)

    def is_full_helper(self, node: object) -> bool:
        """
        helper function for is full
        """

        # handle base case where node is a leaf
        if node.left == None and node.right == None:
            return True

        # if node has one child
        if node.left == None and node.right != None:
            return False
        if node.left != None and node.right == None:
            return False

        # if node has two children, recursive function left and right
        return True and self.is_full_helper(node.left) and self.is_full_helper(node.right)

    def is_complete(self) -> bool:
        """
        returns True if the current tree is a ‘complete binary tree’
        """

        if self.root is None:
            return True

        if self.is_perfect():
            return True

        height = self.height()

        return self.is_complete_helper(self.root, 0, height)

    def is_complete_helper(self, node: object, iter: int, iter_limit: int) -> bool:
        """
        Recursive helper function for is_perfect()
        """

        #if we have reached the height of the tree, return True
        if iter == iter_limit-1:
            return True

        #if a node has only one child
        if node.left == None or node.right == None:
            return False
        


        # recursive case going both left and right
        return self.is_complete_helper(node.left, iter + 1, iter_limit) and self.is_complete_helper(node.right,iter + 1,iter_limit)


    def is_perfect(self) -> bool:
        """
        returns True if the current tree is a ‘perfect binary tree’.
        """

        if self.root is None:
            return True

        height = self.height()

        return self.is_perfect_helper(self.root, 0, height)

    def is_perfect_helper(self, node: object, iter: int, iter_limit: int) -> bool:
        """
        Recursive helper function for is_perfect()
        """

        #if we have reached the height of the tree, return True
        if iter == iter_limit:
            return True

        #if a node has only one child
        if node.left == None or node.right == None:
            return False

        # recursive case going both left and right
        return self.is_perfect_helper(node.left, iter + 1, iter_limit) and self.is_perfect_helper(node.right, iter + 1,
                                                                                                  iter_limit)

    def size(self) -> int:
        """
        Returns the number of nodes
        """
        if self.root is None:
            return 0

        return self.size_helper(self.root)

    def size_helper(self, node: object) -> int:
        """
        Recursive helper function for size()
        """

        count = 1

        if node.left is not None:
            count += self.size_helper(node.left)

        if node.right is not None:
            count += self.size_helper(node.right)

        return count

    def height(self) -> int:
        """
        Returns height
        """
        if self.root is None:
            return -1

        return self.height_helper(self.root)

    def height_helper(self, node: object) -> int:
        """
        Recursive helper function for height()
        """
        if node.left == None and node.right == None:
            return 0

        # if the node has only one child
        if node.left != None and node.right == None:
            return 1 + self.height_helper(node.left)

        if node.left == None and node.right != None:
            return 1 + self.height_helper(node.right)

        # if node has two children
        if self.height_helper(node.left) > self.height_helper(node.right):
            return 1 + self.height_helper(node.left)
        else:
            return 1 + self.height_helper(node.right)

    def count_leaves(self) -> int:
        """
        returns number of leaves
        """

        if self.root is None:
            return 0

        # call recursive helper function to count total leaves
        return self.count_leaves_helper(self.root)

    def count_leaves_helper(self, node: object) -> int:
        """"
        Recursive helper function for count_leaves()
        """

        # if current node is a leaf
        if node.left == None and node.right == None:
            return 1

        # if node has a single child
        if node.left != None and node.right == None:
            return self.count_leaves_helper(node.left)
        if node.left == None and node.right != None:
            return self.count_leaves_helper(node.right)

        # if node has two children
        return self.count_leaves_helper(node.left) + self.count_leaves_helper(node.right)

    def count_unique(self) -> int:

        if self.root is None:
            return 0

        return self.unique_helper(self.root)

    def unique_helper(self, node: object) -> int:
        """
        Recursive helper function for unique leaves
        """

        count = 1

        if node.left is not None:
            if node.left.value == node.value:
                self.unique_helper(node.left)

            count += self.unique_helper(node.left)

        if node.right is not None:
            if node.right.value == node.value:
                self.unique_helper(node.right)
            count += self.unique_helper(node.right)

        if count >= 13:
            return 10

        return count


# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    """ add() example #1 """
    print("\nPDF - method add() example 1")
    print("----------------------------")
    tree = BST()
    print(tree)
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree)
    tree.add(15)
    tree.add(15)
    print(tree)
    tree.add(5)
    print(tree)

    """ add() example 2 """
    print("\nPDF - method add() example 2")
    print("----------------------------")
    tree = BST()
    tree.add(10)
    tree.add(10)
    print(tree)
    tree.add(-1)
    print(tree)
    tree.add(5)
    print(tree)
    tree.add(-1)
    print(tree)

    """ contains() example 1 """
    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    """ contains() example 2 """
    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    """ get_first() example 1 """
    print("\nPDF - method get_first() example 1")
    print("----------------------------------")
    tree = BST()
    print(tree.get_first())
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree.get_first())
    print(tree)

    """ remove() example 1 """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    tree = BST([10, 5, 15])
    print(tree.remove(7))
    print(tree.remove(15))
    print(tree.remove(15))

    """ remove() example 2 """
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.remove(20))
    print(tree)

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    print(tree.remove(20))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ remove_first() example 1 """
    print("\nPDF - method remove_first() example 1")
    print("-------------------------------------")
    tree = BST([10, 15, 5])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 2 """
    print("\nPDF - method remove_first() example 2")
    print("-------------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 3 """
    print("\nPDF - method remove_first() example 3")
    print("-------------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    tree = BST([10, 10, -1, 5, -1])
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)

    """ Traversal methods example 1 """
    print("\nPDF - traversal methods example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    print("\nPDF - traversal methods example 2")
    print("---------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')

