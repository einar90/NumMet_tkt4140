clear all; close all; clc;

tspan = [0.0 15.0];     % Tidsrom
theta0 = pi/3; dtheta0 = 0;
y0 = [theta0; dtheta0]; % Initialverdier: [theta0; dtheta0]

dy = @(t,y) [y(2); -sin(y(1))]; % [dy_1; dy_2]

[T,Y] = ode45(dy, tspan, y0);   % Løser ODE med ode45

E = 0.5 * (Y(:,2).^2 - dtheta0^2) + cos(theta0) - cos(Y(:,1)); % Energifunksjon

Fig1 = figure('name','Amplitude');
plot(T,Y(:,1));
title('\theta(t)'); xlabel('t'); ylabel('\theta');

Fig2 = figure('name', 'E');
plot(T,E);
title('E(t)'); xlabel('t'); ylabel('E');
