from ast import IsNot
from collections import defaultdict
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
    print(sorted_trigrams)
    
    return sorted_trigrams

# Example usage
text = "gzpqgkviegmhjoxagjibwtaczxkeysytpqszoeivirbuieeyqxanjnicmqwssgnwwthcthoqecygufcpchzqutismavigkeastuecakqmxlrsdytkvbhrtcdbrzktgrxcieytdpilpnrkcwhtvtudpfkmegfwpedacvtsfrfiqvilijhzcyvtdnqxetestzyvhwqsaxicpeyqktobtiqrfybicxjxgcthnegwrphkotioivpcttencklfbpltifbicsjsyiowuehsmllzglfaigjmcntzvoueelzkoomsxdeabeuxucxnvuoctkntllqrhllxavkorqcoggpbspmulhpcmpoesgrrxqazrivuxdhsdisvtwhbpozycwssweuveiggdtmlcxtojsljagprssmfxrbcgjmcndlgnznrscfiyrrlpmtbdamtteipoygzrtjzkqmxlsrpqrefmqrpxwpsecxpcdtucftyyrnmceywwgqvnjoxagrnsomclespinstwjdiekssfofoxvahzcoiyrrllxphfbipqqbhiyqrldxuoaofcqiwjehdaezkkwaomxkttivzgvpljmykvhrbcbpixufzfsrtxvvcbzfrxsikkispvimdbsmsrzeuzkqmxlnswmvbtopnhjxsilhofnhhvfspiseweemzjmgkihjoxagrsrhawawwwedwqfvqlbqwtaocsbvaaapgicxmzticguayfkgihsesyrnsymcdtyetcihxisrpgwelrtcjllipuctpwwgzqotjocvpkioaemuldduwvclccemswmgfmicgnienoajenvcjagplselkgxhsukhtpsycjzfulzgneqpsxwcrzbklqysvnzhirrthjqueqpiphqfftwcgirobpqglstfwwhlgcrzxjbeuxbuenwecwuuogapctjzshzrqmtovrcfdbtqfkvddtwhtspnvpwuuvqehuinvuoctftapsgtzcceotgkzchbtxwhtjcauocvbeacpyfzyvyisiqqqdmrpzoxidujgclfqijswwfbsgdiapegsoegdkxgrtzbscxjtkmshfscvtnoxvaqvcvtspdvpifhdhscgerlamzershludlpmcglyuxpcyntipsakmifmbhipttdmgtentxcvnrldieasxzosqcutmpaefwgmywwbtxwhtqfkvddtukgselselcovainpmcntzmultdkiadzpqrzxoxrbxucxioaewzuotzvqtzcumwpphkveigqthntbmkobvztohnmqxevhpcypqqbhochupojyvgirszschclycvgqxwlccccusdmxtiyngtwifwzgwvficastkgjfdstqwtyesyqaiycrrylddecsvioilaviyrfewjytpogeqwhahpdrrntakqmxlfsampzkcknkrybseoliaraqqnzqrlpjtxvrszvlpamjqulniygyadmswtpawzgqnpxapnrdkiidkywoepqfjifprfhfpslkeydkiidkaqrcjasxqcmysjvtwiwachuwtwpaeiascveizmzgnhuxcvidsvvrxvljecpgwelgkvopvpjdymlhofnelzkoojmysexxssiaimklnlqivshawvhpqmpwsybeufnuxxvnxoiyiclkqlzymrpxjkvsdrtssvtekukhglmhigpbsexyhqsvbvlgleoczkwdvvgstimrniahlgsyxiioidhxptdzajtzefissumzdkvxicdievajeguioemlqxtspwrgltwihaayrvrshdwtdnlnmeenxjaeynmhtawzzjmpstrtsplyxfgkkksgjicbmmsxqegvmzcwlkeemqgdovxvltuuxpkitlvbjeyfkfpvhhlfhbvscjejcarbaljgsdsgrelgurgxvqrbhcswtvcdtucczyrenxoxkckvxinvuevkzpdmgquclrxlgmxiaepjmcldzhefupympoeljpzagwkctrtjdymlbethpuogszyrlpfclkwsaoeroiys"
result = find_x_grams(text,3)


for trigram, data in result:
    if data['count'] == 4:
        print(f"Trigram: {trigram}, Count: {data['count']}, Positions: {data['positions']}")
        differences = [data['positions'][i+1] - data['positions'][i] for i in range(len(data['positions'])-1)]

        # for all that has counts == 3 => calculate gcd
        print(math.gcd(differences[0],differences[1] ))
        

        # if len(differences) >= 4:
        #     a = differences[0]
        #     if differences[1] is not None:
        #         b = differences[1]
        #         print(math.gcd(a,b))
        #     if differences[2] is not None:
        #         c = differences[2]
        #         print(math.gcd(a,b,c))
        #     if differences[3] is not None:
        #         d = differences[3]
        #         print(math.gcd(a,b,c,d))
        
# c = ciphertext, length = length of the key, positions = vector of positions
# Returns vector of strings, containing the parts of the cipher  
  
def divide_cipher(c, length):

    sections = [c[i:i+length] for i in range(0, len(c), length)]

    return sections
    
    

sections = divide_cipher(text, 27)
print(sections)

def frequency (c):
    # Initialize a defaultdict with integer default value
    freq_dict = defaultdict(int)
    
    # Iterate over each character in the string
    for char in c:
        # If the character is a letter, count its occurrence (ignores case)
        if char.isalpha():
            freq_dict[char.lower()] += 1
    
    # Convert defaultdict to a regular dictionary
    return dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))

print(frequency(sections[3]))

s = "geihsivtielxxrw"

# g = e, e = g, i = k, h = j, s = u, i = k, v = y, t = v, i = k, e = g, x = z, x = z, r = t, w = x

"""
    Function that takes each section, and calculates the shift, based on the most frequent letter (e in English)
    We know, that the first letter in each section will have the same shift.
    We also know that the second letter in each section will have the same shift. Same for the nth letter...

    Thus, take the nth letter of each section and shift based on the shift calculated above.

"""


#gzpqgkviegmhjoxagjibwtaczxk
# g = e => 6-4=2 => c (g=c)

#gzpqgkviegmhjoxagjibwtaczxk
#c###c###########c##########

#eysytpqszoeivirbuieeyqxanjn
# e = e => 4-4 => a (e=a)
#eysytpqszoeivirbuieeyqxanjn
#a#########a#######aa#######

#icmqwssgnwwthcthoqecygufcpc
# c = e => 2-4 = 25 => y (c=y)
##y###########y#####y###y#y

#hzqutismavigkeastuecakqmxlr
# a = e => 0-4 = 23 => w (a=w)
#hzqutismavigkeastuecakqmxlr
#########w#####w#####w######

# sub = plain
# r = e => 17 - 4 = 13 => n (kanske "n" koder för r i 0:e sektionen)
# p = e => 15 - 4 = 11 => l (kanske "l" koder för "p" i första sektionen)
# h = e => 8 - 4 = 4 => e (kanske "e" koder för h i andra sektionen)
# k = e => 11 - 4 = 7 => h (kanske "h" koder för "e" i tredje sektionen)


# kqmxlrsdytkvbhrtcdbrzktgrxc
# h####n####h##en####n#h##n##

# kqmxlsrpqrefmqrpxwpsecxpcdt
# h#####nl#n#####l##l####l###

# kqmxlnswmvbtopnhjxsilhofnhh
# h############l#e#####e###ee

# kqmxlrsdytkvbhrtcdbrzktgrxc
# h####n####h##en####n#h##n