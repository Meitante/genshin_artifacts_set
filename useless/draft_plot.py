import zz
import matplotlib.pyplot as plt
import numpy as np

atk = 700
num = 1
iscr = True
iscd = False

realzz = zz.zz(atk)
realzz.equip_main_entrys(num, iscr, iscd)


# 4 4 x 34 -x , x >= 10, x <=24
xs = range(10, 25)
y = []
for x in xs:
    realzz.equip_sub_entry(4, 4, x, 34 - x)
    damage = realzz.get_damage_expectation()
    y.append(damage)
    # print([realzz.attack, realzz.crit_rate, realzz.crit_damage])
    # print(damage)
    realzz.reset()

print(xs)
print(y)

plt.plot(xs, y)
plt.show()