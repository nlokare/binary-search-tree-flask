class Node:
  def __init__(self, val):
    self.val = val
    self.left_child = None
    self.right_child = None

  def get(self):
    return self.val

  def set(self, val):
    self.val = val

  def get_children(self):
    children = []
    if self.left_child is not None:
      children.append(self.left_child)
    if self.right_child is not None:
      children.append(self.right_child)
    return children

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def _set_root(self, val):
    self.root = Node(val)

  def create_from_list(self, list_of_vals):
    for val in list_of_vals.split(','):
      if val.isdigit():
        self.insert(int(val))

  def insert(self, val):
    if self.root is None:
      self._set_root(val)
    else:
      self._insert_node(self.root, val)

  def _insert_node(self, current_node, val):
    if val < current_node.val:
      if current_node.left_child:
        self._insert_node(current_node.left_child, val)
      else:
        current_node.left_child = Node(val)
    else:
      if current_node.right_child:
        self._insert_node(current_node.right_child, val)
      else:
        current_node.right_child = Node(val)

  def find(self, val):
    return self._find_node(self.root, val)

  def _find_node(self, current_node, val):
    if current_node is None:
      return False
    elif val == current_node.val:
      return True
    elif val < current_node.val:
      return self._find_node(current_node.left_child, val)
    else:
      return self._find_node(current_node.right_child, val)

  def in_order(self, node):
    if node is None:
      return
    self.in_order(node.left_child)
    print(str(node.get()))
    self.in_order(node.right_child)

  def pre_order(self, node):
    if node is None:
      return
    print(str(node.get()))
    self.pre_order(node.left_child)
    self.pre_order(node.right_child)

  def post_order(self, node):
    if node is None:
      return
    self.post_order(node.left_child)
    self.post_order(node.right_child)
    print(str(node.get()))

  def sum_of_longest_path(self, node, sum_total, length, max_len, max_sum):
    if node is None:
      if max_len[0] < length:
        max_len[0] = length
        max_sum[0] = sum_total
      elif max_len[0] == length and max_sum[0] < sum_total:
        max_sum[0] = sum_total
      print(str(max_sum))
      return
    self.sum_of_longest_path(node.left_child, sum_total + node.get(), length + 1, max_len, max_sum)
    self.sum_of_longest_path(node.right_child, sum_total + node.get(), length + 1, max_len, max_sum)

  def max_sum(self):
    max_sum = [-9999999]
    max_len = [0]
    self.sum_of_longest_path(self.root, 0, 0, max_len, max_sum)
    return max_sum[0]
