import numpy as np
a="hola"
def CaracteristicasMaquina(S=36,q=3,P=4,Nc=10,phi=50*10**-3,f=60,a=1):
    #a: caminos de corriente

    n=S/(P*q)  #Bobinas por polo y por fase - bobinas en un grupo de fase

    Te=180*P # Cantidad de grados eléctricos en la máquina

    gamma=180*P/S #grados eléctricos por ranura o paso de ranura

    rho=180-gamma*(n-1) # grados eléctricos entre bobinas o paso de bobina

    kp=np.sin(rho/2 * np.pi/180) # factor de paso

    kd=np.sin(n*gamma/2 *np.pi/180)/(n*np.sin(gamma/2 *np.pi/180)) #factor de distribucion

    kw=kp*kd #Factor de devanado

    Ne=P*n*Nc*kw/a # Numero de vueltas efectivas

    Ea=(2*np.pi/np.sqrt(2))*Ne*f*phi #Voltaje de fase - Ea=(4.44)*Ne*f*pow

    data={'n':n,
          'Te':Te,
          'gamma':gamma,
          'rho':rho,
          'kp':kp,
          'kd':kd,
          'kw':kw,
          'Ne':Ne,
          'Ea':Ea}

    return data

data=CaracteristicasMaquina(S=36,q=3,P=4,Nc=10,phi=50*10**-3,f=60,a=1)
print('Voltaje en la fase: ',data['Ea'],'[V]')
