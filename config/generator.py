import os
import secrets
import string
from pathlib import Path


os.chdir(Path(__file__).parent)
LOCAL_SETTINGS_PATH = "./local_settings.py"


def generate_secret_key():
    """
    シークレットーキー自動生成
    """

    sequence = string.ascii_letters + string.digits + "!#$%()+-@"

    gen = (
        secrets.choice(sequence) for letter in range(50)
    )
    secret_key = "".join(gen)

    return secret_key


def secret_key_is_exist():
    """
    SECRET_KEY_LSの存在確認
    """
    with open(LOCAL_SETTINGS_PATH, "r", encoding="utf-8") as f:
        for row in f:
            if "SECRET_KEY_LS" in row:
                print("SECRET_LEY_LS is already defined.")
                return True
        return False


def write_on_ls():
    """
    generate_secret_keyで生成したシークレットキーを
    local_settings.pyに書き込む
    """
    if not secret_key_is_exist():
        with open(LOCAL_SETTINGS_PATH, "a", encoding="utf-8") as f:
            secret_key = generate_secret_key()
            f.write("SECRET_KEY_LS = \"" + secret_key + "\"\n")
        print("SECRET_KEY_LS has been generated.")


if __name__ == "__main__":
    write_on_ls()
