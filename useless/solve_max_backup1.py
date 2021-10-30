from sympy import *

ba,na,m,nr,br,nd,bd,ca,cr,cd, xr = symbols("ba, na, m, nr, br, nd, bd, ca, cr, cd, xr")

# solve formula 2,3 to get nd represented by nr
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("联立2，3式,解出nd，用nr表达")
res_nd_nr = linsolve([cr*(bd + nd*cd) - (br+nr*cr)*cd], [nd])
# pprint(res_nd_nr)
expr_nd_nr = next(iter(res_nd_nr))[0]
pprint(expr_nd_nr)

# solve formula 1,2 to get na reprensented by nr
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("联立1，2式,解出na，用nr表达")
res_na_nr = nonlinsolve([ca + ca*(br + nr*cr)*(bd+nd*cd) - (1+na*ca)*cr*(bd+nd*cd)], [na])
# pprint(res_na_nr)
res_na_nr = res_na_nr.subs(nd, expr_nd_nr)
# pprint(res_na_nr)
expr_na_nr = next(iter(res_na_nr))[0]
pprint(expr_na_nr)

# solve 
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("代入限制式，解出nr")
expr_m = na + nd + nr - m
expr_nr_constant = expr_m.subs([(na, expr_na_nr),(nd, expr_nd_nr)])
pprint(expr_nr_constant)
# res_nr = nonlinsolve([expr_nr_constant], [nr])
# # pprint(res_nr)
# expr_nr = next(iter(res_nr))[0]
# pprint(expr_nr)

# print("代入基本数值")
# expr_nr_values_no_m = expr_nr.subs([(br, 0.05), (bd, 0.5), (ca, 0.04975), (cr, 0.033), (cd, 0.066)])
# pprint(expr_nr_values_no_m)

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("代入基本数值, 设定一个m")
expr_nr_values_no_m = expr_nr_constant.subs([(br, 0.05), (bd, 0.5), (ca, 0.04975), (cr, 0.033), (cd, 0.066), (m, 21)])
pprint(expr_nr_values_no_m)
# res = solve_rational_inequalities([[((expr_nr_values_no_m, 0), "<=")]])
res1 = simplify(expr_nr_values_no_m)
pprint(res1)

expr_nr_equal_med_nr = (xr-0.1)/0.066
res2 = res1.subs(nr, expr_nr_equal_med_nr)
pprint(res2)

res3 = simplify(res2)
pprint(res3)