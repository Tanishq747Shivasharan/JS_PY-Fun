import random
import string

RESET  = "\033[0m"
BOLD   = "\033[1m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
YELLOW = "\033[93m"
MAGENTA= "\033[95m"
DIM    = "\033[2m"
RED    = "\033[91m"

def generate_key(length: int) -> str:
    """Generate a random one-time key of same length as plaintext."""
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def vernam_encrypt(plaintext: str, key: str) -> list:
    """Encrypt via bitwise XOR on ASCII values. Returns list of ints."""
    return [ord(p) ^ ord(k) for p, k in zip(plaintext, key)]

def vernam_decrypt(cipher_vals: list, key: str) -> str:
    """Decrypt by XOR-ing again with the same key (XOR is self-inverse)."""
    return ''.join(chr(c ^ ord(k)) for c, k in zip(cipher_vals, key))

def banner():
    print(f"""
{CYAN}{BOLD}╔══════════════════════════════════════════════════╗
║         VERNAM  CIPHER  —  ONE-TIME  PAD         ║
╚══════════════════════════════════════════════════╝{RESET}
""")

def show_table(plaintext, key, cipher_vals, decrypted):
    col = 9
    print(f"{BOLD}  {'Char':<7}{'P(ord)':<{col}}{'K(ord)':<{col}}{'C=P⊕K':<{col}}{'Hex':<{col}}{'Dec'}{RESET}")
    print(f"  {'─' * 52}")
    for p, k, c, d in zip(plaintext, key, cipher_vals, decrypted):
        ok = f"{GREEN}✔{RESET}" if d == p else f"{RED}✘{RESET}"
        print(
            f"  {YELLOW}{p}{RESET} ⊕ {MAGENTA}{k}{RESET}   "
            f"{ord(p):<{col}}{ord(k):<{col}}"
            f"{CYAN}{c:<{col}}{RESET}"
            f"{DIM}0x{c:03X}{RESET}    "
            f"{GREEN}{d}{RESET} {ok}"
        )
    print()

def main():
    banner()

    plaintext = "NETWORK"
    print(f"  {BOLD}Plaintext      :{RESET}  {YELLOW}{plaintext}{RESET}")

    key = generate_key(len(plaintext))
    print(f"  {BOLD}Key (random)   :{RESET}  {MAGENTA}{key}{RESET}\n")

    cipher_vals = vernam_encrypt(plaintext, key)

    print(f"  {BOLD}Cipher (int)   :{RESET}  {CYAN}{' '.join(str(v) for v in cipher_vals)}{RESET}")
    print(f"  {BOLD}Cipher (hex)   :{RESET}  {CYAN}{' '.join(f'0x{v:03X}' for v in cipher_vals)}{RESET}\n")

    decrypted = vernam_decrypt(cipher_vals, key)
    print(f"  {BOLD}Decrypted      :{RESET}  ", end="")
    if decrypted == plaintext:
        print(f"{GREEN}{BOLD}{decrypted}  ✔  Integrity confirmed{RESET}\n")
    else:
        print(f"{RED}{decrypted}  ✘  Mismatch!{RESET}\n")

    print(f"{BOLD}  ── Step-by-step XOR breakdown ──{RESET}\n")
    show_table(plaintext, key, cipher_vals, decrypted)

    print(f"{DIM}  ── How It Works ────────────────────────────────────")
    print(f"  Encrypt : C = P XOR K   (bitwise XOR on ASCII values)")
    print(f"  Decrypt : P = C XOR K   (XOR is its own inverse)")
    print()
    print(f"  ── Security Properties ─────────────────────────────")
    print(f"  • Key length must equal plaintext length ({len(key)} chars)")
    print(f"  • Key is used exactly once — never reused")
    print(f"  • Information-theoretically secure (Shannon, 1949)")
    print(f"  • Without key, ciphertext leaks zero information{RESET}\n")

if __name__ == "__main__":
    main()