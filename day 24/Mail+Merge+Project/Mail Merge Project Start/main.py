#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open('../Mail Merge Project Start/Input/Names/invited_names.txt', 'r') as file:
    names = file.readlines()


with open('../Mail Merge Project Start/Input/Letters/starting_letter.txt') as file:
    content = file.read()
    for name in names:
        stripped_name = name.strip()
        x = content.replace('[name]', stripped_name)
        with open(f'./Output/ReadyToSend/letter to {stripped_name}.txt', mode='w') as file:
            file.write(x)
