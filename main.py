import nationstates as ns
import fetch as f
import sys
from nation import ScriptNation as SN

TEST_MODE = True
ENABLE_DUMP_DOWNLOAD = False
daily_dump = None
api = ns.Nationstates("ForExCalc")

def main():
    import xml
    import xml.etree
    import xml.etree.ElementTree as ET
    from nation import ScriptNation as SN
    if ENABLE_DUMP_DOWNLOAD:
        f.download_daily_dumps(urls=f.URLS)
    else:
        pass

    nationstree = ET.parse(r"dumps\nations.xml")
    nationsroot = nationstree.getroot()
    perdition = api.region("the Plains of Perdition")

    nationsdata = nationsroot.findall('NATION')

    perd_nations:list[str] = []
    script_nations:list[SN] = []

    ### Main user loop
    nation1 = api.nation(input("Please input the first nation:")) # User inputs EXACT name of the nation
    for nation in nationsdata:
        if nation.findtext("NAME") == nation1.nation_name:
            nation1_class = SN.create_sc_nat(name=nation.findtext("NAME"),currency=nation.findtext("CURRENCY"),avg_inc=float(nation1.get_shards(ns.Shard("census",scale="72",mode="score"))['census']['scale']['score']))
            print(nation1_class.name, nation1_class.currency, nation1_class.avg_ann_inc)
            continue

    nation2 = api.nation(input("Now the second nation: "))
    for nation in nationsdata:
        if nation.findtext("NAME") == nation2.nation_name:
                nation2_class = SN.create_sc_nat(name=nation.findtext("NAME"),currency=nation.findtext("CURRENCY"),avg_inc=float(nation2.get_shards(ns.Shard("census",scale="72",mode="score"))['census']['scale']['score']))
                print(nation2_class.name, nation2_class.currency, nation2_class.avg_ann_inc)
                continue
    
    nation1_class.calculate_exchange_rate(nation2_class)
    
            
if __name__ == "__main__":
    print(main())