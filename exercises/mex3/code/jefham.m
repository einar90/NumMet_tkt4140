function df = jefham(eta, f)
  global alpha  Re
  df = zeros(3,1);
  df(1) = f(2);
  df(2) = f(3);
  df(3) = -2 * alpha * f(2) * (Re * f(1) + 2*alpha);
end

