import numpy as np

from fParam import*

from fChannel import*

from fAlgorithm import*

from fPlot import*

sys_param = system_parametes()

num_samples = 1

x_axis_name ="err_min_cand"

if (x_axis_name == "P_S_dBm_cand"):

    x_axis_cand = np.arange(start=0, stop=55, step=5)

elif(x_axis_name=="err_min_cand"):

     x_axis_cand = np.arange(start = 0, stop = 0.55, step = 0.05)

num_algorithms = 1


r_D_E_P = np.zeros((num_algorithms,np.size(x_axis_cand)))

for ind1 in range(0,num_samples):

    param_locations = {}

    param_locations["seed_seq"] = ind1

    locations = myf_locations(sys_param,param_locations)

    # if(ind1==0):

    #     myf_plot_locations(sys_param,locations)

    param_channel = {}

    param_channel["seed_seq"] = num_samples + ind1

    channel = myf_channel(sys_param,locations,param_channel)

    r_D_E_P_temp = np.zeros((num_algorithms,np.size(x_axis_cand)))

    for ind2 in range(0,np.size(x_axis_cand, axis=0)):

        if(x_axis_name == "P_S_dBm_cand" ) :

            sys_param["P_S_dBm"] = x_axis_cand[ind2]

            sys_param["P_S"] = 10**(sys_param["P_S_dBm"]/10) / (10**3)

        elif(x_axis_name =="err_min_cand"):

            sys_param["epsilon"] = x_axis_cand[ind2]
  
        solutions_algorithm_1 = myf_algorihtm_1(sys_param,channel)

        r_D_E_P_temp[0,ind2] = myf_DEP(sys_param,channel,solutions_algorithm_1)

        
    print(r_D_E_P_temp)
    # r_D_E_P = (ind1 + 1 - 1) / (ind1 + 1) * r_D_E_P + 1/(ind1 + 1)*r_D_E_P_temp

    # print(r_D_E_P)



    

    





