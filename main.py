import os

output_folder = "Output/ReadyToSend"


guests = open('C:\\Users\\Illia Gabchenko\\Desktop\\Python\\mail\\Mail Merge Project Start\\Input\\Names\\invited_names.txt', "r")
guest_list = guests.readlines()

with open('C:\\Users\\Illia Gabchenko\\Desktop\\Python\\mail\\Mail Merge Project Start\\Input\\Names\\invited_names.txt', "r") as guest_list:
    guest_list = [name.strip() for name in guest_list.readlines()]
    print(guest_list)

with open('C:\\Users\\Illia Gabchenko\\Desktop\\Python\\mail\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt', 'r') as letter_text:
    lines_of_letter = letter_text.readlines()

for guests in guest_list:
    personalized_letter = lines_of_letter.copy()
    personalized_letter[0] = personalized_letter[0].replace('[name]', guests)
    file_path = os.path.join(output_folder, f"letter for {guests}.txt")
    with open(file_path, 'w') as new_file:
        new_file.writelines(personalized_letter)
