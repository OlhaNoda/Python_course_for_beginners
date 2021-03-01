def caesar(text: str, shift: int = 3) -> str:
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    result_text = ''
    for letter in text.lower():
        if letter.isalpha():
            result_text += alpha[(alpha.index(letter) + shift) % len(alpha)]
        else:
            result_text += letter
    return result_text
