from sys import stdin

def main():
    chains_dict = {}
    chains_list = []
    for input in stdin:
        if input == '': # If empty string is read then stop the loop
            break
        else:
            if "start_" + input[0:4] not in chains_dict:
                chains_dict["start_" + input[0:4]] = input[:-1]
            else:
                chains_dict["start_" + input[0:4]].append(input[:-1])
            if "end_" + input[-5:-1] not in chains_dict:
                chains_dict["end_" + input[-5:-1]] = input[:-1]
            else:
                chains_dict["end_" + input[-5:-1]].append(input[:-1])
            chains_list.append(input[:-1])
    # match()

# def match(dna_list, dict):
#     for e in dna_list:

if __name__ == "__main__":
    main()