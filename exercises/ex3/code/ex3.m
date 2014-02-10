s = -64/113;
xs = [0, 0.25, 0.50, 0.75, 1.0];

un = [1; 1+s/4; 1+s/2; 1+23*s/32; 1+113*s/128]'
gn = [s; s; 7*s/8; 21*s/32; 105*s/256]'

uef = inline('1 - erf(x)/(2*erf(1))');
gef = inline('-exp(-x.^2)/(erf(1)*sqrt(pi))');

ue = feval(uef, xs)
ge = feval(gef, xs)


disp('==============================')
clear all; clc;

s = 7/39;
ys = [0; 1/3; 2/3; 1]'

un = [0; s/3;   2*s/3-4/9; 13*s-4/3]'
%gn = [s; s-4/3; 37*s-8/3;  109*s-52]'

A = (1+1/81*(cosh(18)-1))/(sinh(18));
B = -1/81;
uef = inline('(1+1/81*(cosh(18)-1))/(sinh(18))*sinh(18*y) + (-1/81)*cosh(18*y) + 1/81');

ue = feval(uef, ys)
