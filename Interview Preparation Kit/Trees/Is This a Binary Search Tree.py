def isBST(node, mini, maxi):

    if node is None:
        return True

    if node.data < mini or node.data > maxi:
        return False

    return (isBST(node.left, mini, node.data - 1) and
          isBST(node.right, node.data + 1, maxi))

def checkBST(root):
    return isBST(root, 0, 10000)