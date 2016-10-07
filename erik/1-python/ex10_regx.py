import re

def get_matching_words(regex):
     words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

     return [word for word in words if re.search(regex, word)]


# contains v
#print get_matching_words('v')
# contains ss
#print get_matching_words('ss')
# ends with e
#print get_matching_words('e')
# b any char then b
# print get_matching_words('b\wb')
# b then any chars than another b
#print get_matching_words('[b.*b]')
# contains all vowels in a row
#print get_matching_words('aeiou')
# and of these letters regular expression
#print get_matching_words('[regular expression]')
# contain double letter
print get_matching_words(r'(.)\1+')
