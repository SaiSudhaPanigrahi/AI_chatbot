import enchant

def spellchecker(title):
	try:
		d = enchant.Dict("en_US")
	except ImportError:
		print ("Enchant Library Not Found. Spell Checking Failed.")
		return title
	options = []
	newt = ""
	ccount = 0
	fail = "no"
	for word in title.split(" "):
		if d.check(word) is True:
			newt = newt + word + " "
		else:
			clist = d.suggest(word)
			word = clist[ccount]
			newt = newt + word + " "
			fail = "yes"
	return print (newt)
	
	
	
	
spellchecker("sadf")