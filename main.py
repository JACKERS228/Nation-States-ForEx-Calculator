import nationstates as ns
import fetch as f
from nation import ScriptNation as SN
import json as js
import datetime as dt

api = ns.Nationstates("ForExCalc") # Prepare the NationStates API

def main():
    import utils as u
    import xml
    import xml.etree
    import xml.etree.ElementTree as ET
    from nation import ScriptNation as SN
    u.cs()
    if input(f"Update dumps from NationStates? (y/n) ").capitalize() == "Y":
        f.download_daily_dumps(urls=f.URLS)
    else:
        pass
    u.cs()
    print("Loading...")
    nationstree = ET.parse(r"dumps\nations.xml")
    nationsroot = nationstree.getroot()
    perdition = api.region("the Plains of Perdition")

    nationsdata = nationsroot.findall('NATION')

    perd_nations:list[str] = []
    script_nations:list[SN] = []

    ### Main user loop
    while True:
        u.cs()
        nation1 = api.nation(input("Please input the first nation: ")) # User inputs EXACT name of the nation
        try:
            u.cs()
            print("Loading...")
            for nation in nationsdata:
                if nation.findtext("NAME") == nation1.nation_name:
                    nation1_class = SN.create_sc_nat(name=nation.findtext("NAME"),currency=nation.findtext("CURRENCY"),avg_inc=float(nation1.get_shards(ns.Shard("census",scale="72",mode="score"))['census']['scale']['score']))
                    u.cs()
                    print(f"Nation: {nation1_class.name}")
                    print(f"Currency: {nation1_class.currency}")
                    print(f"Average Annual Income: {nation1_class.avg_ann_inc} {nation1_class.currency}/year")
                    input("Press Enter to continue... ")
                    continue
        except:
            print("An error occurred: Make sure you spelled the nation name exactly as it appears in NationStates! Also check to see if the nation still exists as of yesterday at 11:59pm|23:00 your time.")
        
        u.cs()
        nation2 = api.nation(input("Now the second nation: "))
        try:
            u.cs()
            print("Loading...")
            for nation in nationsdata:
                if nation.findtext("NAME") == nation2.nation_name:
                    nation2_class = SN.create_sc_nat(name=nation.findtext("NAME"),currency=nation.findtext("CURRENCY"),avg_inc=float(nation2.get_shards(ns.Shard("census",scale="72",mode="score"))['census']['scale']['score']))
                    u.cs()
                    print(f"Nation: {nation2_class.name}")
                    print(f"Currency: {nation2_class.currency}")
                    print(f"Average Annual Income: {nation2_class.avg_ann_inc} {nation2_class.currency}/year")
                    input("Press Enter to continue... ")
                    continue
        except:
            print("An error occurred: Make sure you spelled the nation name exactly as it appears in NationStates! Also check to see if the nation still exists as of yesterday at 11:59pm|23:00 your time.")
        u.cs()
        try:
            nation1_class.calculate_exchange_rate(nation2_class)
        except:
            print("An error occurred: Make sure you spelled the nation name exactly as it appears in NationStates! Also check to see if the nation still exists as of yesterday at 11:59pm|23:00 your time.")
        
        if input("Do another conversion? (y/n) ").capitalize() == "Y":
            pass
        else:
            print("Exiting...")
            break 
    
            
if __name__ == "__main__":
    main()