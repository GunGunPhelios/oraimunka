ppl= {
'szgergo' : 'Szkiva Gergő',
'gyadam' : 'Györgyi Ádám',
'bmaja': 'Borók Maja',
'svivien' : 'Sánta Vivien'}

for key,value in ppl.items():
    print(key,value)

ppl.popitem()
ppl.popitem()
ppl.popitem()


ppl.update({'redavid': 'Rédai Dávid'})

print(ppl.get('redavid'))