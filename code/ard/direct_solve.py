from sympy import *

def getOnlySolution(setForm):
    return next(iter(setForm))[0]

ba,na,m,nr,br,nd,bd,ca,cr,cd, xr, NA, CA, ya = symbols("ba, na, m, nr, br, nd, bd, ca, cr, cd, xr, NA, CA, ya")

init_data = {
    "br": 0.05, # 除开主词条和副词条之外的暴击率，包括初始的5%， 套装加成, 武器加成，深渊BUFF，角色升级带去的，等等等等一切你想模拟的情况
    "bd": 0.5, # 除开主词条和副词条之外的暴击率，包括初始的50%， 套装加成，武器加成，各种BUFF，角色升级带去的，等等等等一切你想模拟的情况
    "ya": 311 # 非基础攻击力中，除开圣遗物大攻击(主副)加成，剩下的攻击力，包含羽毛主词条，套装加成，武器加成，甚至说是各种拐，班尼特，九条，各种各种，等等你想模拟的情况
}

# use_r 代表使用暴击帽
# use_d 代表使用爆伤帽
# attack_count 代表杯和时计使用了几个主词条大攻击
def direct_solve(gom, yourBasicAttack = 1000, use_r = False, use_d = False, attck_count = 0, fix_r =False, fix_d = False, toDoLog = True,):
    global init_data
    constants = [(br, init_data["br"] + 0.33 if use_r else 0), (bd, init_data["bd"] + 0.66 if use_d else 0),\
                    (NA, attck_count),(ca, 0.04975), (cr, 0.033), (cd, 0.066),  \
                    (CA, 0.466), (ba, yourBasicAttack), (m, gom), (ya, init_data["ya"])]
    if fix_d:
        constants.append((nd, 4 if use_d else 5))
    elif fix_r:
        constants.append((nr, 4 if use_r else 5))

    # 写出总攻击力，总爆率， 总爆伤的表达式
    if toDoLog:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    expr_A = (ba*(1+NA*CA+na*ca) + ya)
    expr_A = expr_A.subs(constants)
    if toDoLog:
        print("总攻击力:")
        pprint(expr_A)

    expr_r = br+nr*cr
    expr_r = expr_r.subs(constants)
    if toDoLog:
        print("总爆率:")
        pprint(expr_r)

    expr_d = bd+nd*cd
    expr_d = expr_d.subs(constants)
    if toDoLog:
        print("总爆伤")
        pprint(expr_d)

    # 写出方程组，联立Lnd和Lnr的式子已经化简/排除了2组解
    if toDoLog:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    
    expr_12 = ba*ca + ba*ca*(br+nr*cr)*(bd+nd*cd) - (ba*(1+NA*CA+na*ca) + ya)*cr*(bd+nd*cd)
    expr_13 = ba*ca + ba*ca*(br+nr*cr)*(bd+nd*cd) - (ba*(1+NA*CA+na*ca) + ya)*(br+nr*cr)*cd
    # expr_23 = ba*(1+na*ca)*cr*(bd+nd*cd)- ba*(1+na*ca)*(br+nr*cr)*cd
    expr_23 = -bd/cd + br/cr +nr - nd
    expr_4 = na + nr + nd - m

    expr_12_after_sub = expr_12.subs(constants)
    expr_13_after_sub = expr_13.subs(constants)
    expr_23_after_sub = expr_23.subs(constants)
    expr_4_after_sub = expr_4.subs(constants)

    # 根据现在是什么模式，fix_r？fix_d？ 挑选方程组求解
    if toDoLog:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

    if fix_d:
        if toDoLog:
            print("固定nd, 求解以下方程")
            pprint(expr_4_after_sub)
            pprint(expr_12_after_sub)
            print("解为")
        res = solve([expr_4_after_sub, expr_12_after_sub], [na ,nr])
        if toDoLog:
            pprint(res)
        value_na = res[na]
        value_nr = res[nr]
        value_nd = 4 if use_d else 5
    elif fix_r:
        if toDoLog:
            print("固定nr, 求解以下方程")
            pprint(expr_4_after_sub)
            pprint(expr_13_after_sub)
            print("解为")
        res = solve([expr_4_after_sub, expr_13_after_sub], [na ,nd])
        if toDoLog:
            pprint(res)
        value_na = res[na]
        value_nr = 4 if use_r else 5
        value_nd = res[nd]
    else:
        if toDoLog:
            print("求解以下方程")
            pprint(expr_4_after_sub)
            pprint(expr_13_after_sub)
            pprint(expr_23_after_sub)
        res = solve([expr_4_after_sub, expr_13_after_sub, expr_23_after_sub], [na, nr, nd])
        if toDoLog:
            pprint(res)
        value_na = res[0][0]
        value_nr = res[0][1]
        value_nd = res[0][2]

    # 根据模式，由解获得最终输出，或者根据解的情况，决定r或者d，进行再一次求解
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    if fix_r:
        value_A = expr_A.subs([(na, value_na), (nd, value_nd)])
        value_r = expr_r.subs([(na, value_na), (nd, value_nd)])
        value_d = expr_d.subs([(na, value_na), (nd, value_nd)])
        E = value_A + value_A*value_r*value_d
        print(value_na, value_nr, value_nd, value_A, value_r, value_d, E)
        return [value_na, value_nr, value_nd, value_A, value_r, value_d, E, True, False] # True 表示结果是fix_r的
    elif fix_d:
        value_A = expr_A.subs([(na, value_na), (nr, value_nr)])
        value_r = expr_r.subs([(na, value_na), (nr, value_nr)])
        value_d = expr_d.subs([(na, value_na), (nr, value_nr)])
        E = value_A + value_A*value_r*value_d
        print(value_na, value_nr, value_nd, value_A, value_r, value_d, E)
        return [value_na, value_nr, value_nd, value_A, value_r, value_d, E, False, True] # True 表示结果是fix_d的
    else:
        # 非固定 r 和 d
        value_A = expr_A.subs([(na, value_na), (nr, value_nr), (nd, value_nd)])
        value_r = expr_r.subs([(na, value_na), (nr, value_nr), (nd, value_nd)])
        value_d = expr_d.subs([(na, value_na), (nr, value_nr), (nd, value_nd)])
        E = value_A + value_A*value_r*value_d
        print(value_na, value_nr, value_nd, value_A, value_r, value_d, E)
        if not S.Reals.contains(value_nr):
            print("复数解，完蛋啦！")
            return [value_na, value_nr, value_nd, value_A, value_r, value_d, E, False, False]
        elif value_nr < (4 if use_r else 5):
            print("nr 小于 最小值啦，后面开始固定 nr")
            return direct_solve(gom, yourBasicAttack, use_r, use_d, attck_count, fix_r = True, fix_d= False, toDoLog = False)
        elif value_nd < (4 if use_d else 5):
            print("nd 小于 最小值啦，后面开始固定 nr")
            return direct_solve(gom, yourBasicAttack, use_r, use_d, attck_count, fix_r = False, fix_d= True, toDoLog = False)
        else:
            return [value_na, value_nr, value_nd, value_A, value_r, value_d, E, False, False]


if __name__ == "__main__":
    gom = 25
    # direct_solve(gom, use_r = True, use_d = False, 2, fix_d = False,toDoLog = False)

    res = direct_solve(39, 1000, use_r = True, use_d = False, attck_count = 0, fix_r = False, fix_d = False,toDoLog = False)
    pprint(res)