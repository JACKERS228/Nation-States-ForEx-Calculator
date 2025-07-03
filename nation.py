class ScriptNation:
    def __init__(self,name,avg_ann_inc):
        self.name = name
        self.avg_ann_inc = avg_ann_inc
    
    @staticmethod
    def create_sc_nat(name=None,avg_inc:int=None):
        ret_nation =  ScriptNation(name=name,avg_ann_inc=avg_inc)
        return ret_nation
        pass