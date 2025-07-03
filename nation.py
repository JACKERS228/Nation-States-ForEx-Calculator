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

        big_mac1 = daily_inc1 * 0.07
        grande_latte1 = daily_inc1 * 0.046
        bread1 = daily_inc1 * 0.012

        total_basket1 =  big_mac1 + grande_latte1 + bread1

        # Currency 2
        monthly_inc2:float = nation2.avg_ann_inc / 12
        weekly_inc2 = monthly_inc2 / 4
        daily_inc2 =  weekly_inc2 / 7

        big_mac2 = daily_inc2 * 0.07
        grande_latte2 = daily_inc2 * 0.046
        bread2 = daily_inc2 * 0.012

        total_basket2 =  big_mac2 + grande_latte2 + bread2

        exchange_rate =  round(float(total_basket1 / total_basket2,),2)

        print(f"1 {nation2.name + "-ian"} {nation2.currency} is about {exchange_rate} {self.name} {self.currency}")


