import numpy as np

def system_parametes():

    sys_param = {}

    sys_param["BW"] = 20 * 10**6

    sys_param["d_OS_range"] = 100
    
    sys_param["d_OD_range"] = 100

    sys_param["d_OR_range"] = 100

    sys_param["d_OW_range"] = 100

    sys_param["P_S_dBm"] = 23

    sys_param["P_S"] = 10**(sys_param["P_S_dBm"]/10) / (10**3)

    sys_param["P_D_bar_dBm"] = 23

    sys_param["P_D_bar"] = 10**(sys_param["P_D_bar_dBm"] / 10) / (10**3)

    sys_param["r_P_bar"] = 0.1

    sys_param["sigma_square_W_dB"] = -160

    sys_param["sigma_square_W"] = 10**(sys_param["sigma_square_W_dB"]/10)/(10**3) *   sys_param["BW"]

    sys_param["noise_uncertainty_zeta_dB"] = 5

    sys_param["noise_uncertainty_zeta"] = 10**(sys_param["noise_uncertainty_zeta_dB"]/10)

    sys_param["sigma_square_D_dB"] = -160

    sys_param["sigma_square_D"] = 10**(sys_param["sigma_square_D_dB"]/10)/(10**3) * sys_param["BW"]

    sys_param["sigma_square_R_dB"] = -160

    sys_param["sigma_square_R"] = 10**(sys_param["sigma_square_R_dB"]/10)/(10**3) * sys_param["BW"]

    sys_param["sigma_square_SI_dB"] = -100

    sys_param["sigma_square_SI"] = 10**(sys_param["sigma_square_SI_dB"]/10) 

    sys_param["epsilon"] = 0.45

    sys_param["beta"] = 3.5

    sys_param["r_C_bar"] = 0.5




    return sys_param


