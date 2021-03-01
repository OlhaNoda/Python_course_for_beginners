def caesar(text: str, shift: int = 3) -> str:
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    result_text = ''
    for letter in text:
        if letter.isalpha():
            if letter.islower():
                result_text += alpha[(alpha.index(letter) + shift) % len(alpha)]
            else:
                result_text += alpha[(alpha.index(letter.lower()) + shift) % len(alpha)].upper()
        else:
            result_text += letter
    return result_text
