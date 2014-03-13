%--------------------------------------
% TKT4140 - Matlab øving 3
% Oppgave 2: Eks. fra avsnitt 2.2
%
% Based on the 'blasec' script
%--------------------------------------
clear all; close all; clc; format long;

x0 = 0;
x1 = 1;
xspan = [x0 x1];
beta = -1;

s0 = 2;
s1 = 3;

y0 = [s0 -8];
[x,y] = ode45(@eks22fun,xspan,y0);
fi0 = y(end,2) - beta;


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
  y0 = [s1 -8];
  [x,y] = ode45(@eks22fun,xspan,y0,options);
  fi1 = y(end,2) - beta;
  ds = -fi1*(s1 - s0)/(fi1 - fi0);
  s0 = s1;
  s1 = s1 + ds;
  fi0 = fi1;
  fprintf('%10d %12.6f %12.3e\n',it,s1,ds);
end


% First and last values for y and y'
fprintf('\n         x        y          y'' \n\n');
fprintf(' %12.2f %10.6f %10.6f\n',[x(1) y(1,:)]');
fprintf(' %12.2f %10.6f %10.6f\n',[x(end) y(end,:)]');

% Plotting f' and f" as a function of eta
plot(x,y(:,1),'--',x,y(:,2));
ylabel('y,y''')
xlabel('x')
title('Eksempel fra 2.2')
legend('y', 'y''')
grid on;
