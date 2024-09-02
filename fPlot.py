
import numpy as np
import matplotlib.pyplot as plt

def myf_plot_locations(sys_param, locations):

    d_OS = locations["d_OS"]

    d_OD = locations["d_OD"]

    d_OR = locations["d_OR"]

    d_OW = locations["d_OW"]

    positions_S = locations["positions_S"]

    positions_D = locations["positions_D"]

    positions_R = locations["positions_R"]

    positions_W = locations["positions_W"]

    margin_percentage = 1.20

    lim_max = np.amax(np.hstack(([[d_OS]],[[d_OD]],[[d_OR]],[[d_OW]]))) * margin_percentage

    fig, axes = plt.subplots(1,1)

    axes.scatter(0, 0, marker='o', c='w', alpha=None, edgecolors='k', s=100)

    axes.scatter(positions_S[0,:],positions_S[1,:],marker='s',c='b',alpha=0.8,edgecolors='k',s=100)

    axes.scatter(positions_D[0,:],positions_D[1,:],marker='o',c='g',alpha=0.8,edgecolors='k',s=100)

    axes.scatter(positions_R[0,:],positions_R[1,:],marker='v',c='g',alpha=0.8,edgecolors='k',s=100)

    axes.scatter(positions_W[0,:],positions_W[1,:],marker='^',c='r',alpha=0.8,edgecolors='k',s=100)

    axes.text(positions_S[0,:]-lim_max/margin_percentage*0.15,
              positions_S[1,:]-lim_max/margin_percentage*0.15,
              "Source",fontsize=10)
    
    axes.text(positions_D[0,:]-lim_max/margin_percentage*0.20,
              positions_D[1,:]-lim_max/margin_percentage*0.40,
              ("Disguised\n"
                    "FD\n"
               "Destination\n"
                  "Node"), fontsize=10)
    
    axes.text(positions_R[0,:]-lim_max/margin_percentage*0.15,
              positions_R[1,:]-lim_max/margin_percentage*0.15,
              "Hidden receiver",fontsize=10)
    
    axes.text(positions_W[0,:]-lim_max/margin_percentage*0.15,
              positions_W[1,:]-lim_max/margin_percentage*0.15,
              "Warden",fontsize=10)
    axes.grid()

    axes.set_xlim(-lim_max,lim_max)

    axes.set_ylim(-lim_max,lim_max)

    axes.set_xlabel("Horizontal distance[m]")

    axes.set_ylabel("Verticall distance[m]")

    plt.savefig('node_location.png', dpi=500)

    plt.show()

def myf_plot_r_C_R(sys_param, x_axis_variables, r_C_R, x_axis_variables_label):

    fig, axes = plt.subplots(1, 1)

    axes.plot(x_axis_variables, r_C_R[0], 'b*-', markersize=12,
              markerfacecolor="None", label=r'optimal ($r_{C_R}$)')
    
    axes.plot(x_axis_variables, r_C_R[1], 'mo--', markersize=6,
              markerfacecolor="None", label=r'$5\%~P_S$ ($r_{C_R}$)')
    
    axes.plot(x_axis_variables, r_C_R[2], 'm^--', markersize=6,
              markerfacecolor="None", label=r'$1\%~P_S$($r_{C_R}$)')
    
    axes.plot(x_axis_variables, r_C_R[3], 'mX--', markersize=6,
              markerfacecolor="None", label=r'$0.1\%~P_S$($r_{C_R}$)')
    
    axes.plot(x_axis_variables, r_C_R[4], 'ks--', markersize=6,
              markerfacecolor="None", label=r'Random $P_D$($r_{C_R}$)')
    
    axes.grid()

    if x_axis_variables_label == "P_S_dBm_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Source transmit power $P_S$ [dBm]')

    elif x_axis_variables_label == "P_D_bar_dBm_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Destination transmit power $P_D$ [dBm]')

    elif x_axis_variables_label == "r_P_bar_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Minimum quality of service for public message')

    elif x_axis_variables_label == "res_SI_dB_cand":
        axes.legend(loc="best")
        axes.set_xlabel(r'Residual self-interference [dB]')

    elif x_axis_variables_label == "err_min_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Minimum DEP Threshold')

    elif x_axis_variables_label == "noise_uncertainty_bound_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Noise uncertainty bound [dB]')

    elif x_axis_variables_label == "r_C_bar":
        axes.legend(loc="best")
        axes.set_xlabel('covert rate $\overline{r}_C$')

    axes.set_ylabel(r'Average covert rate')

    axes.set_xlim(min(x_axis_variables), max(x_axis_variables))
    axes.set_ylim(0, max(np.amax(r_C_R), np.amax(r_C_R)) * 1.10)

    plt.show()

######## plot for P_D #######
def myf_plot_Solutions_P_D(sys_param,x_axis_variables,Solutions_P_D, x_axis_variables_label):

    fig, axes = plt.subplots(1,1)

    axes.plot(x_axis_variables,Solutions_P_D[0],'b*-', markersize=12,
              markerfacecolor= "None",label=r'optimal ($P_D$))')
    
    axes.plot(x_axis_variables,Solutions_P_D[1],'mo--', markersize=6,
              markerfacecolor= "None",label=r'5%~PS ($P_D$))')
    
    axes.plot(x_axis_variables,Solutions_P_D[2],'m^--', markersize=6,
              markerfacecolor= "None",label=r'1%~PS($P_D$))')
    
    axes.plot(x_axis_variables,Solutions_P_D[3],'mX--', markersize=6,
              markerfacecolor= "None",label=r'0.1%~PS($P_D$))')
    axes.plot(x_axis_variables,Solutions_P_D[4],'ks--', markersize=6,
              markerfacecolor= "None",label=r'Random%~PS ($P_D$))')
    
    axes.grid()

    if(x_axis_variables_label =="P_S_dB_cand"):
        axes.legend(loc="best")
        axes.set_xlabel('Source transmit power $P_S_dBm$')

    elif(x_axis_variables_label == "P_D_bar_dBm_cand"):
        axes.legend(loc="best")
        axes.set_xlabel('Destinations transmit power $P_S_dBm$')

    elif(x_axis_variables_label == "r_P_bar_cand"):
        axes.legend(loc="best")
        axes.set_xlabel('Minimum quality of services for public message')

    elif(x_axis_variables_label == "res_SI_dB_cand"):
        axes.legend(loc="best")
        axes.set_xlabel(r'residual self-interference')

    elif(x_axis_variables_label == "err_min_cand"):
        axes.legend(loc="best")
        axes.set_xlabel('Minimum DEP Threshold')

    elif(x_axis_variables_label == "noise_uncertainty_bound_cand"):
        axes.legend(loc="best")
        axes.set_xlabel('Noise uncertainity bound')
        
    elif x_axis_variables_label == "r_C_bar":
        axes.legend(loc="best")
        axes.set_xlabel('covert rate $\overline{r}_C$')

    axes.set_ylabel(r'Average $P_D$')

    axes.set_xlim(min(x_axis_variables),max(x_axis_variables))

    axes.set_ylim(0,max(np.amax(Solutions_P_D),np.amax(Solutions_P_D))*1.10)

    plt.show()


###### plot for DEP ######
def myf_plot_DEP(sys_param, x_axis_variables, DEP, x_axis_variables_label):
    
    fig, axes = plt.subplots(1, 1)
    
    axes.plot(x_axis_variables, DEP[0], 'b*-', markersize=12, markerfacecolor="None", label=r'Optimal (DEP)')
    axes.plot(x_axis_variables, DEP[1], 'mo--', markersize=6, markerfacecolor="None",
              label=r'$5\%~P_S$ (DEP)')
    axes.plot(x_axis_variables, DEP[2], 'm^--', markersize=6, markerfacecolor="None",
              label=r'$1\%~P_S$ (DEP)')
    axes.plot(x_axis_variables, DEP[3], 'mX--', markersize=6, markerfacecolor="None",
              label=r'$0.1\%~P_S$ (DEP)')
    axes.plot(x_axis_variables, DEP[4], 'ks--', markersize=6, markerfacecolor="None",
              label=r'$\mathrm{Random}~P_S~\mathrm{(DEP)}$')




    axes.grid()

    if x_axis_variables_label == "P_S_dBm_cand":
        
        axes.legend(loc="best")
        axes.set_xlabel('Source transmit power $P_S$ (dBm)')

    elif x_axis_variables_label == "P_D_bar_dBm_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Destination transmit power $\overline{P}_D$ (dBm)')

    elif x_axis_variables_label == "r_P_bar_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Minimum quality of service for public message QoS')

    elif x_axis_variables_label == "res_SI_dB_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Residual self-interference (dB)')

    elif x_axis_variables_label == "err_min_cand":
        axes.legend(loc="best")
        axes.set_xlabel(r'Minimum DEP Threshold,$\epsilon$')

    elif x_axis_variables_label == "noise_uncertainty_bound_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Noise uncertainty bound')

    elif x_axis_variables_label == "r_C_bar":
        axes.legend(loc="best")
        axes.set_xlabel('covert rate $\overline{r}_C$')

    axes.set_ylabel(r'Average worst-case DEP')
    axes.set_xlim(min(x_axis_variables), max(x_axis_variables))
    axes.set_ylim(bottom=None, top=0.5)
    # axes.set_ylim(0.4, 0.5)
    plt.savefig('DEP.png', dpi=500)
    plt.show()

   
#####Plot for r_P_R########

def myf_plot_r_P_R(sys_param, x_axis_variables, r_P_R, x_axis_variables_label):

    fig, axes = plt.subplots(1, 1)

    axes.plot(x_axis_variables, r_P_R[0], 'b*-', markersize=12,
              markerfacecolor="None", label=r'optimal ($r_{P_R}$)')
    
    axes.plot(x_axis_variables, r_P_R[1], 'mo--', markersize=6,
              markerfacecolor="None", label=r'$5\%~P_S$($r_{P_R}$)')
    
    axes.plot(x_axis_variables, r_P_R[2], 'm^--', markersize=6,
              markerfacecolor="None", label=r'$1\%~P_S$($r_{P_R}$)')
    
    axes.plot(x_axis_variables, r_P_R[3], 'mX--', markersize=6,
              markerfacecolor="None", label=r'$0.1\%~P_S$($r_{P_R}$)')
    
    axes.plot(x_axis_variables, r_P_R[4], 'ks--', markersize=6,
              markerfacecolor="None", label=r'Random $P_D$($r_{P_R}$)')
    
    axes.grid()

    if x_axis_variables_label == "P_S_dBm_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Source transmit power $P_S$ [dBm]')

    elif x_axis_variables_label == "P_D_bar_dBm_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Destination transmit power $P_D$ [dBm]')

    elif x_axis_variables_label == "r_P_bar_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Minimum quality of service for public message')

    elif x_axis_variables_label == "res_SI_dB_cand":
        axes.legend(loc="best")
        axes.set_xlabel(r'Residual self-interference [dB]')

    elif x_axis_variables_label == "err_min_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Minimum DEP Threshold')

    elif x_axis_variables_label == "noise_uncertainty_bound_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Noise uncertainty bound [dB]')

    elif x_axis_variables_label == "r_C_bar":
        axes.legend(loc="best")
        axes.set_xlabel('covert rate $\overline{r}_C$')

    axes.set_ylabel(r'Data rate of hidden receiver $\overline{r}_{P,R}$')

    axes.set_xlim(min(x_axis_variables), max(x_axis_variables))
    axes.set_ylim(0, max(np.amax(r_P_R), np.amax(r_P_R)) * 1.10)

    plt.show()

###### r_P_D ########

def myf_plot_r_P_D(sys_param, x_axis_variables, r_P_D, x_axis_variables_label):

    fig, axes = plt.subplots(1, 1)

    axes.plot(x_axis_variables, r_P_D[0], 'b*-', markersize=12,
              markerfacecolor="None", label=r'optimal ($r_{P_D}$)')
    
    axes.plot(x_axis_variables, r_P_D[1], 'mo--', markersize=6,
              markerfacecolor="None", label=r'$5\%~P_S$($r_{P_D}$)')
    
    axes.plot(x_axis_variables, r_P_D[2], 'm^--', markersize=6,
              markerfacecolor="None", label=r'$1\%~P_S$($r_{P_D}$)')
    
    axes.plot(x_axis_variables, r_P_D[3], 'mX--', markersize=6,
              markerfacecolor="None", label=r'$0.1\%~P_S$($r_{P_D}$)')
    
    axes.plot(x_axis_variables, r_P_D[4], 'ks--', markersize=6,
              markerfacecolor="None", label=r'Random $P_D$($r_{P_D}$)')
    
    axes.grid()

    if x_axis_variables_label == "P_S_dBm_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Source transmit power $P_S$ [dBm]')

    elif x_axis_variables_label == "P_D_bar_dBm_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Destination transmit power $P_D$ [dBm]')

    elif x_axis_variables_label == "r_P_bar_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Minimum quality of service for public message')

    elif x_axis_variables_label == "res_SI_dB_cand":
        axes.legend(loc="best")
        axes.set_xlabel(r'Residual self-interference [dB]')

    elif x_axis_variables_label == "err_min_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Minimum DEP Threshold')

    elif x_axis_variables_label == "noise_uncertainty_bound_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Noise uncertainty bound [dB]')
    elif x_axis_variables_label == "r_C_bar":
        axes.legend(loc="best")
        axes.set_xlabel('covert rate $\overline{r}_C$')

    axes.set_ylabel(r'data rate of destination node $\overline{r}_{P,D}$')

    axes.set_xlim(min(x_axis_variables), max(x_axis_variables))
    axes.set_ylim(0, max(np.amax(r_P_D), np.amax(r_P_D)) * 1.10)

    plt.show()