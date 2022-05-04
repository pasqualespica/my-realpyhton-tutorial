from morse_binary_tree import Morse_Code_Bin_Tree
from morse_binary_tree_sim import Morse_Code_Bin_Tree

mc_tree = Morse_Code_Bin_Tree()
# ..- -? .
# res = mc_tree.translate_mc_to_letter("..-")  # = > "H"
## Output: UNME

input_to_decode = "..- -? . ???"
# input_to_decode = "??"
letters = input_to_decode.split(" ")
for letter in letters:
    print(letter, " => ", mc_tree.translate_mc_to_letter(letter))
    print(letter, " => ", mc_tree.translate_mc_to_letter_pas(letter))
    print("----------------------------------------------------------------")
