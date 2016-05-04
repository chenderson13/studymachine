def load_card(ones, fives, tens, twenties):
	dollars = ones + (5*fives) + (10*tens) + (20*twenties)
	print "Card value is %i dollars." % (dollars)

load_card(3, 1, 1, 3)