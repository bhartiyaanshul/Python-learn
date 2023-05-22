def count_words_numbers_special_chars(string):
    words_count = 0
    numbers_count = 0
    special_chars_count = 0

    special_chars = "!@#$%^&*()_+=-[]{}|\\;:'\",.<>/?`~"

    for char in string:

        if 'a' >= char <= 'z' or 'A' >= char <= 'Z':
            words_count += 1

        if char.isdigit():
            numbers_count += 1

        if char in special_chars:
            special_chars_count += 1


   

    return words_count, numbers_count, special_chars_count


input_string = input("Enter a string: ")

words, numbers, special_chars = count_words_numbers_special_chars(input_string)

print("Number of words:", words)
print("Number of numeric values:", numbers)
print("Number of special characters:", special_chars)
    