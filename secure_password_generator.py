import random

digits = '123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

num_passwords = int(input('Сколько паролей нужно сгенерировать? '))
length = int(input('Какой длины должен быть каждый пароль? '))

include_digits = input('Включать ли цифры 0123456789? (да/нет): ').strip().lower()
include_uppercase = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет): ').strip().lower()
include_lowercase = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет): ').strip().lower()
include_symbols = input('Включать ли символы !#$%&*+-=?@^_.? (да/нет): ').strip().lower()
exclude_ambiguous = input('Исключать ли неоднозначные символы il1Lo0O? (да/нет): ').strip().lower()

if include_digits == 'да':
    chars += digits
if include_uppercase == 'да':
    chars += uppercase_letters
if include_lowercase == 'да':
    chars += lowercase_letters
if include_symbols == 'да':
    chars += punctuation

if exclude_ambiguous == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(length, chars):
    """Возвращает случайный пароль длины length из символов chars."""
    return ''.join(random.choice(chars) for _ in range(length))

print('\nСгенерированные пароли:')
for _ in range(num_passwords):
    print(generate_password(length, chars))