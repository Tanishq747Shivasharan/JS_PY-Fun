from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return private_key, private_key.public_key()

def sign(private_key, message: bytes) -> bytes:
    return private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )

def verify(public_key, message: bytes, signature: bytes) -> bool:
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        return True
    except InvalidSignature:
        return False

def main():
    print("Generating RSA-2048 key pair...")
    private_key, public_key = generate_keys()
    print("Keys generated.\n")

    message = b"This message will be digitally signed."
    print(f"Message: {message.decode()}\n")

    print("Signing message with private key...")
    signature = sign(private_key, message)
    print(f"Signature ({len(signature)} bytes): {signature.hex()[:64]}...\n")

    # Verify the original message
    result = verify(public_key, message, signature)
    print(f"Verification (original message) : {'PASSED' if result else 'FAILED'}")

    # Verify a tampered message — should always fail
    tampered = message + b" [tampered]"
    result = verify(public_key, tampered, signature)
    print(f"Verification (tampered message) : {'PASSED' if result else 'FAILED'}")

if __name__ == "__main__":
    main()