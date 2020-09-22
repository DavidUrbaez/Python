format long

Ra27=(0.00385*2+0.00386)/3
C=243
Ra75=Ra27*(75+C)/(27+C)

%% Istator

Vab=13.8 %kv
S=101800*exp(acos(0.9)*1j)

Ia=conj((S/3)*(sqrt(3)/Vab))
Ia_magnitud=abs(Ia)

3*Ia_magnitud^2*Ra75/1e3 %kW


