import random

def airdrop_lottery(dict, num_winners=1):
    address_list=[]
    total_tokens_weight=[]
    #load dictionary and traverse  the values to replaces the tokens with the number of items in that list
    address_dict=dict
    # address_dict={'addr1qyu7l5qedhvcv8y5z8gq3z5lkyznukgp2gr4qxa7nzj0scyh6klrtehdqduz267ptxrzyufzme0xj2wxj2jzhkjvuy5suc7l6r': ['otranto2131'], 'addr1w999n67e86jn6xal07pzxtrmqynspgx0fwmcmpua4wc6yzsxpljz3': ['otranto2444', 'otranto1129', 'otranto2344', 'otranto1569', 'otranto2329', 'otranto1162', 'otranto1680', 'otranto2138', 'otranto1966', 'otranto1289', 'otranto1938', 'otranto1224', 'otranto2117', 'otranto1998', 'otranto825', 'otranto1121'], 'addr1q9w3q8d5n5q4nmmva9x5areduk46kd9tkgt7jzhueg2ytgw2ycw6xm2zmdc59kzjgtaxeptc079nz6u0saeq8nepf03sq4ldck': ['otranto2170', 'otranto1392', 'otranto1122'], 'addr1qxj89hacsuymmgkuyylkr7dntgtsr5u98c2hph9vucwax505d584wvegxlttpsahce9nfles6vm6dq6wlymsx9q52ctqr5yqjx': ['otranto2411', 'otranto2051'], 'addr1q9kwdej9rv3x7d6xa6yl0vjpnget4algjg7lqgu56ujpea7u9h57qxc5h7r5jfr075gpmv922na9y62n75k8wjz3a6zs8uxphy': ['otranto1776', 'otranto1584', 'otranto950'], 'addr1qx8qyr0d3gks28ncpuatvzma0v0jk7w3gshsr8hehnpvl3tz4mqqwxzfpecq33rh2fsd8jka8pus9986h23guzahtpgs5r6l57': ['otranto807', 'otranto1870', 'otranto1821', 'otranto2136', 'otranto1450'], 'addr1qxjaujxx35wvej359vgzdje93c7ewqmt4s8n27afznpn85sy024cnnv8u4tf2rz2htcqqu6xvk6yx33sgqgcrks88z7steakr0': ['otranto2242'], 'addr1q8cm20aaql8jl0s5fh7ql44cv5xmwd06p38ph73uz7fpq5s0l98lfxv4wgjj8tfnspql6yw99e54glnk26vd9238eccqe76ftk': ['otranto2325', 'otranto1863', 'otranto1645', 'otranto1293', 'otranto1161'], 'addr1qyweqpm5cllnejhpjaj0wzs9yat54g6nptelrttau32z304prhdyxq7r65vdjdxxrnh4ewr8yerusjpzpyknze7rhf9svz72na': ['otranto1197'], 'addr1q9vpf5483s2russ2j0tm4yfqxlyx47q6km95mhxtnkqprwxw4nrrt85snuq392t44lsytm30en85djqp5v2vq5xj0zrq7v8vla': ['otranto1610'], 'addr1q89n3yaj72zdwnfteh72lg3clmhsaekpdqh7cjv4tcm4gr0ny56hvh80fus2d8yujyg5mcudht8sefx7kvtmdqs2vg3qdrphph': ['otranto2202', 'otranto1761'], 'addr1q9let094wpskgmxmn3qvmc2t06kkrm27lwwa8p5p0keey4l88k58whr5hscqq2a768j3ewrac82jp5f845th0dwqjq3s2j0fq0': ['otranto2348', 'otranto2309', 'otranto2254', 'otranto1959', 'otranto1741', 'otranto1011'], 'addr1q9qgvldyx7rhdsww7azy62anf3grct9x52t0e9736g9jrq4tl8e78hm26lts3jtgedla87fzq4u5m3zfpf4rmjsfplyqkyruhe': ['otranto2245', 'otranto1789', 'otranto1253']}

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
