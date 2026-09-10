from client import HuffmanCoder

def main():
    print("=== Testing Shannon Entropy & Huffman Coder ===")
    coder = HuffmanCoder()
    text = "ABBCCCDDDD"
    ent = coder.entropy(text)
    print(f"Shannon Entropy: {ent:.3f} bits/symbol")
    assert ent > 0

    tree = coder.build_tree(text)
    codes = coder.generate_codes(tree)
    print("Huffman Codebook:", codes)
    assert len(codes) == 4
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
