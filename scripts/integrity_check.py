#!/usr/bin/env python3
import os
import subprocess

def run_integrity_check():
    print("--- Integrity Audit Started ---")
    # Verify git status
    res = subprocess.run(["git", "status"], capture_output=True, text=True)
    if "working tree clean" in res.stdout:
        print("[PASS] Git working tree clean.")
    else:
        print("[WARN] Git working tree dirty!")
    
    # Check for secrets (very basic check)
    forbidden = ["ghp_", "hf_", "sk-"]
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == ".gitignore": continue
            try:
                with open(os.path.join(root, file), 'r', errors='ignore') as f:
                    content = f.read()
                    for fbd in forbidden:
                        if fbd in content:
                            print(f"[CRITICAL] Potential secret in {os.path.join(root, file)}")
            except: pass
    print("--- Integrity Audit Finished ---")

if __name__ == "__main__":
    run_integrity_check()
