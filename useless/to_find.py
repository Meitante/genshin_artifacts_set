from sympy import *

def getOnlySolution(setForm):
    return next(iter(setForm))[0]

ba,na,m,nr,br,nd,bd,ca,cr,cd, xr = symbols("ba, na, m, nr, br, nd, bd, ca, cr, cd, xr")
gom = 20
constants = [(br, 0.05 + 0.33), (bd, 0.5), (ca, 0.04975), (cr, 0.033), (cd, 0.066), (ba, 1)]




expr_1 = ba*ca + ba*ca*(br+nr*cr)*(bd+nd*cd) 
expr_2 = ba*(1+na*ca)*cr*(bd+nd*cd)
expr_3 = ba*(1+na*ca)*(br+nr*cr)*cd

expr_1_after_sub = expr_1.subs(constants + [(m, gom)])
expr_2_after_sub = expr_2.subs(constants + [(m, gom)])
expr_3_after_sub = expr_3.subs(constants + [(m, gom)])

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
pprint(expr_1_after_sub)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
pprint(expr_2_after_sub)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
pprint(expr_3_after_sub)


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
expr_ra = simplify(expr_2_after_sub - expr_1_after_sub)
pprint(expr_ra) 

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
expr_da = simplify(expr_3_after_sub - expr_1_after_sub)
pprint(expr_da) 