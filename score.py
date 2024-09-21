import random

card= [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
comp = []
# computer.append(one_card())
sums = sum(comp)
while sums<17:
    x = random.choice(card)
    
    comp.append(x)
    card.remove(x)
    sums = sum(comp)

sum1 = sum(comp)
computer1 = comp
cards = card



art = '''
B                              JJJJJJJJJJJJJJJJJ
B B                                    J 
B  B                                   J
B   B                                  J
B  B                                   J
B B                                    J
BB          -------------              J
B B                                    J
B  B                             J     J
B   B                              J   J
B  B                                J  J
B B                                  J J
B                                     JJ


'''