import json
import sys

from cryptography.fernet import Fernet

"""
对称加密算法
"""

# 生成密钥
key = Fernet.generate_key()


# 加密字符串
def encrypt_message(message: str, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(message.encode())


# 解密字符串
def decrypt_message(message: bytes, key: bytes) -> str:
    f = Fernet(key)
    return f.decrypt(message).decode()


def main():
    """
    使用说明
    python3 current.py test_in.md test_out
    """
    input = sys.argv[1]
    out = sys.argv[2]
    # 加密示例
    encrypted_message = ""
    with open(input, "r") as f:
        content = f.read()
        encrypted_message = encrypt_message(content, key)
        print(encrypted_message)

    data = {
        "key": key.decode('utf-8'),
        "value": encrypted_message.decode('utf-8')
    }

    with open(f"{out}.json", "w+") as f:
        f.write(json.dumps(data))
        f.flush()


main()
