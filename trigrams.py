from ast import IsNot
import math
from functools import reduce

def find_x_grams(text: str, length: int):
    # Dictionary to store the trigrams and their data
    trigram_data = {}

    # Iterate through the string and extract all 3-letter combinations
    for i in range(len(text) - length-1):
        trigram = text[i:i+length]  # Extract the trigram from the string
        position = i           # The position of the trigram in the string

        # If the trigram is already in the dictionary, update its count and add the new position
        if trigram in trigram_data:
            trigram_data[trigram]['count'] += 1
            trigram_data[trigram]['positions'].append(position)
        else:
            # If it's a new trigram, initialize it with count 1 and its position
            trigram_data[trigram] = {'count': 1, 'positions': [position]}
    
    # Sort the trigrams by count (highest to lowest)
    sorted_trigrams = sorted(trigram_data.items(), key=lambda x: x[1]['count'], reverse=False)
    
    return sorted_trigrams

# Example usage
text = "gzpqgkviegmhjoxagjibwtaczxkeysytpqszoeivirbuieeyqxanjnicmqwssgnwwthcthoqecygufcpchzqutismavigkeastuecakqmxlrsdytkvbhrtcdbrzktgrxcieytdpilpnrkcwhtvtudpfkmegfwpedacvtsfrfiqvilijhzcyvtdnqxetestzyvhwqsaxicpeyqktobtiqrfybicxjxgcthnegwrphkotioivpcttencklfbpltifbicsjsyiowuehsmllzglfaigjmcntzvoueelzkoomsxdeabeuxucxnvuoctkntllqrhllxavkorqcoggpbspmulhpcmpoesgrrxqazrivuxdhsdisvtwhbpozycwssweuveiggdtmlcxtojsljagprssmfxrbcgjmcndlgnznrscfiyrrlpmtbdamtteipoygzrtjzkqmxlsrpqrefmqrpxwpsecxpcdtucftyyrnmceywwgqvnjoxagrnsomclespinstwjdiekssfofoxvahzcoiyrrllxphfbipqqbhiyqrldxuoaofcqiwjehdaezkkwaomxkttivzgvpljmykvhrbcbpixufzfsrtxvvcbzfrxsikkispvimdbsmsrzeuzkqmxlnswmvbtopnhjxsilhofnhhvfspiseweemzjmgkihjoxagrsrhawawwwedwqfvqlbqwtaocsbvaaapgicxmzticguayfkgihsesyrnsymcdtyetcihxisrpgwelrtcjllipuctpwwgzqotjocvpkioaemuldduwvclccemswmgfmicgnienoajenvcjagplselkgxhsukhtpsycjzfulzgneqpsxwcrzbklqysvnzhirrthjqueqpiphqfftwcgirobpqglstfwwhlgcrzxjbeuxbuenwecwuuogapctjzshzrqmtovrcfdbtqfkvddtwhtspnvpwuuvqehuinvuoctftapsgtzcceotgkzchbtxwhtjcauocvbeacpyfzyvyisiqqqdmrpzoxidujgclfqijswwfbsgdiapegsoegdkxgrtzbscxjtkmshfscvtnoxvaqvcvtspdvpifhdhscgerlamzershludlpmcglyuxpcyntipsakmifmbhipttdmgtentxcvnrldieasxzosqcutmpaefwgmywwbtxwhtqfkvddtukgselselcovainpmcntzmultdkiadzpqrzxoxrbxucxioaewzuotzvqtzcumwpphkveigqthntbmkobvztohnmqxevhpcypqqbhochupojyvgirszschclycvgqxwlccccusdmxtiyngtwifwzgwvficastkgjfdstqwtyesyqaiycrrylddecsvioilaviyrfewjytpogeqwhahpdrrntakqmxlfsampzkcknkrybseoliaraqqnzqrlpjtxvrszvlpamjqulniygyadmswtpawzgqnpxapnrdkiidkywoepqfjifprfhfpslkeydkiidkaqrcjasxqcmysjvtwiwachuwtwpaeiascveizmzgnhuxcvidsvvrxvljecpgwelgkvopvpjdymlhofnelzkoojmysexxssiaimklnlqivshawvhpqmpwsybeufnuxxvnxoiyiclkqlzymrpxjkvsdrtssvtekukhglmhigpbsexyhqsvbvlgleoczkwdvvgstimrniahlgsyxiioidhxptdzajtzefissumzdkvxicdievajeguioemlqxtspwrgltwihaayrvrshdwtdnlnmeenxjaeynmhtawzzjmpstrtsplyxfgkkksgjicbmmsxqegvmzcwlkeemqgdovxvltuuxpkitlvbjeyfkfpvhhlfhbvscjejcarbaljgsdsgrelgurgxvqrbhcswtvcdtucczyrenxoxkckvxinvuevkzpdmgquclrxlgmxiaepjmcldzhefupympoeljpzagwkctrtjdymlbethpuogszyrlpfclkwsaoeroiys"
result = find_x_grams(text,3)

for trigram, data in result:
    print(f"Trigram: {trigram}, Count: {data['count']}, Positions: {data['positions']}")
    differences = [data['positions'][i+1] - data['positions'][i] for i in range(len(data['positions'])-1)]
    
    if differences[0] is not None:
        a = differences[0]
    if differences[1] is not None:
        b = differences[1]
        print(math.gcd(a,b))
    if differences[2] is not None:
        c = differences[2]
        print(math.gcd(a,b,c))
    if differences[3] is not None:
        d = differences[3]
        print(math.gcd(a,b,c,d))
    
    
    

