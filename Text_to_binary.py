def text_to_binary(text):
  binary_data = ''.join(format(ord(char), '08b') for char in text)
  return binary_data

text = input("\033[1;34mEnter text: \033[0m")
binary = text_to_binary(text)
print("\033[1;34mBinary representation: \033[0m", binary)


# End of code
# Github : 1eaz
# IG : aflzc
