import base64
import random
from four import four, four1 #the custom dictionary named four is not being shown.

class Cipher:
    def __init__(self):
        pass

    def encode_message(self, message):
        encoded = ""
        new_em = ""
        for letter in message:
            if letter.isalpha():
                if letter in four:
                    encoded += str(four[letter])
                    new_em += random.choice(str(four[letter]))
                elif letter in four1:
                    encoded += str(four1[letter])
                    new_em += random.choice(str(four1[letter]))
                else:
                    encoded += letter
            else:
                encoded += letter
        base64_encoded_message = base64.b64encode(new_em.encode()).decode()
        return encoded, base64_encoded_message

    def decode_message(self, encoded_message):
        decoded = ""
        i = 0
        while i < len(encoded_message):
            found = False
            for key, value in four.items():
                if str(value) == encoded_message[i:i+len(str(value))]:
                    decoded += key
                    found = True
                    break
            if not found:
                decoded += encoded_message[i:i+1]
            i += len(str(value)) if found else 1

        return decoded

def main():
    cipher = Cipher()

    print("Enter the message to encode:")
    message_lines = []
    try:
        while True:
            line = input()
            if not line:
                break
            message_lines.append(line)
    except EOFError:
        pass

    message = '\n'.join(message_lines)

    encoded_message, base64_encoded_message = cipher.encode_message(message)
    print("Encoded message:", base64_encoded_message)
  
#below the necessary logic to decode the encoded is encoded here.
    LGUgbzhuWywsIGVhaWFjbnQ4IHMscl10MCwnICAyaCdvJywnMG1bIGVhbyx5cFtuW250LDAgIGYscGNdbycgcGt2W2UnJ29nICcnMCxpbixpLGgnICxdY2gsXSwwYycnJyBlb3NyZCAnIGVyZSwsJ2UsJ2UsbmJlc1thZDdobywnLCwwIHJ0Nm4=

if __name__ == "__main__":
    main()
