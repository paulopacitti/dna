from sys import stdin

def main():
    chains_dict = {}
    chains_list = []
    for input in stdin:
        if input == '': # If empty string is read then stop the loop
            break
        else:
            if "start_" + input[0:4] not in chains_dict:
                chains_dict["start_" + input[0:4]] = [input[:-1]]
            else:
                chains_dict["start_" + input[0:4]].append(input[:-1])
            if "end_" + input[-5:-1] not in chains_dict:
                chains_dict["end_" + input[-5:-1]] = [input[:-1]]
            else:
                chains_dict["end_" + input[-5:-1]].append(input[:-1])
            chains_list.append(input[:-1])
    dna_list = match(chains_list, chains_dict)
    
    for dna in dna_list:
        print(dna)

def match_recursive(curr_chain, combinations_list, chains_dict):
    possible_combinations = combinations(curr_chain, chains_dict)
    if not possible_combinations:
        return curr_chain

    for dna in possible_combinations:
        combinations_list.append(match_recursive(curr_chain + dna, combinations_list, chains_dict))
    
    return curr_chain

def match(dna_list, chains_dict):
    final_combinations = []
    for dna in dna_list:
        if not combinations(dna, chains_dict):
            final_combinations.append(dna)
        else:
            match_recursive(dna, final_combinations, chains_dict)
    
    remove_list = []
    for x in final_combinations:
        for y in final_combinations:
            if y.find(x) != -1:
                if len(y) > len(x):
                    remove_list.append(x)
                elif len(y) < len(x): 
                    remove_list.append(y)
    
    return [combination for combination in final_combinations if combination not in remove_list]

def combinations(chain, chains_dict):
    possible_key = "start_" + chain[-4:]
    if possible_key in chains_dict:
        return chains_dict[possible_key]
    else:
        return False

if __name__ == "__main__":
    main()
