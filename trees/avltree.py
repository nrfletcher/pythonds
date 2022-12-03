""" An AVL tree, otherwise known as a balanced binary tree, is a binary tree where
    a balance factor (typically -1 to 1 at most) is the max height difference between
    the left subtree of the root and the right subtree

    By implementing this data structure we prevent a traditional binary tree from
    running into runtime degradation, since an average runtime for searching is log n
    but in some circumstances it can degrade to n. An AVL tree prevents this by
    ensuring that with every new value added, it is done so in a balanced fashion """


class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, curr):
        if key < curr.key:
            if curr.has_left_child():
                self._put(key, val, curr.left_child)
            else:
                curr.left_child = TreeNode(key, val, parent=curr)
        else:
            if curr.has_right_child():
                self._put(key, val, curr.right_child)
            else:
                curr.right_child = TreeNode(key, val, parent=curr)
                
    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            ret = self._get(key, self.root)
            if ret:
                return ret.payload
            else:
                return None
        else:
            return None

    def _get(self, key, curr):
        if not curr:
            return None
        elif curr.key == key:
            return curr
        elif key < curr.key:
            return self._get(key, curr.left_child)
        else:
            return self._get(key, curr.right_child)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        if self._get(item, self.root):
            return True
        else:
            return False


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None, bf=0):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.balance_factor = bf

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, val, lc, rc):
        self.key = key
        self.payload = val
        self.right_child = rc
        self.left_child = lc
        if self.has_right_child():
            self.right_child.parent = self
        if self.has_left_child():
            self.left_child.parent = self
