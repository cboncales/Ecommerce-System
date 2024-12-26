from cryptography.fernet import Fernet
from django.conf import settings

# Initialize encryption key
encryption_key = settings.ENCRYPTION_KEY
cipher = Fernet(encryption_key)


def encrypt_message(message: str) -> str:
    """Encrypt a message."""
    return cipher.encrypt(message.encode()).decode()


def decrypt_message(encrypted_message: str) -> str:
    """Decrypt a message."""
    return cipher.decrypt(encrypted_message.encode()).decode()
