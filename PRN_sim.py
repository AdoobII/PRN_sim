import numpy as np
from link import config
#from scipy.ndimage.interpolation import shift
#from adib_type_converter import type



#get the registers' length
rlength = config.get_rlength()

#get an array containing the taps' locations for register 1
t_rs1 = config.get_taps_rs1()

#get an array containing the taps' locations for register 2
t_rs2 = config.get_taps_rs2()

#initiate register 1 with the values defined by the PRN ID in the config file
rs1 = np.array(config.get_PRN_ini(),dtype=np.bool).reshape(rlength,)

#initiate register 2 with all 1's
rs2 = np.full((rlength,),1,dtype=np.bool)

#get the PRN code length
PRN_length = config.get_PRN_length()

#initiate an array that has the size PRN_length to store the full PRN code
PRN_code = np.full((PRN_length,),1,dtype=np.bool)


#The PRN generation loop
for i in range(PRN_length):
    n_chip1 = False
    n_chip2 = False

    #Xor'ing the last chips of rs1 and rs2 and injecting it to the PRN_code array
    n_chip_PRN = np.logical_xor(rs1[-1],rs2[-1])
    PRN_code[i] = n_chip_PRN


    #making new chip of rs1
    for d in t_rs1:
        n_chip1 = np.logical_xor(rs1[d],n_chip1)

    rs1 = np.roll(rs1,1)
    rs1[0] = n_chip1

    #making new chip of rs2
    for d in t_rs2:
        n_chip2 = np.logical_xor(rs2[d],n_chip2)

    rs2 = np.roll(rs2,1)
    rs2[0] = n_chip2



PRN_code = PRN_code.astype(int)
PRN_code_oct = np.full((int(PRN_length/3),),1,dtype=np.int32)


for i in range(int(PRN_length/3)):
    PRN_code_oct[i] = (1*PRN_code[3*i]+2*PRN_code[3*i+1]+4*PRN_code[3*i+2])

PRN_code = np.flip(PRN_code)
PRN_code_oct = np.flip(PRN_code_oct)

print(PRN_code_oct)
