S=9000
V_ll_nominal=208

Ia_nominal=S/(sqrt(3)*V_ll_nominal)

Ea=5j*Ia_nominal+V_ll_nominal/sqrt(3)

Efem=V_ll_nominal/sqrt(3)
Ia=0:0.5:Efem/5;

Va=Efem*sqrt(1-(5*Ia/Efem).^2);
plot(Ia,abs(Va),'r-o')
hold on
plot(Ia,Ia*5,'b-o')

xlim([0,30])
%%

S=9000
V_ll_nominal=208

Ia_nominal=S/(sqrt(3)*V_ll_nominal)

Ea=5j*Ia_nominal+V_ll_nominal/sqrt(3)

Efem=V_ll_nominal/sqrt(3)
Ia=0:0.5:Efem/5;

Va=Efem*sqrt(1-(5*Ia/Efem).^2);
plot(Ia,abs(Va),'r-o')
hold on
plot(Ia,Ia*5,'b-o')

xlim([0,30])
xlabel('Ia Armadura [A]')
ylabel('Va [V]')