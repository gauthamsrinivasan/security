from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
def generate_dsa_keypair():
    private_key = dsa.generate_private_key(key_size=1024, backend=default_backend())
    public_key = private_key.public_key()
    return private_key, public_key
def sign_data(private_key, data):
    signature = private_key.sign(data, hashes.SHA256())
    return signature
def verify_signature(public_key, data, signature):
    try:
        public_key.verify(signature, data, hashes.SHA256())
        return True
    except:
        return False
    
# Example usage:
private_key, public_key = generate_dsa_keypair()
message = "Hello, DSA!"
# Signing (encode the message before signing)
signature = sign_data(private_key, message.encode('utf-8'))
# Verifying
is_verified = verify_signature(public_key, message.encode('utf-8'), signature)
print("Original Message:", message)
print("Signature:", signature.hex())
print("Verified:", is_verified)
