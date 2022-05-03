import random

def airdrop_lottery(dict, num_winners=1):
    address_list=[]
    total_tokens_weight=[]
    #load dictionary and traverse  the values to replaces the tokens with the number of items in that list
    address_dict=dict
    
    #traverese the values and store in a list
    #set the values as the weightes
    #use random.choices to pick from the list of addresses based on the corresponding weights
    for a in address_dict:
        address_list.append(a)
        num_tokens=len(address_dict[a])
        total_tokens_weight.append(num_tokens)

    print(address_list)
    print("address list", len(address_list))
    print(total_tokens_weight)
    print("token weight list", len(total_tokens_weight))

    #pick a winner with the total_tokens_weight as the weighted random choice
    winners =random.choices(address_list, weights=total_tokens_weight, k=num_winners)
    print(winners)
    return winners
