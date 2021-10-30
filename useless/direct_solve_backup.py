from sympy import *

def getOnlySolution(setForm):
    return next(iter(setForm))[0]

ba,na,m,nr,br,nd,bd,ca,cr,cd, xr, NA, CA = symbols("ba, na, m, nr, br, nd, bd, ca, cr, cd, xr, NA, CA")

def direct_solve(gom, use_r = False, use_d = False, attck_count = 0, fix_d = False, toDoLog = True):
    constants = [(br, 0.05 + 0.33 if use_r else 0), (bd, 0.5 + 0.66 if use_d else 0), (NA, attck_count),(ca, 0.04975), (cr, 0.033), (cd, 0.066),  (CA, 0.466), (ba, 1)]
    if fix_d:
        constans.append((nd, 4))

    if toDoLog:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    expr_A = ba*(1+NA*CA+na*ca)
    expr_A = expr_A.subs(constants)
    if toDoLog:
        pprint(expr_A)

    expr_r = br+nr*cr
    expr_r = expr_r.subs(constants)
    if toDoLog:
        pprint(expr_r)

    expr_d = bd+nd*cd
    expr_d = expr_d.subs(constants)
    if toDoLog:
        pprint(expr_d)

    if toDoLog:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    expr_13 = ba*ca + ba*ca*(br+nr*cr)*(bd+nd*cd) - ba*(1+NA*CA+na*ca)*(br+nr*cr)*cd
    # expr_23 = ba*(1+na*ca)*cr*(bd+nd*cd)- ba*(1+na*ca)*(br+nr*cr)*cd
    expr_23 = -bd/cd + br/cr +nr - nd
    expr_4 = na + nr + nd - m

    expr_13_after_sub_without_m = expr_13.subs(constants)
    expr_23_after_sub_without_m = expr_23.subs(constants)

    if toDoLog:
        pprint(expr_4)
        pprint(expr_13_after_sub_without_m)
        pprint(expr_23_after_sub_without_m)

    # res = solve([expr_4, expr_13_after_sub_without_m, expr_23_after_sub_without_m], [na, nr, nd])
    # pprint(res)
    if toDoLog:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    expr_13_after_sub = expr_13_after_sub_without_m.subs([(m, gom)])
    expr_23_after_sub = expr_23_after_sub_without_m.subs([(m, gom)])
    expr_4_after_sub = expr_4.subs([(m, gom)])

    # res = solve([expr_4_after_sub, expr_13_after_sub, expr_23_after_sub], [na, nr, nd])
    # pprint(res)
    res = solve([expr_4_after_sub, expr_13_after_sub, expr_23_after_sub], [na, nr, nd], domain =S.Reals)
    pprint(res)

    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    value_A = expr_A.subs([(na, res[0][0]), (nr, res[0][1]), (nd, res[0][2])])
    value_r = expr_r.subs([(na, res[0][0]), (nr, res[0][1]), (nd, res[0][2])])
    value_d = expr_d.subs([(na, res[0][0]), (nr, res[0][1]), (nd, res[0][2])])
    E = value_A + value_A*value_r*value_d
    print(value_A, value_r, value_d, value_A/value_r, E)

if __name__ == "__main__":
    gom = 39
    use_r = False
    use_d = True
    direct_solve(gom, use_r, use_d, 0, False)