
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
              "Disguised/FD/DestiantinNode",fontsize=10)
    
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

    plt.show()

def myf_plot_test(r_C_R,x_axis_cand):

    plt.figure()
    x_axis_cand = x_axis_cand
    
    plt.plot(x_axis_cand, r_C_R[0], 'k^-', linewidth=2, markersize=8, label=f'covert Rate optimal 5% Ps (rC,R)')

    plt.plot(x_axis_cand, r_C_R[1], 'go-', linewidth=2, markersize=6, label=f'covert Rate optimal 1% Ps (rC,R)')

    plt.plot(x_axis_cand, r_C_R[2], 'ys-', linewidth=2, markersize=4, label=f'covert Rate optimal 0.1% Ps (rC,R)')

    plt.plot(x_axis_cand, r_C_R[3], 'b*-', linewidth=2, markersize=4, label=f'covert Rate optimal 0.01% Ps (rC,R)')

    plt.plot(x_axis_cand, r_C_R[4], 'v-', color='orange', linewidth=2, markersize=4, label=f'covert Rate optimal Random PD (rC,R)')
    # plt.xticks(x_axis_cand, [f'{val:.1f}' for val in x_axis_cand])
    
    plt.grid(True)
    plt.legend()
    plt.xlabel('noise uncertainty bound dB')
    plt.ylabel('Covert rate')
    plt.show()

def myf_plot_r_C_R(sys_param, x_axis_variables, r_C_R, x_axis_variables_label):

    fig, axes = plt.subplots(1, 1)

    axes.plot(x_axis_variables, r_C_R[0], 'b*-', markersize=12,
              markerfacecolor="None", label=r'optimal ($r_{C_R}$)')
    
    axes.plot(x_axis_variables, r_C_R[1], 'mo--', markersize=6,
              markerfacecolor="None", label=r'$5\%~P_S$ optimal ($r_{C_R}$)')
    
    axes.plot(x_axis_variables, r_C_R[2], 'm^--', markersize=6,
              markerfacecolor="None", label=r'$1\%~P_S$ optimal ($r_{C_R}$)')
    
    axes.plot(x_axis_variables, r_C_R[3], 'mX--', markersize=6,
              markerfacecolor="None", label=r'$0.1\%~P_S$ optimal ($r_{C_R}$)')
    
    axes.plot(x_axis_variables, r_C_R[4], 'ks--', markersize=6,
              markerfacecolor="None", label=r'Random $P_D$ optimal ($r_{C_R}$)')
    
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

    axes.set_ylabel(r'Average covert rate')

    axes.set_xlim(min(x_axis_variables), max(x_axis_variables))
    axes.set_ylim(0, max(np.amax(r_C_R), np.amax(r_C_R)) * 1.10)

    plt.show()

def myf_plot_Solutions_P_D(sys_param,x_axis_variables,Solutions_P_D, x_axis_variables_label):

    fig, axes = plt.subplots(1,1)

    axes.plot(x_axis_variables,Solutions_P_D[0],'b*-', markersize=12,
              markerfacecolor= "None",label=r'optimal ($P_D$))')
    
    axes.plot(x_axis_variables,Solutions_P_D[1],'mo--', markersize=6,
              markerfacecolor= "None",label=r'5%~PS ooptimal ($P_D$))')
    
    axes.plot(x_axis_variables,Solutions_P_D[2],'m^--', markersize=6,
              markerfacecolor= "None",label=r'1%~PS optimal ($P_D$))')
    
    axes.plot(x_axis_variables,Solutions_P_D[3],'mX--', markersize=6,
              markerfacecolor= "None",label=r'0.1%~PS optimal ($P_D$))')
    axes.plot(x_axis_variables,Solutions_P_D[4],'ks--', markersize=6,
              markerfacecolor= "None",label=r'Random%~PS optimal ($P_D$))')
    
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

    axes.set_ylabel(r'Average covert rate ')

    axes.set_xlim(min(x_axis_variables),max(x_axis_variables))

    axes.set_ylim(0,max(np.amax(Solutions_P_D),np.amax(Solutions_P_D))*1.10)

    plt.show()



def myf_plot_DEP(sys_param, x_axis_variables, DEP, x_axis_variables_label):

    fig, axes = plt.subplots(1, 1)

    axes.plot(x_axis_variables, DEP[0], 'b*-', markersize=12, markerfacecolor="None", label=r'optimal (DEP)')
    axes.plot(x_axis_variables, DEP[1], 'mo--', markersize=6, markerfacecolor="None",
              label=r'$5\%~P_S$ optimal (DEP)')
    axes.plot(x_axis_variables, DEP[2], 'm^--', markersize=6, markerfacecolor="None",
              label=r'$1\%~P_S$ optimal (DEP)')
    axes.plot(x_axis_variables, DEP[3], 'mX--', markersize=6, markerfacecolor="None",
              label=r'$0.1%~P_S$ optimal (DEP)')
    axes.plot(x_axis_variables, DEP[4], 'ks--', markersize=6, markerfacecolor="None",
              label=r'$Random%~P_S$ optimal ($DEP$)')

    axes.grid()

    if x_axis_variables_label == "P_S_dB_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Source transmit power $P_S$ (dBm)')

    elif x_axis_variables_label == "P_D_bar_dBm_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Destination transmit power $P_D$ (dBm)')

    elif x_axis_variables_label == "r_P_bar_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Minimum quality of service for public message')

    elif x_axis_variables_label == "res_SI_dB_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Residual self-interference (dB)')

    elif x_axis_variables_label == "err_min_cand":
        axes.legend(loc="best")
        axes.set_xlabel(r'Minimum DEP Threshold,$\epsilon$')

    elif x_axis_variables_label == "noise_uncertainty_bound_cand":
        axes.legend(loc="best")
        axes.set_xlabel('Noise uncertainty bound')

    axes.set_ylabel(r'Average covert rate')
    axes.set_xlim(min(x_axis_variables), max(x_axis_variables))
    axes.set_ylim(0.4, 0.5)

    plt.show()

   
