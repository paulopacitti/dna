# Paulo Pacitti | RA 185447
# Caio Pardal | RA 195216
# MC346 - Projeto 3

from sys import stdin

def main():
    chains_dict = {} # store dna chains in a dictionay to find possible combinations
    chains_list = [] # store dna chains given in input
    for input in stdin:
        if input == '': # If empty string is read then stop the loop
            break
        else:
            if "start_" + input[0:4] not in chains_dict:
                chains_dict["start_" + input[0:4]] = [input[:-1]] # store chains that begin with a sequence with 4 characters
            else:
                chains_dict["start_" + input[0:4]].append(input[:-1])
            if "end_" + input[-5:-1] not in chains_dict:
                chains_dict["end_" + input[-5:-1]] = [input[:-1]] # store chains that end with a sequence with 4 characters
            else:
                chains_dict["end_" + input[-5:-1]].append(input[:-1])
            chains_list.append(input[:-1]) # add input chain to chains_list
    dna_list = match(chains_list, chains_dict) # find the greates dna chains combinations
    
    for dna in dna_list: # print the greatest possible sequences
        print(dna)

def match_recursive(curr_chain, combinations_list, chains_dict):
    possible_combinations = combinations(curr_chain, chains_dict) # get all the possible sequences
    if not possible_combinations:
        return curr_chain # did not found any more sequences

    for dna in possible_combinations: # for each sequential dna, find sequences starting curr_chain + dna
        combinations_list.append(match_recursive(curr_chain + dna, combinations_list, chains_dict)) # store combination in array of all combinations
    
    return curr_chain

def match(dna_list, chains_dict):
    final_combinations = [] # store all possible combinations
    for dna in dna_list: # for each dna of the input, find the possible chain combinations
        if not combinations(dna, chains_dict): # if does not have any possible combination, store as it is
            final_combinations.append(dna)
        else:
            match_recursive(dna, final_combinations, chains_dict) # find all the possible combinations that start with dna
    
    remove_list = []
    for x in final_combinations: # maintain only the greatest combinations, removing substrings of longer chains
        for y in final_combinations:
            if y.find(x) != -1:
                if len(y) > len(x):
                    remove_list.append(x)
                elif len(y) < len(x): 
                    remove_list.append(y)
    
    return [combination for combination in final_combinations if combination not in remove_list] # lsit comprehension to remove useless combinations

def combinations(chain, chains_dict):
    possible_key = "start_" + chain[-4:] # assemble the key to find the next sequential dna
    if possible_key in chains_dict: # found sequences
        return chains_dict[possible_key]
    else:
        return False # does not have any sequences to that chain

if __name__ == "__main__":
    main()
