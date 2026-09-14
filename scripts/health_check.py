#!/usr/bin/env python3
import urllib.request
import json
import sys

def check_9router():
    try:
        req = urllib.request.Request("http://localhost:20128/v1/models")
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode())
            print("[PASS] 9Router is reachable at http://localhost:20128")
            return True
    except Exception as e:
        print(f"[FAIL] 9Router unreachable: {e}")
        return False

if __name__ == "__main__":
    ok = check_9router()
    sys.exit(0 if ok else 1)
