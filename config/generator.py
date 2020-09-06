import secrets
import string


def generate_secret_key():
    """シークレットーキー自動生成"""

    sequence = string.ascii_letters + string.digits + "!#$%()+-@"

    gen = (
        secrets.choice(sequence) for letter in range(50)
    )
    secret_key = "".join(gen)

    return secret_key


print(generate_secret_key())

