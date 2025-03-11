import re

def generate_matrix(keyword):
    keyword = keyword.upper().replace("J", "I")
    chars = "".join(dict.fromkeys(keyword + "ABCDEFGHIKLMNOPQRSTUVWXYZ"))
    return [list(chars[i:i+5]) for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for r, row in enumerate(matrix):
        if letter in row:
            return r, row.index(letter)

def prepare_text(text):
    text = re.sub(r'[^A-Z]', '', text.upper().replace("J", "I"))
    text = re.sub(r'(.)\1', r'\1X', text)  
    if len(text) % 2: text += "X"  
    return [text[i:i+2] for i in range(0, len(text), 2)]

def process_pairs(matrix, pairs, mode):
    result = ""
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            c1, c2 = (c1+1, c2+1) if mode == "encrypt" else (c1-1, c2-1)
        elif c1 == c2:
            r1, r2 = (r1+1, r2+1) if mode == "encrypt" else (r1-1, r2-1)
        else:
            c1, c2 = c2, c1
        
        result += matrix[r1 % 5][c1 % 5] + matrix[r2 % 5][c2 % 5]
    return result

def playfair_cipher():
    matrix = generate_matrix(input("Enter keyword: "))
    mode = "encrypt" if input("(E)ncrypt or (D)ecrypt? ").strip().lower() == 'e' else "decrypt"
    text_pairs = prepare_text(input("Enter text: "))
    
    print("Playfair Matrix:")
    for row in matrix:
        print(" ".join(row))
    
    print("Result:", process_pairs(matrix, text_pairs, mode))

playfair_cipher()
