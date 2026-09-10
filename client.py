import math

class HuffmanNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoder:
    """
    Shannon Entropy & Huffman Prefix Coding Engine.
    Constructs minimum redundancy tree graphs.
    """
    def entropy(self, text):
        if not text:
            return 0.0
        freqs = {}
        for c in text:
            freqs[c] = freqs.get(c, 0) + 1
        n = len(text)
        return -sum((cnt / n) * math.log2(cnt / n) for cnt in freqs.values())

    def build_tree(self, text):
        freqs = {}
        for c in text:
            freqs[c] = freqs.get(c, 0) + 1
        nodes = [HuffmanNode(c, f) for c, f in freqs.items()]
        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.freq)
            left = nodes.pop(0)
            right = nodes.pop(0)
            parent = HuffmanNode(None, left.freq + right.freq, left, right)
            nodes.append(parent)
        return nodes[0] if nodes else None

    def generate_codes(self, root, prefix="", codes=None):
        if codes is None:
            codes = {}
        if root:
            if root.char is not None:
                codes[root.char] = prefix or "0"
            self.generate_codes(root.left, prefix + "0", codes)
            self.generate_codes(root.right, prefix + "1", codes)
        return codes
