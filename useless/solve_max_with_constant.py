from sympy import *

def getOnlySolution(setForm):
    return next(iter(setForm))[0]

ba,na,m,nr,br,nd,bd,ca,cr,cd, xr = symbols("ba, na, m, nr, br, nd, bd, ca, cr, cd, xr")
constants = [(br, 0.05), (bd, 0.5), (ca, 0.04975), (cr, 0.033), (cd, 0.066)]

expr_13 = ba*ca + ba*ca*(br+nr*cr)*(bd+nd*cd) - ba*(1+na*ca)*(br+nr*cr)*cd
# expr_23 = ba*(1+na*ca)*cr*(bd+nd*cd)- ba*(1+na*ca)*(br+nr*cr)*cd
expr_23 = -bd/cd + br/cr +nr - nd
expr_4 = na + nr + nd - m

expr_13_after_sub_without_m = expr_13.subs(constants)
expr_23_after_sub_without_m = expr_23.subs(constants)

pprint(expr_4)
pprint(expr_13_after_sub_without_m)
pprint(expr_23_after_sub_without_m)

# res = nonlinsolve([expr_4, expr_13_after_sub_without_m, expr_23_after_sub_without_m], [na, nr, nd])
# pprint(res)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
res_na_nrnd = nonlinsolve([expr_13_after_sub_without_m], [na])
expr_na_nrnd = getOnlySolution(res_na_nrnd)
pprint(res_na_nrnd)

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
res_nd_nr = nonlinsolve([expr_23_after_sub_without_m], [nd])
expr_nd_nr = getOnlySolution(res_nd_nr)
pprint(res_nd_nr)

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
expr_na_nr = expr_na_nrnd.subs([(nd, expr_nd_nr)])
expr_na_nr = simplify(expr_na_nr)
pprint(expr_na_nr)


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
expr_0_nr_by4 = expr_4.subs([(na, expr_na_nr), (nd, expr_nd_nr)])
pprint(expr_0_nr_by4)


expr_nr_xr = (xr-0.05)/0.033
expr_xr_nr = 0.033*nr + 0.05

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
expr_0_xr_by4 = simplify(expr_0_nr_by4.subs([(nr, expr_nr_xr)]))
pprint(expr_0_xr_by4)

# print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# print("xr 无实数解")
# for i in range(1, 30):
#     this_m = i
#     expr_0_xr_by4_with_m = expr_0_xr_by4.subs([(m, this_m)])
#     res = nonlinsolve([expr_0_xr_by4_with_m], [xr])
#     print(this_m, res)

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

for i in range(1, 30):
    this_m = i
    value_xr = sqrt(15.1515151515152/90.9090909090909)
    value_nr = expr_nr_xr.subs([(xr, value_xr)])
    value_na = expr_na_nr.subs([(nr, value_nr)])
    value_nd = expr_nd_nr.subs([(nr, value_nr)])
    print(this_m, value_xr, value_nr, value_na, value_nd)