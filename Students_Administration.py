#Students Administration System
import csv
import os

def write_into_csv(info_list):# Filling Details
    with open('students_info_file.csv','a', newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(['Name', 'Roll', 'Class', 'Age', 'Email-ID', 'Registration-ID'])
        with open('students_info_file.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            for i in reader:
                if i[5] == info_list[5]:
                    print('Record with Same Registration Id already Present\n Pls enter non-duplicate details')
                    ask_details()
            writer.writerow(info_list)

def ask_details():# Asking Details
        count=1
        count_2=0
        while(True):
            details=['Name','Roll','Class','Age','Email-ID','Registration-ID',]
            print('Enter the details for student #{} : \n'.format(count))
            details[0] = input('1. Name     : ')
            details[1] = input('2. Roll     : ')
            details[2] = input('3. Class    : ')
            details[3] = int(input('4. Age      : '))
            details[4] = input('5. Email-ID : ')
            details[5] = input('6. Reg-ID    : ')
            if count_2 != 0:
                continue
            print('\nAre the details provided corrected: \n1. Name   : {} \n2. Roll   : {} \n3. Class  : {} \n4. Age    : {} '
                  '\n5. Email-ID: {}\n6. Registration-ID: {}'
                  .format(details[0],details[1],details[2],details[3],details[4],details[5]))
            choice_1=input('Enter yes or no : ')
            if choice_1 == 'no':
                print('\n Enter correct details \n')
                continue
            write_into_csv(details)
            choice_2=input('Do you want to enter the details of any other students \nEnter yes or no : ')
            if choice_2 == 'no':
                break
            else:
                count+=1

def ser_details():# Searching  Details
    with open('students_info_file.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        count = 0
        choice=int(input('Search by :\n1. Name\n2. Roll\n3. Class\n4. Age \n5.Email-ID\n6.Registration-ID\n'))
        if choice == 1:
            Name = input('Enter the Name : ')
            for i in reader:
                if Name == i[0]:
                    print('\n\nStudents details found')
                    print('\n1. Name   : {} \n2. Roll   : {} \n3. Class  : {} \n4. Age    : {} \n5.Email-ID: {}'
                          .format(i[0], i[1], i[2], i[3], i[4]))
                    count += 1
        elif choice == 2:
            Roll = input('Enter the Roll : ')
            for i in reader:
                if Roll == i[1]:
                    print('\n\nStudents details found')
                    print('\n1. Name   : {} \n2. Roll   : {} \n3. Class  : {} \n4. Age    : {} \n5.Email-ID: {}'
                          .format(i[0], i[1], i[2], i[3], i[4]))
                    count += 1
                    break
        elif choice == 3:
            Class = input('Enter the Class : ')
            for i in reader:
                if Class == i[2]:
                    print('\n\nStudents details found')
                    print('\n1. Name   : {} \n2. Roll   : {} \n3. Class  : {} \n4. Age    : {} \n5.Email-ID: {}'
                          .format(i[0], i[1], i[2], i[3], i[4]))
                    count += 1
        elif choice == 4:
            Age = int(input('Enter the Age : '))
            for i in reader:
                if Age == i[3]:
                    print('\n\nStudents details found')
                    print('\n1. Name   : {} \n2. Roll   : {} \n3. Class  : {} \n4. Age    : {} \n5.Email-ID: {}'
                          .format(i[0], i[1], i[2], i[3], i[4]))
                    count += 1
        elif choice == 5:
            Email = input('Enter the Email-ID : ')
            for i in reader:
                if Email == i[4]:
                    print('\n\nStudents details found')
                    print('\n1. Name   : {} \n2. Roll   : {} \n3. Class  : {} \n4. Age    : {} \n5.Email-ID: {}'
                          .format(i[0], i[1], i[2], i[3], i[4]))
                    count += 1
                    break
        elif choice == 6:
            Reg = input('Enter the Registration-ID : ')
            for i in reader:
                if Reg == i[5]:
                    print('\n\nStudents details found')
                    print('\n1. Name   : {} \n2. Roll   : {} \n3. Class  : {} \n4. Age    : {} \n5.Email-ID: {}'
                          .format(i[0], i[1], i[2], i[3], i[4]))
                    count += 1
                    break
        else:
            print('Entered wrong values !!!')
        if count == 0:
            print(' No Record found ')

def prt_details():# Printing Details
    with open('students_info_file.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        count=1
        for i in reader:
            if count>1 :
                print('Student #{}'.format(count-1),'\n1. Name   : {} \n2. Roll   : {} \n3. Class  : {} \n4. Age    : {} '
                                                  '\n5.Email-ID: {}\n6.Registration-ID: {}'
                    .format(i[0], i[1], i[2], i[3], i[4],i[5]),'\n\n')
            count+= 1

def del_details():# Deleting Details
    with open('students_info_file.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        with open('students_info.csv', 'a', newline='') as csv_file_2:
            writer = csv.writer(csv_file_2)
            Roll=input('Enter the Roll no. : ')
            for i in reader:
                if Roll != i[1]:
                    writer.writerow(i)
    csv_file.close()
    os.remove('students_info_file.csv')
    os.rename('students_info.csv','students_info_file.csv')

if __name__ == '__main__':
    print('\nWelcome to Student Administration System :\n')
    while(True):
        print('\n1.Enter Students Details.'
              '\n2.Delete Students Details\n3.Print Students details\n4.Search Students details\n\nEnter your choice (1/2/3/4) :\n')
        choice=int(input())
        if choice == 1:
            ask_details()
        elif choice == 2:
            del_details()
        elif choice == 3:
            prt_details()
        elif choice == 4:
            ser_details()
        else:
            print('Entered wrong values !!!')
        choice_3 = input('\nDo you want to perform any other operations?  \nEnter yes or no : ')
        if choice_3 == 'no':
            break
        elif choice_3 == 'yes':
            continue
        else:
            print('Entered wrong values !!!')