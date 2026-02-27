import hashlib
import os
import pyfiglet

def compute_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def verify_hash(text, encode):
    computed = compute_hash(text)
    return computed == expected.lower().strip(), computed

def hash_file(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def main():
    banner = pyfiglet.figlet_format("SHA-256 HASH TOOL (CLI)")
    print(banner)

    while True:
        print("OPTIONS:")
        print("  [1] Compute hash of a message")
        print("  [2] Verify integrity of a message")
        print("  [3] Hash a file")
        print("  [4] Exit\n")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            text = input("Enter message: ")
            print(f"\n  SHA-256 → {compute_hash(text)}\n")
        elif choice == '2':
            text = input("Enter message: ")
            expected = input("Enter expected hash: ")
            match, computed = verify_hash(text, expected)
            print(f"\n  Computed → {computed}")
            if match:
                print("  ✔  MATCH — Integrity verified.\n")
            else:
                print("  ✗  MISMATCH — Data may be tampered.\n")
        elif choice == '3':
            path = input("Enter file path: ").strip()
            if os.path.exists(path):
                print(f"\n  SHA-256 → {hash_file(path)}\n")
            else:
                print("\n  Error: File not found.\n")
        elif choice == '4':
            print("\nExiting. Goodbye!\n")
            break
        else:
            print("\n  Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
