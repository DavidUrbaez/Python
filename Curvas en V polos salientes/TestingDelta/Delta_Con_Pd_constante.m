%% Settings
clc 
clear all
close all

min_x = 0;
max_x = 4;
min_y = 0;
max_y = 1.4;
Ia_max=1.25

%% Code
Pd_total=3*[0,0.25,0.5,0.75,1];
Start=[0.01,0.01,0.325,0.665,1];
Xq=0.66;
Xd=1.02;
Va=1;
for i=1:5 %Iter over constant Power
    Ea_total=Start(i):0.05:2.3;

    Pd=Pd_total(i);
   
    Ia_total=[];
    delta_total=[];
    for Ea=Ea_total %Iter over constant induced voltage
        X=[0.5,0.01]'; % <-- [Ia,delta] <-- Vector that i want to find
        %%
        syms Ia delta
        J1=(Va*sin(delta)/Xq)^2+((Ea-Va*cos(delta))/Xd)^2 - Ia^2;                       % Ecn1
        J2=(3*Va*Ea*sin(delta)/Xd)+3*((Xd-Xq)/(Xd*Xq))*(Va^2)*sin(delta)*cos(delta)-Pd; % Ecn2
        J=jacobian([J1,J2],[Ia,delta]);
        %%
        for i=1:5 %Iter over Newton Raphson Method
            D1=double(subs(J1,[Ia,delta],X'));
            D2=double(subs(J2,[Ia,delta],X'));
            J_calculado=double(subs(J,[Ia,delta],X'));

            X=X-inv(J_calculado)*([D1,D2]');
        end
        % Y axis Limit
        if X(1)> Ia_max
            X(1)=nan
        end
        % borrable
        
        Ia_total=[Ia_total,X(1)];
        delta_total=[delta_total,X(2)];
        X(1)
    end
    hold on
    If=Ea_total/1.1+0.004*Ea_total.*exp(3.4*Ea_total);
    plot(Ea_total,delta_total*180/pi,'LineWidth',2)
end


%%
xlabel('I_{FD} [p.u.]')
ylabel('delta [ ºGrados ]')

legend('P_n = 0.00 [p.u]','P_n = 0.25 [p.u]','P_n = 0.50 [p.u]','P_n = 0.75 [p.u]','P_n = 1.00 [p.u]')