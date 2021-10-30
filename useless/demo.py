import zz

# a attack
# b attack percent
# c crit rate
# d crit damage

def isvalid(main_data, artifacts_data):
# main data: [a, b, c, d]
# artifacts_data: [[a1,b1,c1,d1], [a2,b2,c2,d2], [a3,.....] ......]
    for i in range(4):
        sum = 0
        for j in range(5):
            sum += artifacts_data[j][i]
        if sum != main_data[i]:
            return False
    return True


def get_all_possible_candidate_artifact(sum, abandon = -1):
    res = []
    for a in range(sum + 1):
        if abandon == 0 and a != 0:
            continue
        if abandon != 0 and a == 0:
            continue
        for b in range(sum + 1 - a):
            if abandon == 1 and b != 0:
                continue
            if abandon != 1 and b == 0:
                continue
            if a == 0 and b == 0:
                continue
            for c in range(sum + 1 - a - b):
                if abandon == 2 and c != 0:
                    continue
                if abandon != 2 and c == 0:
                    continue
                if a == 0 and c == 0:
                    continue
                if b == 0 and c == 0:
                    continue
                for d in range(sum + 1 - a - b -c):
                    if abandon == 3 and d != 0:
                        continue
                    if abandon != 3 and d == 0:
                        continue
                    if a + b + c + d == sum:
                        res.append([a, b, c, d])
    return res

def lets_go(zzstub, main_data):
    # we will list all candidate artifacts_datra here, and pick valid one
    A1 = []
    A2 = []
    A3 = []
    A4 = []
    A5 = []

    A1 = get_all_possible_candidate_artifact(9, -1)
    A2 = get_all_possible_candidate_artifact(8, 0)
    if zzstub.number_of_main_attack_percent == 3:
        A3 = get_all_possible_candidate_artifact(8, 1)
        A4 = get_all_possible_candidate_artifact(8, 1)
        A5 = get_all_possible_candidate_artifact(8, 1)
    elif zzstub.number_of_main_attack_percent == 2:
        A3 = get_all_possible_candidate_artifact(8, 1)
        A4 = get_all_possible_candidate_artifact(8, 1)
        if zzstub.is_using_crit_rate:
            A5 = get_all_possible_candidate_artifact(8, 2)
        elif zzstub.is_using_crit_damage:
            A5 = get_all_possible_candidate_artifact(8, 3)
        else:
            A5 = get_all_possible_candidate_artifact(9, -1)
    elif zzstub.number_of_main_attack_percent == 1:
        A3 = get_all_possible_candidate_artifact(8, 1)
        A4 = get_all_possible_candidate_artifact(9, -1)
        if zzstub.is_using_crit_rate:
            A5 = get_all_possible_candidate_artifact(8, 2)
        elif zzstub.is_using_crit_damage:
            A5 = get_all_possible_candidate_artifact(8, 3)
        else:
            A5 = get_all_possible_candidate_artifact(9, -1)
    else:
        A3 = get_all_possible_candidate_artifact(9, -1)
        A4 = get_all_possible_candidate_artifact(9, -1)
        A5 = get_all_possible_candidate_artifact(9, -1)
    # print(A1)
    # print(A2)
    # print(A3)
    # print(A4)
    # print(A5)
    
    f = open("1000attack-One-Rate.txt", "w")
    for f1 in A1:
        for f2 in A2:
            for f3 in A3:
                for f4 in A4:
                    for f5 in A5:
                        candidate = [f1,f2,f3,f4,f5]
                        # print([f1,f2,f3,f4,f5])
                        if isvalid(main_data, candidate):
                            print(candidate)
                            for i in range(5):
                                for j in range(4):
                                    f.write(str(candidate[i][j]) + ",")
                            f.write("\n")
                            # print("1111111111111111111111111111111111111")
    f.flush()
    f.close()

    # A1 = get_all_possible_candidate_artifact(9, -1)
    # A2_
    # A3_num = 9 # TBD
    # A4_num = 9 # TBD
    # A5_num = 9 # TBD
    # if zzstub.number_of_attack_percent == 3:
    #     A3_num = 8
    #     A4_num = 8
    #     A5_num = 8
    # elif zzstub.number_of_attack_percent == 2:
    #     A3_num = 8
    #     A4_num = 8
    #     if zzstub.is_using_crit_rate or zzstub.is_using_crit_damage:
    #         A5_num = 8
    #     else:
    #         A5_num = 9
    # elif zzstub.number_of_attack_percent == 1:
    #     A3_num = 8
    #     A4_num = 9
    #     if zzstub.is_using_crit_rate or zzstub.is_using_crit_damage:
    #         A5_num = 8
    #     else:
    #         A5_num = 9
def generate_all_valid_artifacts_data(zzstub):
    sss = zzstub.get_max_effetive_entry_number()
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
                    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                    print([a,b,c,d])
                    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                    lets_go(zzstub, [a, b, c, d])

if __name__ == '__main__':
    zzstub = zz.zz(1000, is_stub=True)
    zzstub.equip_main_entrys(1, True, False)
    generate_all_valid_artifacts_data(zzstub)