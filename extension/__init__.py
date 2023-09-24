import re


def encrypt(text):
    encrypted = ""
    text = remove_special_characters(text)
    bin = ' '.join(format(ord(c), 'b') for c in text)
    for i in bin:
        if i == "0":
            encrypted += my_dict[0]
        elif i == "1":
            encrypted += my_dict[1]
        elif i == " ":
            encrypted += "meow"
        else:
            encrypted += "-"
    return encrypted

def decrypt(encrypted_text):
    binary_text = ""
    decrypted = ""
    encrypted_text_list = []
    reversed_dict = {v: str(k) for k, v in my_dict.items()}
    
    encrypted_text = encrypted_text.replace("-", "")
    encrypted_text = encrypted_text.split("meow")

    for word in encrypted_text:
        convert_word = ""
        binary_text = ""
        encrypted_text_list = split_string_into_list(word, 7)

        for b in encrypted_text_list:
            binary_text += reversed_dict.get(b, "")

        binary_text_list = split_string_into_list(binary_text, 7)

        for b in binary_text_list:
            convert_word += chr(int(b, 2))

        decrypted += convert_word

    return decrypted


def split_string_into_list(input_string, chunk_size):
    result = []

    for i in range(0, len(input_string), chunk_size):
        result.append(input_string[i:i + chunk_size])

    return result

def remove_special_characters(input_string):
    pattern = r'[^a-zA-Z0-9\s]'
    cleaned_string = re.sub(pattern, '', input_string)
    return cleaned_string

my_dict = {
    0: "MIaUUUU",
    1: "miiiaau",
}
