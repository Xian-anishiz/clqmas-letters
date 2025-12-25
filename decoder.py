import base64
def base64_decoder(data: bytes):
    return base64.decode(data)

def xor_decoder(data: bytes, key: int):
    return (d ^ key for d in data)