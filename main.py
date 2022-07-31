import re
import csv

def phone(tel):
    if len(tel) == 1:
        for t in tel:
            telephone = f'+7({t[1]}){t[2]}-{t[3]}-{t[4]}'
            return telephone
    elif len(tel) > 1:
        tel_dob = tel[0] + tel[1]
        telephone = f'+7({tel_dob[1]}){tel_dob[2]}-{tel_dob[3]}-{tel_dob[4]} доб.{tel_dob[-1]}'
        return telephone
    elif len(tel) == 0:
        return 'phone'

def delete_duplicate(contacts):
    for contact in contacts:
        last_name = contact[0]
        first_name = contact[1]
        for new_contact in contacts:
            new_last_name = new_contact[0]
            new_first_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == '':
                    contact[2] = new_contact[2]
                if contact[3] == '':
                    contact[3] = new_contact[3]
                if contact[4] == '':
                    contact[4] = new_contact[4]
                if contact[5] == '' or contact[5] == None or contact[5] == 'phone':
                    contact[5] = new_contact[5]
                if contact[6] == '':
                    contact[6] = new_contact[6]
    final_list = []
    for string in contacts:
        if string not in final_list:
            final_list.append(string)
    return final_list

if __name__ == "__main__":

    with open('phonebook_raw.csv') as f:
        rows = csv.reader(f, delimiter=",")
        contact_list = list(rows)

    pattern1 = re.compile(r'^^(\w+)(\,?|\s*)(\w+)(\,?|\s*)(\w+)?,+')
    pattern2 = re.compile(r'(\+7|8)\s*\(?(\d{3})\)?\s*[-\s]?(\d{3})\s*[-\s]?(\d{2})\s*[-\s]?(\d{2})\,?|\s\(?доб.\s(\d+)')

    phone_book = []
    for string in contact_list:
        person = pattern1.findall(','.join(string))
        tel = pattern2.findall(' '.join(string))
        for fio in person:
            phone_book_string = [fio[0], fio[2], fio[4], string[3], string[4], phone(tel), string[6]]
            phone_book.append(phone_book_string)

    with open("phonebook.csv", "w") as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(delete_duplicate(phone_book))

