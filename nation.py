import os
class ScriptNation:
    def __init__(self,name,currency,avg_ann_inc):
        self.name = name
        self.currency = currency
        self.avg_ann_inc = avg_ann_inc
    
    @staticmethod
    def create_sc_nat(name=None,currency:str=None,avg_inc:float=None):
        ret_nation =  ScriptNation(name=name,currency=currency,avg_ann_inc=avg_inc)
        return ret_nation
    
    def calculate_exchange_rate(self,nation2):
        # Currency 1
        monthly_inc1:float = self.avg_ann_inc / 12
        weekly_inc1:float = monthly_inc1 / 4
        daily_inc1:float =  weekly_inc1 / 7

        big_mac1 = round(daily_inc1 * 0.07,2)
        print(f"In {self.name}, a Big-Mac would cost around {big_mac1} {self.currency}")
        grande_latte1 = round(daily_inc1 * 0.046,2)
        print(f"In {self.name}, a Grande Latte would cost around {grande_latte1} {self.currency}")
        bread1 = round(daily_inc1 * 0.012,2)
        print(f"In {self.name}, a loaf of bread would cost around {bread1} {self.currency}")

        total_basket1 =  round(big_mac1 + grande_latte1 + bread1,2)
        print(f"A very average day in {self.name} would cost about {total_basket1} {self.currency}")
        print("")
        # Currency 2
        monthly_inc2:float = nation2.avg_ann_inc / 12
        weekly_inc2 = monthly_inc2 / 4
        daily_inc2 =  weekly_inc2 / 7

        big_mac2 = round(daily_inc2 * 0.07,2)
        print(f"In {nation2.name}, a Big-Mac would cost around {big_mac2} {nation2.currency}")
        grande_latte2 = round(daily_inc2 * 0.046,2)
        print(f"In {nation2.name}, a Grande Latte would cost around {grande_latte2} {nation2.currency}")
        bread2 = round(daily_inc2 * 0.012,2)
        print(f"In {nation2.name}, a loaf of bread would cost around {bread2} {nation2.currency}")

        total_basket2 =  round(big_mac2 + grande_latte2 + bread2,2)

        print(f"A very average day in {nation2.name} would cost about {total_basket2} {nation2.currency}")


        exchange_rate =  round(float(total_basket1 / total_basket2,),2)
        print("")

        print(f"1 {nation2.name} {nation2.currency} is about {exchange_rate} {self.name} {self.currency}")
        if exchange_rate > 1:
            print(f"This means that the {self.name} {self.currency} has less buying power than the {nation2.name} {nation2.currency}")
        else:
            print(f"This means that the {self.name} {self.currency} has more buying power than the {nation2.name} {nation2.currency}")


