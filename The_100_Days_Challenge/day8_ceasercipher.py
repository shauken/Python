# redo later
def caesar_cypher(cypher_text, shift_change, cypher_direction):
    encrypted = ''

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    for i in range(len(cypher_text)):

        if ord(cypher_text[i]) + shift_change > 122:

            position = (122 - ord(cypher_text[i]))

            new_shift = (shift_change - position) - 2

            encrypted += alphabet[new_shift]

    print(f'Here\'s the encoded result:\n{encrypted}')



while choice == 'yes':

    direction = input('Type \'encode\' to encrypt, type \'decode\' to decrypt:')

    message = input('Type your message:\n')

    shift = int(input('Type the shift number:\n'))

    choice = input('Type \'yes\' if you want to go again. Otherwise type \'no\'.\n')

    caesar_cypher(message, shift, direction)
