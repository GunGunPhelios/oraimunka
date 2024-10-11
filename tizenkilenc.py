import texttable as tt

tb= tt.Texttable()

tb.header(["ID", "Vezetéknév", "Keresztnév", "Lakhely"])
tb.add_row([1, "Györgyi", "Ádám", "Békéscsaba"])
tb.add_row([2, "Szkiva", "Gergely", "Szeged"])
tb.add_row([3, "Szalai", "Bence", "Szeged"])
tb.add_row([4, "Kondocs", "Bence", "Szeged"])
tb.add_row([5, "Gazdag", "Detti", "Makó"])
tb.add_row([6, "Tőkés", "Martin", "Szeged"])
tb.add_row([7, "Vigh", "Greta", "Kistelek"])
tb.add_row([8, "Borók", "Maja", "Szeged",])
tb.add_row([9, "Sánta", "Vivien", "Szeged"])
tb.add_row([10, "Grósz", "Patrik", "Üllés"])
tb.add_row([11, "Halasz-Szabo", "Daniel", "Szeged"])
tb.add_row([12, "Császár", "Róbert", "Mórahalom"])

print(tb.draw())

