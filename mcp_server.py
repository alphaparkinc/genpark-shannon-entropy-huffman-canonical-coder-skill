import sys
import json
from client import HuffmanCoder

def main():
    coder = HuffmanCoder()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "entropy":
            e = coder.entropy(params.get("text", ""))
            res = {"entropy": e}
        elif method == "codes":
            tree = coder.build_tree(params.get("text", ""))
            c = coder.generate_codes(tree)
            res = {"codes": c}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
