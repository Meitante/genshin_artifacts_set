from direct_solve import direct_solve
import pandas as pd
import os

column_name = ["m", "a条数", "r条数", "d条数", "A值", "r值", "d值", "期望伤害", "是否固定r", "是否固定d"]
dr_choice = [[True, False], [False, True]]

def get_file_name(use_r, use_d, attack_count):
    filepath = os.path.abspath(__file__)
    filepath = filepath[0:filepath.rfind("/")]
    filename = filepath + "/ard"
    if use_r:
        filename += "_use_r"
    elif use_d:
        filename += "_use_d"
    
    filename += "_attackCount"+str(attack_count)
    filename += ".csv"
    return filename


for choice in dr_choice:
    v_use_r = choice[0]
    v_usr_d = choice[1]
    for v_attack_count in range(0, 3):
        do_fix_r = False
        do_fix_d = False
        all_res = []
        for i in range(44, 14, -1):
            res = direct_solve(i, use_r = v_use_r, use_d = v_usr_d, attck_count = v_attack_count, fix_r = do_fix_r, fix_d = do_fix_d,toDoLog = False)
            all_res.append([i] + res)
            do_fix_r = res[-2]
            do_fix_d = res[-1]
        output_pd = pd.DataFrame(columns = column_name, data = all_res)
        output_pd.to_csv(get_file_name(v_use_r, v_usr_d, v_attack_count), encoding="utf-8")