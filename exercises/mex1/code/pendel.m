% TKT4140 Matlabøving 1
clear all; close all; clc;

%% Variable som er felles for oppgave 1 og 2
% Kjøreparametere
tmax = 15;                  % Maks tid
dt = 0.1;                   % Tidsinkrement
n = round(tmax/dt);         % Antall tidsskritt

% Initialverdier
theta0 = pi/2;              % Startvinkel/-posisjon
dtheta0 = 0.0;              % Starthastighet


%% Oppgave 1: Bruk av Eulers metode

% Allokerer vektorer
t = linspace(0,tmax,n)';      % Tidsvektor
theta_e = zeros(n,1);         % Posisjonsvektor
dtheta_e = zeros(n,1);        % Hastighetsvektor
ddtheta_e = zeros(n,1);       % Akselerasjonsvektor
E_e = zeros(n,1);             % Energifunksjon

% Setter inn startverdier
theta_e(1) = theta0;
dtheta_e(1) = dtheta0;
ddtheta_e(1) = -sin(theta0);

% Beregner vektorer for posisjon og hastighet vha. Eulers metode
for i = 2:n
  theta_e(i) = theta_e(i-1) + dt * dtheta_e(i-1);
  dtheta_e(i) = dtheta_e(i-1) + dt * ddtheta_e(i-1);
  ddtheta_e(i) = - sin(theta_e(i));
end

% Beregner energivektoren
for i = 1:n
  E_e(i) = 0.5 * (dtheta_e(i)^2 - dtheta_e(1)^2) + cos(theta_e(1)) - cos(theta_e(i));
end


%% Oppgave 2: Bruk av Heuns metode

% Allokerer nye vektorer
theta_h = zeros(n,1);         % Posisjonsvektor
thetap_h = zeros(n,1);        % Posisjonsvektor, predikat
dtheta_h = zeros(n,1);        % Hastighetsvektor
dthetap_h = zeros(n,1);       % Hastighetsvektor, predikat
ddtheta_h = zeros(n,1);       % Akselerasjonsvektor
ddthetap_h = zeros(n,1);      % Akselerasjonsvektor, predikat
E_h = zeros(n,1);             % Energifunksjon

% Setter inn startverdier
theta_h(1) = theta0;
dtheta_h(1) = dtheta0;
ddtheta_h(1) = -sin(theta0);

% Beregner vektorer for posisjon og hastighet vha. Eulers metode
for i = 2:n
  thetap_h(i) = theta_h(i-1) + dt * dtheta_h(i-1);                     % Pos. (p)
  dthetap_h(i) = dtheta_h(i-1) + dt * ddtheta_h(i-1);                  % Has. (p)
  ddthetap_h(i) = -sin(thetap_h(i));                                   % Aks. (p)
  theta_h(i) = theta_h(i-1) + dt/2 * (dtheta_h(i-1)+dthetap_h(i));     % Pos.
  dtheta_h(i) = dtheta_h(i-1) + dt/2 * (ddtheta_h(i-1)+ddthetap_h(i)); % Has.
  ddtheta_h(i) = -sin(theta_h(i));                                     % Aks.
end

% Beregner energivektoren
for i = 1:n
  E_h(i) = 0.5 * (dtheta_h(i)^2 - dtheta_h(1)^2) + cos(theta_h(1)) - cos(theta_h(i));
end


% Lager kombinasjonsplott
comb_A = figure('name', 'Amplitude (Euler+Heun)');
hold on;
plot(t, theta_e, 'color', 'r');
plot(t, theta_h, 'color', 'b');
title(strcat('\Delta t = ', num2str(dt))); xlabel('t'); ylabel('\theta');
legend('Euler', 'Heun');
print(comb_A, '-depsc2', 'comb_A.eps');

% Lager kombinasjonsplott
comb_E = figure('name', 'Energi (Euler+Heun)');
hold on;
plot(t, E_e, 'color', 'r');
plot(t, E_h, 'color', 'b');
title(strcat('\Delta t = ', num2str(dt))); xlabel('t'); ylabel('\theta');
legend('Euler', 'Heun');
print(comb_E, '-depsc2', '-zbuffer', '-r200', 'comb_E.eps');


%% Analytical solution
eqn = 'D2y+sin(x)=0';
inits = strcat(strcat('y(0)=',num2str(theta0)), strcat(',Dy(0)=',num2str(dtheta0)));
y = dsolve(eqn,inits,'x');
x = t;
theta_a = eval(vectorize(y));

% Plotting 'analytical'
figure('name', 'analytical');plot(t,theta_a);
