"""Devise the necessary code in any language to receive from prompt your First and Last names
separated by a space and return it as a complete reverse string. Example: John Doe -> eoD nhoJ.
The intention of this exercise is to NOT use any built in methods by any framework or tool that
provide this functionality, but see how you implement it"""


def reverse_string(string):
    reversed_string = ''
    for i in range(0, len(string)):
        reversed_string += string[len(string)-(i+1)]
    return reversed_string


def request_input():
    names = input("Enter First and Last name separated by space:")
    return names


def main():
    string_test = request_input()
    result = reverse_string(string_test)
    print('Reversed string: {}'.format(result))


if __name__== "__main__" :
    main()


