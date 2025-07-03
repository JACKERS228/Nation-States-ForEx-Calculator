def cs():
    import os
    import platform as plat
    if plat.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    return
