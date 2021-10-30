# attack            14   16   18   19
# attack percent    4.1  4.7  5.3  5.8
# crit rate         2.7  3.1  3.5  3.9
# crit damage       5.4  6.2  7.0  7.8

# then we will use expectation of each value
# attack            16.75
# attack percent    4.975
# crit rate         3.3
# crit damage       6.6

# Considering zz's limit intelligence , this class excludes elemental mastery

class zz(object):
    attack_per_entry = 16.75
    attack_percent_per_entry = 0.04975
    crit_rate_per_entry = 0.033
    crit_damage_per_entry = 0.066


    attack_percent_per_main = 0.466
    crit_rate_per_main = 0.311
    crit_damage_per_main = 0.622

    max_number_of_sub_entry_in_one = 6

    def __init__(self, basic_attack, extra_attack_percent = 0, extra_crit_rate = 0, extra_crit_damage = 0, is_stub = False):
        # basic means zz is lv90, and equipped with a lv90 weapon
        self.basic_attack = basic_attack
        self.extra_attack_percent_from_weapon = extra_attack_percent # just record it for now.
        self.is_stub = is_stub # stub is not real calculating, but just for test.
        self.extra_crit_rate = extra_crit_rate
        self.extra_crit_damage = extra_crit_damage



        # We assume, when number_of_main_attack_percent is 1, then this one is the third 圣遗物
        # if it is 2, then these two are the third and the fourth
        self.number_of_main_attack_percent = 0
        self.is_using_crit_rate = False
        self.is_using_crit_damage = False
        self.max_effetive_entry = 44

        self.attack = 0
        self.crit_rate = 0.05
        self.crit_damage = 0.5
        self.reset(True)
        

    def reset(self, is_first = False):
        self.attack = self.basic_attack + self.basic_attack * self.extra_attack_percent_from_weapon
        self.crit_rate = 0.05 + self.extra_crit_rate
        self.crit_damage = 0.5 + self.extra_crit_damage
        # print([self.number_of_main_attack_percent, self.is_using_crit_rate, self.is_using_crit_damage])
        self.equip_main_entrys(self.number_of_main_attack_percent, self.is_using_crit_rate, self.is_using_crit_damage, is_first)


    def equip_main_entrys(self, number_of_attack_percent, is_using_crit_rate, is_using_crit_damage, is_first = False):
        if is_using_crit_rate and is_using_crit_damage:
            raise Exception("fuck you")

        self.number_of_main_attack_percent = number_of_attack_percent
        self.is_using_crit_rate = is_using_crit_rate
        self.is_using_crit_damage = is_using_crit_damage
        if is_first:
            self.attack += number_of_attack_percent * zz.attack_percent_per_main * self.basic_attack
        else:
            self.attack += 311 + number_of_attack_percent * zz.attack_percent_per_main * self.basic_attack
        # 311 is the value from yumao
        self.number_of_main_attack_percent = number_of_attack_percent
        if is_using_crit_rate:
            self.crit_rate += zz.crit_rate_per_main
            self.is_using_crit_rate = True
        elif is_using_crit_damage:
            self.crit_damage += zz.crit_damage_per_main
            self.is_using_crit_damage = True

        self.max_effetive_entry = 44 # 9 * 5 -1, 1 for yumao
        self.max_effetive_entry -= self.number_of_main_attack_percent
        if self.is_using_crit_rate or self.is_using_crit_damage:
            self.max_effetive_entry -= 1

    def calculate_values_and_store(self, attack, attack_percent, crit_rate, crit_damage):
        self.attack += attack * zz.attack_per_entry + attack_percent * zz.attack_percent_per_entry * self.basic_attack
        self.crit_rate += crit_rate * zz.crit_rate_per_entry
        self.crit_damage += crit_damage * zz.crit_damage_per_entry

    def equip_sub_entry(self, attack, attack_percent, crit_rate, crit_damage):
        if not self.is_stub:
            self.calculate_values_and_store(attack, attack_percent, crit_rate, crit_damage)
        return True

    def equip_1_sub_entry(self, attack, attack_percent, crit_rate, crit_damage):
        # parameters here mean number of sub entrys
        if attack > 6 and attack < 1:
            return False
        elif attack_percent > 6 and attack_percent < 1:
            return False
        elif crit_rate > 6 and crit_rate < 1:
            return False
        elif crit_damage > 6 and crit_rate < 1:
            return False

        # If you can not reach max effetive sub entrys, go back to your world and play more
        if attack + attack_percent + crit_rate + crit_damage != 9:
            return False
        
        if not self.is_stub:
            self.calculate_values_and_store(attack, attack_percent, crit_rate, crit_damage)
        return True

    def equip_2_sub_entry(self, attack, attack_percent, crit_rate, crit_damage):
        # parameters here mean number of sub entrys
        if attack != 0:
            return False
        elif attack_percent > 6 and attack_percent < 1:
            return False
        elif crit_rate > 6 and crit_rate < 1:
            return False
        elif crit_damage > 6 and crit_rate < 1:
            return False

        # If you can not reach max effetive sub entrys, go back to your world and play more
        if attack + attack_percent + crit_rate + crit_damage != 8:
            return False
        
        if not self.is_stub:
            self.calculate_values_and_store(attack, attack_percent, crit_rate, crit_damage)
        return True

    def equip_3_sub_entry(self, attack, attack_percent, crit_rate, crit_damage):
        # parameters here mean number of sub entrys
        if attack > 6 and attack < 1:
            return False
        elif crit_rate > 6 and crit_rate < 1:
            return False
        elif crit_damage > 6 and crit_rate < 1:
            return False

        if self.number_of_main_attack_percent == 0:
            if attack_percent > 6 and attack_percent < 1:
                return False
            elif attack + attack_percent + crit_rate + crit_damage != 9:
                return False
        if self.number_of_main_attack_percent > 0:
            if attack_percent != 0:
                return False
            elif attack + attack_percent + crit_rate + crit_damage != 8:
                return False

        if not self.is_stub:
            self.calculate_values_and_store(attack, attack_percent, crit_rate, crit_damage)
        return True

    def equip_4_sub_entry(self, attack, attack_percent, crit_rate, crit_damage):
        # parameters here mean number of sub entrys
        if attack > 6 and attack < 1:
            return False
        elif crit_rate > 6 and crit_rate < 1:
            return False
        elif crit_damage > 6 and crit_rate < 1:
            return False

        if self.number_of_main_attack_percent <= 1:
            if attack_percent > 6 and attack_percent < 1:
                return False
            elif attack + attack_percent + crit_rate + crit_damage != 9:
                return False
        if self.number_of_main_attack_percent > 1:
            if attack_percent != 0:
                return False
            elif attack + attack_percent + crit_rate + crit_damage != 8:
                return False


        # If you can not reach max effetive sub entrys, go back to your world and play more
        if attack + attack_percent + crit_rate + crit_damage != 9:
            return False
        
        if not self.is_stub:
            self.calculate_values_and_store(attack, attack_percent, crit_rate, crit_damage)
        return True

    def equip_5_sub_entry(self, attack, attack_percent, crit_rate, crit_damage):
        # parameters here mean number of sub entrys
        if attack > 6 and attack < 1:
            return False

        if self.is_using_crit_rate:
            if attack_percent > 6 and attack_percent < 1:
                return False
            elif crit_damage > 6 and crit_rate < 1:
                return False
            elif crit_rate != 0:
                return False
            elif attack + attack_percent + crit_rate + crit_damage != 8:
                return False
        elif self.is_using_crit_damage:
            if attack_percent > 6 and attack_percent < 1:
                return False
            elif crit_rate > 6 and crit_rate < 1:
                return False
            elif crit_damage != 0:
                return False
            elif attack + attack_percent + crit_rate + crit_damage != 8:
                return False
        elif self.number_of_main_attack_percent == 3:
            if crit_rate > 6 and crit_rate < 1:
                return False
            elif crit_damage > 6 and crit_rate < 1:
                return False
            elif attack + attack_percent + crit_rate + crit_damage != 8:
                return False
            elif attack_percent != 0:
                return False
        elif self.number_of_main_attack_percent < 3:
            if crit_rate > 6 and crit_rate < 1:
                return False
            elif crit_damage > 6 and crit_rate < 1:
                return False
            elif attack + attack_percent + crit_rate + crit_damage != 9:
                return False
            elif attack_percent > 6 and attack_percent < 1:
                return False

        if not self.is_stub:
            self.calculate_values_and_store(attack, attack_percent, crit_rate, crit_damage)
        return True



    def get_damage_expectation(self):
        cr = min(1, self.crit_rate)
        a = self.attack * (1 - cr)
        b = self.attack * cr * (1 + self.crit_damage)
        # print(cr)
        # print(self.attack)
        # print(self.crit_damage)
        return a + b


    def get_attack(self):
        return self.attack

    def get_crit_rate(self):
        return self.crit_rate
    
    def get_crit_damage(self):
        return self.crit_damage

    def get_max_effetive_entry_number(self):
        a =  44 - self.number_of_main_attack_percent
        if self.is_using_crit_damage or self.is_using_crit_rate:
            a -= 1
        return a


    def is_legal_sub_entrys(self, attack, attack_percent, crit_rate, crit_damage):
        # parameters here mean number of sub entrys

        # If you can not reach max effetive sub entrys, go back to your world and play more
        if attack + attack_percent + crit_rate + crit_damage != self.get_max_effetive_entry_number():
            return False

        # Calculate
        if attack_percent > (5 - self.number_of_main_attack_percent) * zz.max_number_of_sub_entry_in_one:
            return False
        if self.is_using_crit_rate:
            if crit_rate > 4 * zz.max_number_of_sub_entry_in_one:
                return False
        elif self.is_using_crit_damage:
            if crit_damage > 4 * zz.max_number_of_sub_entry_in_one:
                return False

            
        
        return True

    # def get_sub_entrys(self, attack, attack_percent, crit_rate, crit_damage):
    #     if not zz.is_legal_sub_entrys(attack, attack_percent, crit_rate, crit_damage)
    #         return False


if __name__ == "__main__":
    this_zz = zz(1000)
    this_zz.equip_main_entrys(1, True, False)
    this_zz.equip_1_sub_entry(1, 1, 1, 6)
    this_zz.equip_2_sub_entry(0, 1, 1, 6)
    this_zz.equip_3_sub_entry(1, 0, 1, 6)
    this_zz.equip_4_sub_entry(1, 1, 1, 6)
    this_zz.equip_5_sub_entry(1, 1, 0, 6)
    print(this_zz.get_damage_expectation())