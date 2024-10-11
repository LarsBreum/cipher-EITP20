
from collections import defaultdict


alphabet = "abcdefghijklmnopqrstuvwxyz"
substitution = "whitewhitewhitewhite"

eng_freq_list = ["e", "a", "o","t", "i", "n", "h",]

substitution_two = "cbhdsfgptjklmetpqsstuvwxyz"

ciphertext = "gzpqgkviegmhjoxagjibwtaczxkeysytpqszoeivirbuieeyqxanjnicmqwssgnwwthcthoqecygufcpchzqutismavigkeastuecakqmxlrsdytkvbhrtcdbrzktgrxcieytdpilpnrkcwhtvtudpfkmegfwpedacvtsfrfiqvilijhzcyvtdnqxetestzyvhwqsaxicpeyqktobtiqrfybicxjxgcthnegwrphkotioivpcttencklfbpltifbicsjsyiowuehsmllzglfaigjmcntzvoueelzkoomsxdeabeuxucxnvuoctkntllqrhllxavkorqcoggpbspmulhpcmpoesgrrxqazrivuxdhsdisvtwhbpozycwssweuveiggdtmlcxtojsljagprssmfxrbcgjmcndlgnznrscfiyrrlpmtbdamtteipoygzrtjzkqmxlsrpqrefmqrpxwpsecxpcdtucftyyrnmceywwgqvnjoxagrnsomclespinstwjdiekssfofoxvahzcoiyrrllxphfbipqqbhiyqrldxuoaofcqiwjehdaezkkwaomxkttivzgvpljmykvhrbcbpixufzfsrtxvvcbzfrxsikkispvimdbsmsrzeuzkqmxlnswmvbtopnhjxsilhofnhhvfspiseweemzjmgkihjoxagrsrhawawwwedwqfvqlbqwtaocsbvaaapgicxmzticguayfkgihsesyrnsymcdtyetcihxisrpgwelrtcjllipuctpwwgzqotjocvpkioaemuldduwvclccemswmgfmicgnienoajenvcjagplselkgxhsukhtpsycjzfulzgneqpsxwcrzbklqysvnzhirrthjqueqpiphqfftwcgirobpqglstfwwhlgcrzxjbeuxbuenwecwuuogapctjzshzrqmtovrcfdbtqfkvddtwhtspnvpwuuvqehuinvuoctftapsgtzcceotgkzchbtxwhtjcauocvbeacpyfzyvyisiqqqdmrpzoxidujgclfqijswwfbsgdiapegsoegdkxgrtzbscxjtkmshfscvtnoxvaqvcvtspdvpifhdhscgerlamzershludlpmcglyuxpcyntipsakmifmbhipttdmgtentxcvnrldieasxzosqcutmpaefwgmywwbtxwhtqfkvddtukgselselcovainpmcntzmultdkiadzpqrzxoxrbxucxioaewzuotzvqtzcumwpphkveigqthntbmkobvztohnmqxevhpcypqqbhochupojyvgirszschclycvgqxwlccccusdmxtiyngtwifwzgwvficastkgjfdstqwtyesyqaiycrrylddecsvioilaviyrfewjytpogeqwhahpdrrntakqmxlfsampzkcknkrybseoliaraqqnzqrlpjtxvrszvlpamjqulniygyadmswtpawzgqnpxapnrdkiidkywoepqfjifprfhfpslkeydkiidkaqrcjasxqcmysjvtwiwachuwtwpaeiascveizmzgnhuxcvidsvvrxvljecpgwelgkvopvpjdymlhofnelzkoojmysexxssiaimklnlqivshawvhpqmpwsybeufnuxxvnxoiyiclkqlzymrpxjkvsdrtssvtekukhglmhigpbsexyhqsvbvlgleoczkwdvvgstimrniahlgsyxiioidhxptdzajtzefissumzdkvxicdievajeguioemlqxtspwrgltwihaayrvrshdwtdnlnmeenxjaeynmhtawzzjmpstrtsplyxfgkkksgjicbmmsxqegvmzcwlkeemqgdovxvltuuxpkitlvbjeyfkfpvhhlfhbvscjejcarbaljgsdsgrelgurgxvqrbhcswtvcdtucczyrenxoxkckvxinvuevkzpdmgquclrxlgmxiaepjmcldzhefupympoeljpzagwkctrtjdymlbethpuogszyrlpfclkwsaoeroiys"

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

def frequency_doubles (c):
    counts = {}
    for i in range(len(c) - 1):
        if c[i] == c[i + 1]:
            double_letter = c[i:i + 2]
            counts[double_letter] = counts.get(double_letter, 0) + 1
    # Sort the dictionary by frequency in descending order
    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_counts

def frequency_triples (c):
    counts = {}
    for i in range(len(c) - 1):
        if c[i] == c[i + 1] and c[i] == c[i + 2]:
            triple_letter = c[i:i + 3]
            counts[triple_letter] = counts.get(triple_letter, 0) + 1
    # Sort the dictionary by frequency in descending order
    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_counts

def most_common_letter_pairs(c):
    # Dictionary to store the frequency of letter pairs
    pair_freq = defaultdict(int)

    # Iterate through the text to find all letter pairs
    for i in range(len(c) - 1):
        pair = c[i:i+2]  # Get the pair of consecutive letters
        pair_freq[pair] += 1

    # Sort the dictionary by frequency in descending order
    sorted_pairs = dict(sorted(pair_freq.items(), key=lambda item: item[1], reverse=True))

    return sorted_pairs

def decode(c, alphabet, substitution_alphabet):
    decode_map = {substitution_alphabet[i]: alphabet[i] for i in range(len(alphabet))}

    decoded_message = ""

    for char in c:
        if char in decode_map:
            # Replace the character using the decode map
            decoded_message += decode_map[char]
        else:
            # If character is not in the substitution alphabet (e.g., space or punctuation), leave it unchanged
            decoded_message += char
    
    return decoded_message


# print(frequency(ciphertext))
#print(frequency_doubles(ciphertext))
print(frequency_triples(ciphertext))
#print(most_common_letter_pairs(ciphertext))


print(decode(ciphertext, alphabet, substitution))
