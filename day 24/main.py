# Made changes in the snake game , day 20 & 21

### Added functionallity of saving high score everytime the game starts or ends using the file open, read and write. ###

# file = open('hello')
# contents = file.read()
# print(contents)
# file.close()

## How to open, read and write files using the "with" keyword ##

# with open('hello') as file:
#     contents = file.read()
#     print(contents)
#
### # Writing over old text
# with open('hello', mode='w') as file:
#     file.write('hello Madhav')
#
### # Adding new text
# with open('hello', mode='a') as file:
#     file.write('\n100 days 100 projects')
#
### # Creating new file with text, only in write mode
# with open('new_file', mode='w') as file:
#     file.write('New text')

# with open ('C:/Users/MadhavS/Desktop/newF.txt') as file:
#     contents = file.read()
#     print(contents)

with open ('../../../Desktop/newF.txt') as file:
    contents = file.read()
    print(contents)
