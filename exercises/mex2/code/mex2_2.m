clear all; close all; clc;

tspan = [0.0 15.0];
y0 = [-6; 0];

[T,Y] = ode45(@upipe, tspan, y0);

figure('name','Forskyvning og hastighet');
plot(T,Y(:,1),'r', T, Y(:,2),'b');
xlabel('t'); ylabel('m  |  m/s');
legend('location','southeast','Forskyvning','Hastighet');