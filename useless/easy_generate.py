import zz

# a attack
# b attack percent
# c crit rate
# d crit damage

def generate_all_candidate_artifacts_data(zzstub):
    sss = zzstub.get_max_effetive_entry_number()
    final_res = []
    mincr = 5
    mincd = 5
    if zzstub.is_using_crit_rate:
        mincr = 4
    if zzstub.is_using_crit_damage:
        mincd = 4
    for a in range(4, 25):
        for b in range(5 - zzstub.number_of_main_attack_percent, min(25, sss + 1 - a)):
            for c in range(mincr, min(25, sss + 1 - a - b)):
                for d in range(mincd, min(25, sss + 1 - a - b - c)):
                    sum = a + b + c + d
                    if sum != sss: 
                        continue
                    if zzstub.is_legal_sub_entrys(a, b, c, d):
                        res = [a, b, c, d]
                        # print(res)
                        final_res.append(res)
    return final_res


def get_max_damage_situation(zzstub, realzz):
    all_candidates = generate_all_candidate_artifacts_data(zzstub)
    best_candidate = None
    max_damage = 0
    status = []
    for i in all_candidates:
        realzz.reset()
        # print(realzz.attack)
        realzz.equip_sub_entry(i[0], i[1], i[2], i[3])
        damage = realzz.get_damage_expectation()
        # print(damage)
        # print(i)
        if damage > max_damage:
            max_damage = damage
            best_candidate = i
            status = [realzz.attack, realzz.crit_rate, realzz.crit_damage]
            # print(realzz.attack)
    return [max_damage, best_candidate, status]



if __name__ == '__main__':

    atk = 700
    num = 1
    iscr = True
    iscd = False

    zzstub = zz.zz(atk, is_stub=True)
    zzstub.equip_main_entrys(num, iscr, iscd)

    realzz = zz.zz(atk)
    realzz.equip_main_entrys(num, iscr, iscd)
    # print(realzz.attack)

    a = get_max_damage_situation(zzstub, realzz)
    print(a[0])
    print(a[1])
    print(a[2])
    
