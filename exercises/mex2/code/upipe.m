function dy = upipe( t,y )
D = 0.5; f = 0.05; L = 392; g = 9.8;
dy = zeros(2,1);
dy(1) = y(2);
dy(2) = -(2*g/L*y(1) + f/2/D*y(2)*abs(y(2)));
end

