#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

"""1. Возвращает список, где элементами являются строки файла
        2. Заменяет одно слово на другое
        3. Удаляет пробелы или указанные символы по краям строки"""
import os

output_folder = "Output/ReadyToSend"


guests = open('C:\\Users\\Illia Gabchenko\\Desktop\\Python\\mail\\Mail Merge Project Start\\Input\\Names\\invited_names.txt', "r")
guest_list = guests.readlines()
# print(len(guest_list))

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


# for guest in guest_list:
#     letter_text = open('C:\\Users\\Illia Gabchenko\\Desktop\\Python\\mail\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt', 'r')
#     letter_list = letter_text.readlines()
#     greeting = letter_list[0]
#     replace_name = greeting.replace('[name]', guest)
#     print(replace_name)
#     letter_list[0] = replace_name
#     print(letter_text)



# for guest in guest_list:
#     file_path = os.path.join(output_folder, f"letter for {guest.strip()}\.txt")
#     with open(file_path, 'w') as new_file:
#         # strings = [str(string) for string in letter_list]
#
#         # guest.write(f"This is a letter for {guest}")
#         new_file.write(f"{str(letter_list)}")