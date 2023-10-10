import random

def get_user_input():
  user_input = {}

  # Ask the user if they want to include alphabets, digits, and special characters.
  user_input['include_alphabets'] = input('Do you want to include alphabets in your password? (y/n): ')
  user_input['include_digits'] = input('Do you want to include digits in your password? (y/n): ')
  user_input['include_special_characters'] = input('Do you want to include special characters in your password? (y/n): ')

  # Ask the user what characters they want to exclude.
  user_input['exclude'] = input('Enter the characters to exclude from your password (blank for none): ')

  # Prompt the user for the password characters (optional).
  user_input['characters'] = input('Enter the characters to include in your password (blank for all): ') or None

  # Generate a list of characters to include in the password.
  characters = ''
  if user_input['include_alphabets']:
    characters += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  if user_input['include_digits']:
    characters += '0123456789'
  if user_input['include_special_characters']:
    characters += '!@#$%^&*()'

  # Prompt the user for the password length.
  while 'length' not in user_input:
    user_input['length'] = int(input('Enter the length of the password: '))

  # Return the user's input.
  return user_input


def generate_password(length, characters, exclude=None):

  if characters is None:
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

  if exclude is None:
    exclude = ''

  password = ''
  for i in range(length):
    password += random.choice([c for c in characters if c not in exclude])

  return password


def main():

  user_input = get_user_input()

  password = generate_password(
      length=user_input['length'],
      characters=user_input['characters'],
      exclude=user_input['exclude']
  )

  print('Your random password is:', password)


if __name__ == '__main__':
  main()
