import math
import pandas as pd
from operator import itemgetter

class DecisionTree:
    def __init__(self, df, target, positive, parent_val, parent):
        self.data = df
        self.target = target
        self.positive = positive
        self.parent_val = parent_val
        self.parent = parent
        self.childs = []
        self.decision = ''

    def _get_entropy(self, data):
        p = sum(data[self.target] == self.positive)
        n = data.shape[0] - p
        p_ratio = p / (p + n) if (p + n) != 0 else 0
        n_ratio = n / (p + n) if (p + n) != 0 else 0
        entropy_p = -p_ratio * math.log2(p_ratio) if p_ratio != 0 else 0
        entropy_n = -n_ratio * math.log2(n_ratio) if n_ratio != 0 else 0
        return entropy_p + entropy_n

    def _get_gain(self, feat):
        avg_info = 0
        for val in self.data[feat].unique():
            subset = self.data[self.data[feat] == val]
            avg_info += self._get_entropy(subset) * (len(subset) / len(self.data))
        return self._get_entropy(self.data) - avg_info

    def _get_splitter(self):
        self.splitter = max(self.gains, key=itemgetter(1))[0]

    def update_nodes(self):
        self.features = [col for col in self.data.columns if col != self.target]
        self.entropy = self._get_entropy(self.data)
        if self.entropy != 0:
            self.gains = [(feat, self._get_gain(feat)) for feat in self.features]
            self._get_splitter()
            residual_columns = [k for k in self.data.columns if k != self.splitter]
            for val in self.data[self.splitter].unique():
                df_tmp = self.data[self.data[self.splitter] == val][residual_columns]
                tmp_node = DecisionTree(df_tmp, self.target, self.positive, val, self.splitter)
                tmp_node.update_nodes()
                self.childs.append(tmp_node)

    def print_tree(self):
        for child in self.childs:
            if child:
                print(f"{child.parent} = {child.parent_val}")
                child.print_tree()

df = pd.read_csv('PlayTennis.csv')  # Ensure this CSV file is available in the same directory
dt = DecisionTree(df, 'Play Tennis', 'Yes', '', '')
dt.update_nodes()
dt.print_tree()