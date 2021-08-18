#! /usr/bin/env python3
# This program converts caps lock mistakes into lowercase!

import pyperclip
text = pyperclip.paste() # variable is now the sentence that you made a mistake on

text = text.lower() # Will lower it
text = text.capitalize() # Assumes that you want first letter to be capital
pyperclip.copy(text) # And copy it to clipboard

print('The result has been copied to clipboard.') # Lets you know what it did
# NOTE: Make it so if you want to caps something it will do it too
