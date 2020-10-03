format long
S=101.8e6*exp(acos(0.85)*1j)
V=13800

I=conj(S/(sqrt(3)*V))
abs(I)
C=234.5
Ra15=0.0015*((15+C)/(20+C))

Rf15=0.065*((15+C)/(20+C))

%% Potencia de salida

Pout=86.53 %MW

%% Perdidas en el cobre

Pcu=3*Ra15*abs(I)^2
Pcu=Pcu/1e6 %MW
% Pcu=0.799

%% Potencia constante

Pst=0.726+0.231+0.103 %MW
%% Pexcitacion
Psis=0.012 %MW
VfIf=120^2/(Rf15*1e6)
Pexcitacion=Psis+VfIf

%% Eficiencia
n=Pout/(Pcu+Pst+Pexcitacion+Pout)*100

%% Pdesarrollada
Pd=Pout+Pcu-Pst-Pexcitacion
Pd=Pout-Pst-Pexcitacion
%%
% (120^2/Rf15)/1e3
Xd=1.98*1.869


83.45

Perdidas=12.29e3+726.7e3+231.15e3+103.997e3
Pentrada=86.53e6


% Pd=86.609kW con resistencia de armadura
% 98.43% Eficiencia
% Taplicado 232.55K N-m
% Delta 39.38

% %% Test
% clear all
% Vg=26
% Rb=0.190972222222222
% RL=4e-3
% Rf=125/3
% v=-125
% 
% % D=0.994377060353364
% syms D
% Dp=1-D
% 
% IL=-v/(Rf*Dp)
% 
% F=Vg*D-Rb*IL*D-RL*IL+v*Dp
% solve(F==0,D)



