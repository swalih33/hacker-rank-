def print_full_name(first, last):
    # Write your code here
    
    full_name="Hello " + first_name + " " + last_name + "you just delved into python"
    print(full_name)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)