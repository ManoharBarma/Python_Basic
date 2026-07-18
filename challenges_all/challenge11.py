#  Write a program that:
#
#  Asks the user for a filename.
#  Tries to open it.
#  If the file exists:
#  Print "File opened successfully."
#  Print its contents.
#  If the file doesn't exist:
#  Print "File not found."
#  Use a finally block to print:
#  Program ended.

file_name = input("enter your file name : ")

try:
    with open(file_name) as file:
        data = file.read()
        print(f"File opened successfully.")
        print(data)

except Exception as e:
    print("File not found.")
    print(f"error : {e}")
finally:
    print("Program ended")

######################################

numbers = [10, 20, 30]

num = int(input("Enter your index number : "))

try:
    print(numbers[num])
except IndexError:
    print("Index out of range.")
finally:
    print("Done")
