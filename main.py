import numpy as np

from fParam import*

from fChannel import*

from fAlgorithm import*

from fPlot import*

from tqdm import tqdm

sys_param = system_parametes()

num_samples = 1000

x_axis_name ="P_S_dBm_cand"

if (x_axis_name == "P_S_dBm_cand"):

    x_axis_cand = np.arange(start=0, stop=55, step=5)

elif(x_axis_name == "r_C_bar"):

    x_axis_cand = np.arange(start=0,stop=0.30, step=0.03)

elif(x_axis_name=="r_P_bar_cand"):

    x_axis_cand = np.arange(start=0, stop=2.2, step=0.2)

elif(x_axis_name=="err_min_cand"):

    x_axis_cand = np.arange(start = 0, stop = 0.55, step = 0.05)

elif(x_axis_name=="res_SI_DB_cand"):

    x_axis_cand = np.arange(start = -150, stop = -40, step = 10)

elif(x_axis_name=="noise_uncertainty_bound_cand"):

    x_axis_cand = np.arange(start=0.5, stop=5.5, step=0.5)      


num_algorithms = 5


r_D_E_P = np.zeros((num_algorithms,np.size(x_axis_cand)))

solutions_P_D = np.zeros((num_algorithms,np.size(x_axis_cand, axis=0 )))

r_P_R = np.zeros((num_algorithms,np.size(x_axis_cand)))

r_P_D = np.zeros((num_algorithms,np.size(x_axis_cand)))

r_C_R = np.zeros((num_algorithms,np.size(x_axis_cand)))

for ind1 in tqdm(range(0,num_samples)):

    param_locations = {}

    param_locations["seed_seq"] = ind1

    locations = myf_locations(sys_param,param_locations)

    if(ind1==0):

        myf_plot_locations(sys_param,locations)

    param_channel = {}

    param_channel["seed_seq"] = num_samples + ind1

    channel = myf_channel(sys_param,locations,param_channel)

    r_D_E_P_temp = np.zeros((num_algorithms,np.size(x_axis_cand)))

    solutions_P_D_temp = np.zeros((num_algorithms,np.size(x_axis_cand)))

    r_P_R_temp = np.zeros((num_algorithms,np.size(x_axis_cand)))

    r_P_D_temp = np.zeros((num_algorithms,np.size(x_axis_cand)))

    r_C_R_temp = np.zeros((num_algorithms,np.size(x_axis_cand)))

    for ind2 in range(0,np.size(x_axis_cand, axis=0)):

        if(x_axis_name == "P_S_dBm_cand" ) :

            sys_param["P_S_dBm"] = x_axis_cand[ind2]

            sys_param["P_S"] = 10**(sys_param["P_S_dBm"]/10) / (10**3)
        
        elif(x_axis_name == "r_C_bar"):

            sys_param["r_C_bar"] = x_axis_cand[ind2]

        elif(x_axis_name == "r_P_bar_cand"):

            sys_param["r_P_bar"] = x_axis_cand[ind2]

        elif(x_axis_name=="err_min_cand"):

            sys_param["epsilon"] = x_axis_cand[ind2]   

        elif(x_axis_name == "res_SI_DB_cand"):

            sys_param["sigma_square_SI"] = x_axis_cand[ind2]

            sys_param["res_SI"] = 10**(sys_param["sigma_square_SI"] / 10)

        elif(x_axis_name == "noise_uncertainty_bound_cand"):

            sys_param["noise_uncertainty_zeta_dB"] = x_axis_cand[ind2]

            sys_param["noise_uncertainty_zeta"] = 10**(sys_param["noise_uncertainty_zeta_dB"] / 10)



        solutions_algorithm_1 = myf_algorihtm_1(sys_param,channel)

        r_D_E_P_temp[0,ind2] = myf_DEP(sys_param,channel,solutions_algorithm_1)

        solutions_P_D_temp[0,ind2] = solutions_algorithm_1["P_D"]

        r_P_R_temp[0,ind2] = myf_r_P_R(sys_param,channel,solutions_algorithm_1)

        r_P_D_temp[0,ind2] = myf_r_P_D(sys_param,channel,solutions_algorithm_1)

        r_C_R_temp[0,ind2] = myf_r_C_R(sys_param,channel,solutions_algorithm_1)



        solutions_algorithm_2 = myf_algorithm_2(sys_param,channel,0.05)
        
        r_D_E_P_temp[1,ind2] = myf_DEP(sys_param,channel,solutions_algorithm_2)

        solutions_P_D_temp[1,ind2] = solutions_algorithm_2["P_D"]

        r_P_R_temp[1,ind2] = myf_r_P_R(sys_param,channel,solutions_algorithm_2)

        r_P_D_temp[1,ind2] = myf_r_P_D(sys_param,channel,solutions_algorithm_2)

        r_C_R_temp[1,ind2] = myf_r_C_R(sys_param,channel,solutions_algorithm_2)



        solutions_algorithm_3 = myf_algorithm_2(sys_param,channel,0.01)

        r_D_E_P_temp[2,ind2] = myf_DEP(sys_param,channel,solutions_algorithm_3)

        solutions_P_D_temp[2,ind2] = solutions_algorithm_2["P_D"]

        r_P_R_temp[2,ind2] = myf_r_P_R(sys_param,channel,solutions_algorithm_3)

        r_P_D_temp[2,ind2] = myf_r_P_D(sys_param,channel,solutions_algorithm_3)

        r_C_R_temp[2,ind2] = myf_r_C_R(sys_param,channel,solutions_algorithm_3)


        solutions_algorithm_4 = myf_algorithm_2(sys_param,channel,0.001)

        r_D_E_P_temp[3,ind2] = myf_DEP(sys_param,channel,solutions_algorithm_4)

        solutions_P_D_temp[3,ind2] = solutions_algorithm_4["P_D"]

        r_P_R_temp[3,ind2] = myf_r_P_R(sys_param,channel,solutions_algorithm_4)

        r_P_D_temp[3,ind2] = myf_r_P_D(sys_param,channel,solutions_algorithm_4)

        r_C_R_temp[3,ind2] = myf_r_C_R(sys_param,channel,solutions_algorithm_4)


        solutions_algorithm_5 = myf_algorithm_2(sys_param,channel,np.random.rand())

        r_D_E_P_temp[4,ind2] = myf_DEP(sys_param,channel,solutions_algorithm_5)

        solutions_P_D_temp[4,ind2] = solutions_algorithm_4["P_D"]

        r_P_R_temp[4,ind2] = myf_r_P_R(sys_param,channel,solutions_algorithm_5)

        r_P_D_temp[4,ind2] = myf_r_P_D(sys_param,channel,solutions_algorithm_5)

        r_C_R_temp[4,ind2] = myf_r_C_R(sys_param,channel,solutions_algorithm_5)

    
    
    r_D_E_P = (ind1 + 1 - 1) / (ind1 + 1) * r_D_E_P + 1/(ind1 + 1)*r_D_E_P_temp

    solutions_P_D = (ind1 + 1 - 1) / (ind1 + 1) * solutions_P_D + 1/(ind1 + 1)*solutions_P_D_temp

    r_P_R = (ind1 + 1 - 1) / (ind1 + 1) * r_D_E_P + 1/(ind1 + 1) * r_P_R_temp

    r_P_D = (ind1 + 1 - 1) / (ind1 + 1) * r_P_D + 1/(ind1 + 1) * r_P_D_temp

    r_C_R = (ind1 + 1 - 1) / (ind1 + 1) * r_C_R + 1/(ind1 + 1) * r_C_R_temp




# myf_plot_DEP(sys_param,x_axis_cand,r_D_E_P,x_axis_name)

# myf_plot_Solutions_P_D(sys_param,x_axis_cand,solutions_P_D, x_axis_name)
    

myf_plot_r_P_R(sys_param, x_axis_cand, r_P_R, x_axis_name)

myf_plot_r_P_D(sys_param,x_axis_cand,r_P_D,x_axis_name)

myf_plot_r_C_R(sys_param,x_axis_cand,r_C_R,x_axis_name)
    





