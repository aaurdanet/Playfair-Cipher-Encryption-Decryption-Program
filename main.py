def print_stylized_text():
    print("""
@@@@@@@   @@@        @@@@@@   @@@ @@@  @@@@@@@@   @@@@@@   @@@  @@@@@@@   
@@@@@@@@  @@@       @@@@@@@@  @@@ @@@  @@@@@@@@  @@@@@@@@  @@@  @@@@@@@@  
@@!  @@@  @@!       @@!  @@@  @@! !@@  @@!       @@!  @@@  @@!  @@!  @@@  
!@!  @!@  !@!       !@!  @!@  !@! @!!  !@!       !@!  @!@  !@!  !@!  @!@  
@!@@!@!   @!!       @!@!@!@!   !@!@!   @!!!:!    @!@!@!@!  !!@  @!@!!@!   
!!@!!!    !!!       !!!@!!!!    @!!!   !!!!!:    !!!@!!!!  !!!  !!@!@!    
!!:       !!:       !!:  !!!    !!:    !!:       !!:  !!!  !!:  !!: :!!   
:!:        :!:      :!:  !:!    :!:    :!:       :!:  !:!  :!:  :!:  !:!  
 ::        :: ::::  ::   :::     ::     ::       ::   :::   ::  ::   :::  
 :        : :: : :   :   : :     :      :         :   : :  :     :   : :  
    """)


def print_grid(matrix):
    print("+---------------------------+")
    print("|        GRID MATRIX        |")
    print("+---------------------------+")
    for array in matrix:
        print(f"| {array} |")
    print("+---------------------------+")
    print("|         Playfair          |")
    print("+---------------------------+")


def create_grid(key):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    # append plaintext to grid
    grid = []
    for char in key:
        grid.append(char)

    # fill up array with alphabet
    i = 0
    while i < len(alphabet):
        grid.append(alphabet[i])
        i += 1

    # check for repeated characters
    i = 0
    while i < len(grid):
        j = i + 1
        while j < len(grid):
            if grid[i] == grid[j]:
                grid.pop(j)
            else:
                j += 1
        i += 1

    return grid


def box_case(first_r, first_c, second_r, second_c):
    new_first_c = second_c
    new_second_c = first_c
    new_indexes = [first_r, new_first_c, second_r, new_second_c]
    return new_indexes


def column_case(first_r, first_c, second_r, second_c, mode):
    if mode == "encrypt":

        new_indexes = []
        if first_r < 4:
            new_first_r = first_r + 1
        else:
            new_first_r = first_r % 4

        new_indexes.append(new_first_r)
        new_indexes.append(first_c)

        if second_r < 4:
            new_second_r = second_r + 1

        else:
            new_second_r = second_r % 4
        new_indexes.append(new_second_r)
        new_indexes.append(second_c)

        return new_indexes

    elif mode == "decrypt":
        new_indexes = []
        if first_r > 0:
            new_first_r = first_r - 1
        else:
            new_first_r = 4

        new_indexes.append(new_first_r)
        new_indexes.append(first_c)

        if second_r > 0:
            new_second_r = second_r - 1

        else:
            new_second_r = 4
        new_indexes.append(new_second_r)
        new_indexes.append(second_c)

        return new_indexes


def row_case(first_r, first_c, second_r, second_c, mode):
    if mode == "encrypt":
        new_indexes = []
        if first_c < 4:
            new_first_c = first_c + 1
        else:
            new_first_c = first_c % 4
        new_indexes.append(first_r)
        new_indexes.append(new_first_c)

        if second_c < 4:
            new_second_c = second_c + 1
        else:
            new_second_c = second_c % 4
        new_indexes.append(second_r)
        new_indexes.append(new_second_c)

        return new_indexes

    elif mode == "decrypt":
        new_indexes = []
        if first_c > 0:
            new_first_c = first_c - 1
        else:
            new_first_c = 4
        new_indexes.append(first_r)
        new_indexes.append(new_first_c)

        if second_c > 0:
            new_second_c = second_c - 1
        else:
            new_second_c = 4
        new_indexes.append(second_r)
        new_indexes.append(new_second_c)

        return new_indexes


# make padding
def padding_case(text, mode):
    if mode == "encrypt":
        print(text)
        plain_char_array = list(text)
        i = 1

        while i < len(plain_char_array):
            if plain_char_array[i] == plain_char_array[i - 1]:
                if plain_char_array[i] == "x":
                    plain_char_array.insert(i, "q")
                else:
                    plain_char_array.insert(i, "x")
            i += 2
        return ''.join(plain_char_array)

    elif mode == "decrypt":

        cipher_char_array = list(text)
        i = 1
        while i < len(cipher_char_array) - 1:
            if cipher_char_array[i] == "x" and cipher_char_array[i - 1] == cipher_char_array[i + 1]:
                cipher_char_array.pop(i)

            elif cipher_char_array[i + 1] == "q" and cipher_char_array[i] == "q":
                cipher_char_array.pop(i)
                cipher_char_array.insert(i, "q")

                cipher_char_array.pop(i + 1)
                cipher_char_array.insert(i + 1, "q")

            elif cipher_char_array[i] == "q" and cipher_char_array[i - 1] == cipher_char_array[i + 1]:
                cipher_char_array.pop(i)

            i += 2

        return ''.join(cipher_char_array)


def encrypt(two_encode, matrix):
    char = ""
    mode = "encrypt"

    if two_encode[0] == "i":
        two_encode[0] = "j"

    if two_encode[1] == "i":
        two_encode[1] = "j"

    first_char = two_encode[0]
    second_char = two_encode[1]
    first_loc = find_in_matrix(matrix, first_char)
    second_loc = find_in_matrix(matrix, second_char)

    first_r = first_loc[0]
    first_c = first_loc[1]

    second_r = second_loc[0]
    second_c = second_loc[1]

    if first_r != second_r and first_c != second_c:
        encoded_indexes = []
        encoded_indexes = box_case(first_r, first_c, second_r, second_c)

        char = matrix[encoded_indexes[0]][encoded_indexes[1]]  # First character
        char += matrix[encoded_indexes[2]][encoded_indexes[3]]
        print(char)

    if first_c == second_c and first_r != second_r:
        encoded_indexes = []
        encoded_indexes = column_case(first_r, first_c, second_r, second_c, mode)

        char = matrix[encoded_indexes[0]][encoded_indexes[1]]  # First character
        char += matrix[encoded_indexes[2]][encoded_indexes[3]]
        print(char)

    if first_c != second_c and first_r == second_r:
        encoded_indexes = []
        encoded_indexes = row_case(first_r, first_c, second_r, second_c, mode)

        char = matrix[encoded_indexes[0]][encoded_indexes[1]]  # First character
        char += matrix[encoded_indexes[2]][encoded_indexes[3]]
        print(char)

    return char


# find in matrix
def find_in_matrix(matrix, character):
    length_arrays = len(matrix)
    indexes = []
    for i in range(length_arrays):
        r = matrix[i]
        for j in range(len(r)):  # use len(c) to loop over each element in the current array
            c = matrix[i][j]
            if character == c:
                print(f"Value found at arrays[{i}][{j}]: {c}")
                char_r = i
                char_c = j
                indexes.append(char_r)
                indexes.append(char_c)
    return indexes


def start_encryption():
    mode = "encrypt"
    key = i_j_converter(input("Enter key for encryption:\n").replace(" ", ""), "convert")

    grid = create_grid(key)

    array1 = grid[0:5]
    array2 = grid[5:10]
    array3 = grid[10:15]
    array4 = grid[15:20]
    array5 = grid[20:25]

    # print matrix
    matrix = [array1, array2, array3, array4, array5]

    print_grid(matrix)

    plaintext = input("\nEnter text you want to encrypt\n").replace(" ", "")

    formatted_plaintext = padding_case(plaintext, mode)

    # let's separate the input string into char pairs
    two_letter = ""
    cipher = ""
    for char in formatted_plaintext:
        two_letter += char
        if len(two_letter) == 2:
            list(two_letter)
            # Encrypt the pair of characters
            cipher += encrypt(list(two_letter), matrix)  # Convert string to list
            two_letter = ""  # Reset for the next pair

    # add padding for odd
    if len(formatted_plaintext) % 2 != 0:
        cipher += "x"

    print(f"\nCiphertext: {cipher}")


def decrypt(two_decode, matrix):
    char = ""
    mode = "decrypt"

    if two_decode[0] == "i":
        two_decode[0] = "j"

    if two_decode[1] == "i":
        two_decode[1] = "j"

    first_char = two_decode[0]
    second_char = two_decode[1]
    first_loc = find_in_matrix(matrix, first_char)
    second_loc = find_in_matrix(matrix, second_char)

    first_r = first_loc[0]
    first_c = first_loc[1]

    second_r = second_loc[0]
    second_c = second_loc[1]

    if first_r != second_r and first_c != second_c:
        decoded_indexes = []
        decoded_indexes = box_case(first_r, first_c, second_r, second_c)

        char = matrix[decoded_indexes[0]][decoded_indexes[1]]  # First character
        char += matrix[decoded_indexes[2]][decoded_indexes[3]]
        print(char)

    if first_c == second_c and first_r != second_r:
        decoded_indexes = []
        decoded_indexes = column_case(first_r, first_c, second_r, second_c, mode)

        char = matrix[decoded_indexes[0]][decoded_indexes[1]]  # First character
        char += matrix[decoded_indexes[2]][decoded_indexes[3]]
        print(char)

    if first_c != second_c and first_r == second_r:
        decoded_indexes = []
        decoded_indexes = row_case(first_r, first_c, second_r, second_c, mode)

        char = matrix[decoded_indexes[0]][decoded_indexes[1]]  # First character
        char += matrix[decoded_indexes[2]][decoded_indexes[3]]
        print(char)

    return char


def i_j_converter(text, mode):

    if mode == "revert":
        text_w_i = list(text)
        x = 0
        res = ""
        while x < len(text_w_i):
            if text_w_i[x] == "j":
                text_w_i.pop(x)
                text_w_i.insert(x, "i")
            x += 1
        res += "".join(text_w_i)

        return res

    elif mode == "convert":
        text_w_i = list(text)
        x = 0
        res = ""
        while x < len(text_w_i):
            if text_w_i[x] == "i":
                text_w_i.pop(x)
                text_w_i.insert(x, "j")
            x += 1
        res += "".join(text_w_i)

        return res



def start_decryption():
    mode = "decrypt"
    key = i_j_converter(input("Enter key for decryption:\n").replace(" ", ""), "convert")
    grid = create_grid(key)

    array1 = grid[0:5]
    array2 = grid[5:10]
    array3 = grid[10:15]
    array4 = grid[15:20]
    array5 = grid[20:25]

    # print matrix
    matrix = [array1, array2, array3, array4, array5]

    print_grid(matrix)

    cipher = input("\nEnter text you want to decrypt\n").replace(" ", "")

    # formatted_cipher = padding_case(cipher)

    # let's separate the input string into char pairs
    two_letter = ""
    plaintext = ""
    for char in cipher:
        two_letter += char
        if len(two_letter) == 2:
            list(two_letter)
            # Decrypt the pair of characters
            plaintext += decrypt(list(two_letter), matrix)  # Convert string to list
            two_letter = ""  # Reset for the next pair

    cleared_plaintext = i_j_converter(padding_case(plaintext, mode), "revert")

    print(f"\nPlaintext: {cleared_plaintext}")


print_stylized_text()
selection = input("Do you want to encrypt or decrypt using Playfair? [E]ncryption | [D]ecryption\n").upper().strip().replace(" ", "")

if selection == "E":
    start_encryption()
elif selection == "D":
    start_decryption()
