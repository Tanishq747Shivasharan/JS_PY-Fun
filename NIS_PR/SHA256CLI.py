import hashlib
import os
import sys

def hash_text(text: str) -> str:
    """Return the SHA-256 hex digest of a UTF-8 string."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def hash_file(filepath: str) -> str:
    """Return the SHA-256 hex digest of a file (streamed in chunks)."""
    sha = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha.update(chunk)
    return sha.hexdigest()

def verify(data: str, expected_hash: str, is_file: bool = False) -> bool:
    """Compare the computed hash against an expected value."""
    computed = hash_file(data) if is_file else hash_text(data)
    return computed == expected_hash.strip().lower()

RESET  = "\033[0m"
BOLD   = "\033[1m"
GREEN  = "\033[92m"
RED    = "\033[91m"
CYAN   = "\033[96m"
YELLOW = "\033[93m"
DIM    = "\033[2m"

def banner():
    print(f"""
        {CYAN}{BOLD}╔══════════════════════════════════════════════╗
        ║        SHA-256  INTEGRITY  TOOL              ║
        ╚══════════════════════════════════════════════╝{RESET}
            """)

def menu():
    print(f"""  {YELLOW}[1]{RESET} Hash text input
  {YELLOW}[2]{RESET} Hash a file
  {YELLOW}[3]{RESET} Verify text against a known hash
  {YELLOW}[4]{RESET} Verify file against a known hash
  {YELLOW}[0]{RESET} Exit
""")

def print_hash(digest: str, label: str = "SHA-256"):
    half = len(digest) // 2
    print(f"\n  {DIM}{label}:{RESET}")
    print(f"  {CYAN}{digest[:half]}{RESET}")
    print(f"  {CYAN}{digest[half:]}{RESET}\n")


def print_result(match: bool, computed: str):
    if match:
        print(f"\n  {GREEN}{BOLD} INTEGRITY VERIFIED — hashes match.{RESET}")
    else:
        print(f"\n  {RED}{BOLD} INTEGRITY FAILED — hashes do NOT match.{RESET}")
    print_hash(computed, "Computed hash")

def action_hash_text():
    text = input(f"  {BOLD}Enter text:{RESET} ")
    digest = hash_text(text)
    print_hash(digest)

def action_hash_file():
    path = input(f"  {BOLD}File path:{RESET} ").strip()
    if not os.path.isfile(path):
        print(f"\n  {RED}File not found: {path}{RESET}\n")
        return
    digest = hash_file(path)
    print_hash(digest, f"SHA-256  [{os.path.basename(path)}]")

def action_verify_text():
    text     = input(f"  {BOLD}Enter text:{RESET} ")
    expected = input(f"  {BOLD}Expected hash:{RESET} ").strip()
    computed = hash_text(text)
    print_result(computed == expected.lower(), computed)

def action_verify_file():
    path     = input(f"  {BOLD}File path:{RESET} ").strip()
    expected = input(f"  {BOLD}Expected hash:{RESET} ").strip()
    if not os.path.isfile(path):
        print(f"\n  {RED}File not found: {path}{RESET}\n")
        return
    computed = hash_file(path)
    print_result(computed == expected.lower(), computed)

def main():
    banner()
    actions = {
        "1": action_hash_text,
        "2": action_hash_file,
        "3": action_verify_text,
        "4": action_verify_file,
    }
    while True:
        menu()
        choice = input(f"  {BOLD}Choose an option:{RESET} ").strip()
        print()
        if choice == "0":
            print(f"  {DIM}Goodbye.{RESET}\n")
            sys.exit(0)
        elif choice in actions:
            actions[choice]()
        else:
            print(f"  {YELLOW}Invalid option. Please try again.{RESET}\n")

if __name__ == "__main__":
    main()