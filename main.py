from sys import stdin

def main():
    chains = []
    for input in stdin:
        if input == '': # If empty string is read then stop the loop
            break
        else:
            chains.append(input)


def match():