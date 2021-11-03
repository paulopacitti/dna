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
    result = match(chains_list, chains_dict)
    print(result)

def match_recursive(curr_chain, final_combinations, chains_dict):
    possible_combinations = combinations(curr_chain, chains_dict)
    if not possible_combinations:
        return curr_chain

    for e in possible_combinations:
        final_combinations.append(match_recursive(curr_chain + e, final_combinations, chains_dict))
    
    return curr_chain

def match(dna_list, chains_dict):
    final_combinations = []
    for e in dna_list:
        if not combinations(e, chains_dict):
            final_combinations.append(e)
        else:
            match_recursive(e, final_combinations, chains_dict)
    
    print(final_combinations)

    remove_list = []
    for i in final_combinations:
        for x in final_combinations:
            if x.find(i) != -1:
                if len(x) > len(i):
                    remove_list.append(i)
                elif len(x) < len(i): 
                    remove_list.append(x)
    
    print(remove_list)
    
    return [item for item in final_combinations if item not in remove_list]

def combinations(chain, chains_dict):
    possible_key = "start_" + chain[-4:]
    if possible_key in chains_dict:
        return chains_dict[possible_key]
    else:
        return False

if __name__ == "__main__":
    main()
