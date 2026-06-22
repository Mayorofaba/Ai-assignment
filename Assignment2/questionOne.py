def encrypt_name(full_name, key):
    encrypted_text = ""
    # Check fo
    for character in full_name:
        if character.isalpha():  
            shift_amount = key % 26  
            
            if character.islower():
                # Shift lowercase letters: a->b, b->c, etc.
                shifted_char = chr((ord(character) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                # Shift uppercase letters: A->B, B->C, etc.
                shifted_char = chr((ord(character) - ord('A') + shift_amount) % 26 + ord('A'))
            
            encrypted_text += shifted_char
        else:
            # Keep spaces and punctuation unchanged
            encrypted_text += character
    
    # If key is even, reverse the entire encrypted text for extra security
    if key % 2 == 0:
        encrypted_text = encrypted_text[::-1]
    
    return encrypted_text


def decrypt_name(encrypted_text, key):
    # If the key is even, reverse the text back to its original order
    if key % 2 == 0:
        encrypted_text = encrypted_text[::-1]
    
    decrypted_text = ""
    
    # Process each character to reverse the encryption
    for character in encrypted_text:
        if character.isalpha():  # Only decrypt letters
            shift_amount = key % 26  # Keep shift within alphabet range (0-25)
            
            if character.islower():
                # Reverse shift for lowercase letters: b->a, c->b, etc.
                original_char = chr((ord(character) - ord('a') - shift_amount) % 26 + ord('a'))
            else:
                # Reverse shift for uppercase letters: B->A, C->B, etc.
                original_char = chr((ord(character) - ord('A') - shift_amount) % 26 + ord('A'))
            
            decrypted_text += original_char
        else:
            # Keep spaces and punctuation unchanged
            decrypted_text += character
    
    return decrypted_text


# Main program to demonstrate the cipher system
if __name__ == "__main__":
    full_name = "Nwabuko Micheal Chinedu"
    encryption_key = len("Alice")  # Key is the length of the first name (5)
    
    print("=" * 50)
    print("NAME CIPHER SYSTEM DEMONSTRATION")
    print("=" * 50)
    print(f"\nKey: {encryption_key} (length of 'Alice')")
    print(f"Key is {'even' if encryption_key % 2 == 0 else 'odd'} - "
          f"text will {'be reversed' if encryption_key % 2 == 0 else 'not be reversed'}\n")
    
    # Encrypt the name
    original_name = full_name
    encrypted_name = encrypt_name(original_name, encryption_key)
    
    print(f"Original Name:   {original_name}")
    print(f"Encrypted Name:  {encrypted_name}")
    
    # Decrypt the name
    decrypted_name = decrypt_name(encrypted_name, encryption_key)
    print(f"Decrypted Name:  {decrypted_name}")
    
    # Verify the cycle worked correctly
    if decrypted_name == original_name:
        print(f"\n✓ Success! Original and decrypted names match.")
    else:
        print(f"\n✗ Error: Names do not match!")
    
    print("=" * 50)      
