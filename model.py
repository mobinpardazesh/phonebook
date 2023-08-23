# https://www.pyforschool.com/project/contact-book-python-mysql-project.html
# https://www.geeksforgeeks.org/how-to-install-mysql-connector-package-in-python/
import time
import mysql.connector
from mysql.connector import Error

myconnection = mysql.connector.connect(host='localhost',
                                     database='phonebook',
                                     user='root',
                                     password='')

def create_person():
    name = input("Enter name: ")
    address = input("Enter address: ")
    mobile = input("Enter mobile: ")
    email = input("Enter email: ")
    mycursor = myconnection.cursor()
    sql = "INSERT INTO phonebook(name,address,mobile,email) VALUES (%s,%s,%s,%s)"
    record = (name, address, mobile, email)
    # print(type(record))
    mycursor.execute(sql, record)
    myconnection.commit()
    mycursor.close()
    print("Record Entered Succuessfully\n")


def search(name):
    mycursor = myconnection.cursor()
    sql = "select * from phonebook where name = %s"
    value = (name,)
    mycursor.execute(sql, value)
    record = mycursor.fetchone()
    mycursor.close()
    if record == None:
        print("No such record exists")
    else:
        print('Name:', record[0])
        print('Address:', record[1])
        print('Mobile:', record[2])
        print('E-mail:', record[3])


def display_all():
    mycursor = myconnection.cursor()
    mycursor.execute("select * from phonebook")
    print('{0:20}{1:30}{2:15}{3:30}'.format('NAME', 'ADDRESS', 'MOBILE NO', 'E-MAIL'))
    for record in mycursor:
        print('{0:20}{1:30}{2:15}{3:30}'.format(record[0], record[1], record[2], record[3]))
    mycursor.close()


def delete_record(name):
    mycursor = myconnection.cursor()
    sql = "DELETE from phonebook WHERE name = %s"
    value = (name,)
    mycursor.execute(sql, value)
    myconnection.commit()
    if mycursor.rowcount == 0:
        print("Record not found")
    else:
        print("Record deleted successfully")
    mycursor.close()


def modify_record(name):
    mycursor = myconnection.cursor()
    sql = "select * from book where name = %s"
    value = (name,)
    mycursor.execute(sql, value)
    record = mycursor.fetchone()
    if record == None:
        print("No such record exists")
    else:
        while True:
            print("\nPress the option you want to edit: ")
            print("1. Name")
            print("2. Address")
            print("3. Mobile")
            print("4. BACK")
            print()
            ch = int(input("Select Your Option (1-4): "))
            if ch == 1:
                new_name = input("Enter new name: ")
                sql = "UPDATE phonebook SET name = %s WHERE name = %s"
                values = (new_name, name)
                mycursor.execute(sql, values)
                myconnection.commit()
                print(mycursor.rowcount, "record updated successfully")
            elif ch == 2:
                new_address = input("Enter new address: ")
                sql = "UPDATE phonebook SET address = %s WHERE name = %s"
                values = (new_address, name)
                mycursor.execute(sql, values)
                myconnection.commit()
                print(mycursor.rowcount, "record updated successfully")
            elif ch == 3:
                new_mobile = input("Enter new mobile : ")
                sql = "UPDATE phonebook SET mobile = %s WHERE name = %s"
                values = (new_mobile, name)
                mycursor.execute(sql, values)
                myconnection.commit()
                print(mycursor.rowcount, "record updated successfully")
            elif ch == 4:
                break
            else:
                print("invalid choice !!!\n")
    mycursor.close()


def intro():
    print("=" * 80)
    print("{: ^80s}".format("CONTACT"))
    print("{: ^80s}".format("BOOK"))
    print("{: ^80s}".format("PROJECT"))
    print("{: ^80s}".format("MADE BY: Ayda Seyedi"))
    print("=" * 80)
    print()
    time.sleep(2)


def main():
    intro()
    while True:
        print("\nMAIN MENU ")
        print("1. ADD NEW RECORD")
        print("2. SEARCH RECORD")
        print("3. DISPLAY ALL RECORDS")
        print("4. DELETE RECORD")
        print("5. MODIFY RECORD")
        print("6. EXIT")
        print()
        choice = int(input("Select Your Option (1-6): "))
        print()
        if choice == 1:
            print("ADD NEW RECORD")
            create_person()
        elif choice == 2:
            print("SEARCH RECORD BY NAME")
            name = input("Enter name: ")
            search(name)
        elif choice == 3:
            print("DISPLAY ALL RECORDS")
            display_all()
        elif choice == 4:
            print("DELETE RECORD")
            name = input("Enter name: ")
            delete_record(name)
        elif choice == 5:
            print("MODIFY RECORD")
            name = input("Enter name: ")
            modify_record(name)
        elif choice == 6:
            print("Thanks for using Phone Book")
            myconnection.close()
            break
        else:
            print("Invalid choice")


main()
