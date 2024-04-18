import numpy as np

def myf_DEP(sys_param,channel,solutions):

    No_W = sys_param["sigma_square_W"]

    No_W_unc = sys_param["noise_uncertainty_zeta"]

    h_DW = channel["h_DW"]

    P_D = solutions["P_D"]


    numerator = np.abs(h_DW)**2 * P_D + (1 / No_W_unc) * No_W

    denominator = (1/No_W_unc)*No_W

    

    # DEP = (1/2)*(1-(1/(2*np.log(No_W_unc))) * np.log(numerator/denominator))

    DEP = (1/2)*(1-(1/2*np.log(No_W_unc)) * np.log(numerator/denominator))

    return DEP