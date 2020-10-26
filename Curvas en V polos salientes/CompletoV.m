%% Settings
clc 
clear all
close all

min_x = 0;
max_x = 4;
min_y = 0;
max_y = 1.4;
Ia_max=1.25

%%
img= imread('Image2.JPG');
imagesc([min_x max_x], [min_y max_y], flipud(img));
hold on
%% Code
Pd_total=3*[0,0.25,0.5,0.75,1];
Start=[0.01,0.01,0.3,0.65,1];
Xq=0.66;
Xd=1.02;
Va=1;
for i=1:5 %Iter over constant Power
    Ea_total=Start(i):0.05:2.3

    Pd=Pd_total(i)
   
    Ia_total=[]
    for Ea=Ea_total %Iter over constant induced voltage
        X=[0.5,0.01]'; % [Ia,delta] <- lo que quiero encontrar
        %%
        syms Ia delta
        J1=(Va*sin(delta)/Xq)^2+((Ea-Va*cos(delta))/Xd)^2 - Ia^2;
        J2=(3*Va*Ea*sin(delta)/Xd)+3*((Xd-Xq)/(Xd*Xq))*(Va^2)*sin(delta)*cos(delta)-Pd;
        J=jacobian([J1,J2],[Ia,delta]);
        %%
        for i=1:5 %Iter over Newton Raphson Method
            D1=double(subs(J1,[Ia,delta],X'));
            D2=double(subs(J2,[Ia,delta],X'));
            J_calculado=double(subs(J,[Ia,delta],X'));

            X=X-inv(J_calculado)*([D1,D2]');
        end
        % Limite en eje y
        if X(1)> Ia_max
            X(1)=nan
        end
        % borrable
        
        Ia_total=[Ia_total,X(1)];
        X(1)
    end
    hold on
    If=Ea_total/1.1+0.004*Ea_total.*exp(3.4*Ea_total);
    plot(Ea_total,Ia_total,'LineWidth',2)
end
xlim([0,4])
ylim([0,1.4])

                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                %%%          Simulación FP CTE     %%%   
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%
clear all
clc
Va=1

Xd=1.02;
Xq=0.66;
Ra=0.00812333463937716;

% [-acos(0.75) -acos(0.9) acos(1) acos(0.9) acos(0.75)]
for theta=  [-acos(0.25) -acos(0.5) -acos(0.75) -acos(0.9) acos(1) acos(0.9) acos(0.75) acos(0.5) acos(0.25)]
    %% calculos
    Ia_mag=0:0.01:1.2;
    Ia=Ia_mag.*exp(-theta*1j);
    delta=atan((abs(Ia).*Xq*cos(theta) - abs(Ia).*Ra*sin(theta))...
        ./(Va+ abs(Ia) * (Ra * cos(theta) + Xq * sin(theta))));

    Id=abs(Ia).*sin(theta+delta).*exp((delta-pi/2)*1j);

    Iq=abs(Ia).*cos(delta+theta).*exp((delta)*1j);



    Ea=Va+Id.*Xd*1j+Iq.*Xq*1j+Ra.*Ia;

    % delta %se verifica que delta es igual al ángulo de Ea
    % angle(Ea)
    Ea_mag=abs(Ea);
    
    hold on
    plot(Ea_mag,Ia_mag)
end
set(gca,'ydir','normal');  %%http://www.peteryu.ca/tutorials/matlab/plot_over_image_background
xlabel('I_{FD} [A]')
ylabel('I_{A} [A]')