
# Problem Statement

Kent is trying to send his friends a message for Christmas, sadly, an evil twink messed with the letters and encrypted them before reaching the recipients! Can you help the recipients decode Kent's Christmas letter back to their original message?

# Task Details

In this task you are required to create two functions. A base64 decoder that takes in one input `data` of type `bytes` then returns a `bytes` datatype and a XOR decoder that takes in two inputs `data` of type `bytes` and `hash_key` of type `int`. 

The base64 decoder reads the contents of the text file `{recipient_nickname}_encrypted.txt` using data and returns bytes of information, which is then used as input in the XOR decoder alongside the unique `hash_key` given alongside your respective emails.

You may use the following lines of codes to read the encrypted letter contents and output a new file containing the actual message. Reminder to replace the decoders with your own implementations.
```
def decode_letter(recipient: str, hash_key: int):
    in_name = f"{recipient}_encrypted.txt"
    out_name = f"{recipient}_decrypted.txt"

    with open(in_name, "rb") as f:
        data = f.read()

    encrypted = base64_decoder(data)
    decoded = xor_decoder(encrypted, hash_key)

    with open(out_name, "wb") as f:
        f.write(decoded)
```
```
def base64_decoder(data: bytes) -> bytes:
    ...
def xor_decoder(data: bytes, hash_key: int) -> bytes:
    ...
```
*for the recipient, enter your respective name from the list provided below*
```
recipients = [
    "Ariz",
    "JR",
    "Kylie",
    "Erin",
    "Rohan",
    "Lore",
    "Dayshaun",
    "Clint",
    "Fio",
    "Jo",
    "Princ",
    "Paw",
    "Reese",
    "Clique"
]
```

## Hints
Python has a built in base64 module

XOR has three key properties:

-`A XOR B = C`
-`C XOR B = A`
-`A XOR A = 0`

# Scoring
- You get 100❤️ if you solve all the case where you use your own recipient nickname and unique hash_key.
- You get an honorary medal if you manage to decode even other people's letter [but why would you go through the trouble knowing which hash_key belongs to who].
