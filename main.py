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

    for element in nationsdata:
        if element.findtext("REGION") == "the Plains of Perdition":
            perd_nations.append(element.findtext("NAME"))
            continue
            print(f"Region: {element.findtext('REGION')} Nation: {element.findtext('NAME')}")

    ec_values:dict = {}
    if TEST_MODE is True:
        for nation in perd_nations:
            focus = api.nation(nation)
            script_nations.append(SN.create_sc_nat(name=nation,avg_inc=focus.get_shards(ns.Shard("census",scale="72",mode="score"))['census']['scale']['score']))
            sys.exit(1)
        else:
            pass
    if TEST_MODE is False:
        for nation in perd_nations:
    
            focus = api.nation(nation)
            script_nations.append(SN.create_sc_nat(name=nation,avg_inc=focus.get_shards(ns.Shard("census",scale="72",mode="score"))['census']['scale']['score']))
            

            


        

if __name__ == "__main__":
    print(main())