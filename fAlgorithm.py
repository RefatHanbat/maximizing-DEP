import numpy as np
from fCalculations import*

def myf_algorihtm_1(sys_param,channel):

    sigma_square_R = sys_param["sigma_square_R"]
    
    sigma_square_D = sys_param["sigma_square_D"]

    sigma_square_W = sys_param["sigma_square_W"]

    zeta = sys_param["noise_uncertainty_zeta"]

    P_S = sys_param["P_S"]

    r_C_bar = sys_param["r_C_bar"]
    
    P_D_bar =  sys_param["P_D_bar"]

    r_P_bar = sys_param["r_P_bar"]

    h_DR = channel["h_DR"]

    h_SR = channel["h_SR"]

    h_DD_tilde =  channel["h_DD_tilde"]

    h_SD = channel["h_SD"]

    h_DW = channel["h_DW"]

    h_DR_sq_mgn = np.abs(h_DR)**2

    h_SR_sq_mgn = np.abs(h_SR)**2

    h_DD_tilde_sq_mgn = np.abs(h_DD_tilde)**2

    h_SD_sq_mgn = np.abs(h_SD)**2

    h_DW_sq_mgn = np.abs(h_DW)**2

    first_portion = (sigma_square_R/h_DR_sq_mgn) * (2**(r_C_bar) - 1)

    second_portion = (1/h_DR_sq_mgn) * (h_SR_sq_mgn * P_S/(2**r_P_bar - 1) - sigma_square_R)

    third_portion = (1/h_DD_tilde_sq_mgn) * (h_SD_sq_mgn * P_S/(2**r_P_bar-1)-sigma_square_D)

    fourth_portion = (zeta - 1/zeta) * (sigma_square_W / h_DW_sq_mgn)

    P_D_ub = min(first_portion,min(second_portion,third_portion,fourth_portion,P_D_bar))

    P_D_opt = max(0,P_D_ub)

    solutions = {}

    solutions["P_D"] = np.copy(P_D_opt)
   
    return solutions

def myf_algorithm_2(sys_param,channel,P_S_proportion_fixed):

    P_S = sys_param["P_S"]

    P_D_bar = sys_param["P_D_bar"]

    r_P_bar = sys_param["r_P_bar"]

    err_min = sys_param["epsilon"]
    
    ##Function###

    P_D_opt = min(P_S_proportion_fixed * P_S,P_D_bar)

    solutions = {}

    # solutions["P_D"] = np.copy(P_D_opt)

    # if((r_P_bar <= myf_r_P_R(sys_param,channel,solutions)) and \
    #         (r_P_bar <= myf_r_P_D(sys_param,channel,solutions)) and \
    #           (myf_DEP(sys_param,channel,solutions) >= err_min)\
    #           ):
        
    #     None

    # else:
        
    #     P_D_opt = 0

    solutions["P_D"] = np.copy(P_D_opt)

    return solutions