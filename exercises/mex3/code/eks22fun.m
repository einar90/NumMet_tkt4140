function dy = eks22fun( x, y )
  dy = zeros(2,1);
  dy(1) = y(2);
  dy(2) = 3.0/2.0*y(1)^2;
end

