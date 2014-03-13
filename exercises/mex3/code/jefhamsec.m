%--------------------------------------
% TKT4140 - Matlab øving 3
% Oppgave 1: Jeffrey-Hamel strømning
%
% Based on the 'blasec' script
%--------------------------------------
clear all; close all; clc;

global Re alpha
Re = 30;
alpha = 18 * pi / 180;

% Setting eta range
eta0 = 0; %start
eta1 = 1; %etainf
etaspan = [eta0 eta1];

% Initial s guesses.
% The approximate value was found by running the program multiple times.
s0 = -7;
s1 = -6;

% Compute phi0
y0 = [1.0 0.0  s0];
[eta,y] = ode45(@jefham,etaspan,y0);
fi0 = y(end,1);

% Initial values for the iteration
itmax = 50;
it = 0;
epsi = 1.0e-5;
ds = 1;
options = odeset('RelTol',1.0e-5);

% Headline of the table
fprintf('        itr.      s          ds\n\n');

% Start iteration
while(abs(ds) > epsi) & (it < itmax)
  it = it + 1;
  y0(3) = s1;
  [eta,y] = ode45(@jefham,etaspan,y0,options);
  fi1 = y(end,1);
  ds = -fi1*(s1 - s0)/(fi1 - fi0);
  s0 = s1;
  s1 = s1 + ds;
  fi0 = fi1;
  fprintf('%10d %12.6f %12.3e\n',it,s1,ds);
end

% First and last values (eta=0, 1) for f, f' and f''
fprintf('\n         eta        f          f''        f"\n\n');
fprintf(' %12.2f %10.6f %10.6f % 13.5e\n',[eta(1) y(1,:)]');
fprintf(' %12.2f %10.6f %10.6f % 13.5e\n',[eta(end) y(end,:)]');


% Plotting f' and f" as a function of eta
plot(y(:,1),eta,'--',y(:,2),eta, y(:,3),eta,'-.');
ylabel('\eta','Rotation',0)
xlabel('f, f'' , f"')
title('Solution of the Jeffrey-Hamel equation')
legend('f', 'f''','f"')
legend('location','best')
grid on;
