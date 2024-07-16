from DepthFirstSearch.interface.views.dfs_view import DFSView


class DFSController:
    def __init__(self, root, tree):
        self.tree = tree
        self.view = DFSView(root, self.tree)


