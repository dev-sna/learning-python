# -------- Old method of opening a file --------
my_file = open('basic.txt')
print('File: ', my_file, '\n')

# Read the text
print('File text: ', my_file.read(), '\n')
# Read again. It will give no text because the
# curson is now at the end of the file.
print('File text when read again: ', my_file.read(), '\n')

# Reset the cursor
my_file.seek(0)
# Now we will get the full text again
print('Read the file again: ', my_file.read(), '\n')

# Read lines as a list
my_file.seek(0)
print('Read the lines as list: ', my_file.readlines(), '\n')

# An opened file needs to be closed to become available for other software
my_file.close()

# ---------------------------
# New method that directly assigns a
# variable when it opens a file.

with open('basic.txt') as my_new_file:
    file_contents = my_new_file.read()

print('File contents: ', file_contents, '\n')

# Writing to a file
# Permissions:
# r: read only
# w: write only (overwrite existing or create new)
# a: append only(will add on to files)
# r+: reading and writing
# w+: writing and reading (overwrite existing or create new)

# Note: w/w+ creates a new file if the files doesn't exist

# Append
with open('basic.txt', mode='a') as f:
    f.write('\nThis is the fourth line.')

# Writing
# The code below will create a new file if it doesn't exist.
# It will then write a line to it and then print the content.
with open('new_file.txt', mode='w+') as f:
    f.write('This is my new file.')
    # As we write to a file, the cursor is at the
    # end so we need to reset it.
    f.seek(0)
    new_file_content = f.read()
    print('New file content: ', new_file_content, '\n')
