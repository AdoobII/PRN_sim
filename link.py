class config:
    def get_rlength():
        f = open("config.ini", "r")
        k = f.readlines()
        f.close()
        for i in range(len(k)):
            if(k[i] == "register_length\n"):
                i = k[i+1]
                break
        return int(i)


    def get_PRN_ini():
        f = open("config.ini", "r")
        k = f.readlines()
        f.close()
        for i in range(len(k)):
            if(k[i] == "SPS_signal_type\n"):
                i = k[i+1]
                break
        for d in range(len(k)):
            if(k[d] == "PRN_ID\n"):
                d = k[d+1]
                d = int(d)
                break

        if(i == "L5-SPS\n"):
            f = open("PRN_L5.ini","r")
            k = f.readlines()
            f.close()
            i = k[d-1]
            i = i.replace("\n","")


        elif(i == "S-SPS\n"):
            f = open("PRN_S.ini","r")
            k = f.readlines()
            f.close()
            i = k[d-1]
            i = i.replace("\n","")

        return [int(d) for d in i]

    def get_PRN_length():
        f = open("config.ini", "r")
        k = f.readlines()
        f.close()
        for i in range(len(k)):
            if(k[i] == "PRN_code_length\n"):
                i = k[i+1]
                break
        return int(i)

    def get_taps_rs1():
        f = open("config.ini", "r")
        k = f.readlines()
        f.close()
        for i in range(len(k)):
            if(k[i] == "taps_rs1\n"):
                i = k[i+1]
                break

        i = i.replace("\n","")

        return [int(d) for d in i]

    def get_taps_rs2():
        f = open("config.ini", "r")
        k = f.readlines()
        f.close()
        for i in range(len(k)):
            if(k[i] == "taps_rs2\n"):
                i = k[i+1]
                break

        i = i.replace("\n","")

        return [int(d) for d in i]
