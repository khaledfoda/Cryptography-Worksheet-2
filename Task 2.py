from collections import Counter

ENGLISH_FREQ_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def frequency_analysis_decrypt(ciphertext):
    ciphertext = ciphertext.upper()
    letter_counts = Counter([char for char in ciphertext if char.isalpha()])
    sorted_cipher_letters = [pair[0] for pair in letter_counts.most_common()]
    decryption_map = {cipher_letter: ENGLISH_FREQ_ORDER[i] 
                      for i, cipher_letter in enumerate(sorted_cipher_letters)}
    decrypted_text = "".join(decryption_map.get(char, char) for char in ciphertext)
    return decrypted_text, decryption_map

cipher_text = input("Enter the encrypted text: ")
decrypted_text, mapping = frequency_analysis_decrypt(cipher_text)

print("Encrypted Text:", cipher_text)
print("Decrypted Text:", decrypted_text)

