% 2016 octobre
% Algo de suivi de trajectoire NLGL
% Olivier Gougeon (rapport de projet)
% Polytechnique Montréal

function dpsi_c = NLGL(Wi,Wii,p,psi,v_a,L)

% Local definition of (x,y) for easier reading of the code
x = 1;
y = 2;

% Step 1: Initialization (Function inputs)

%--- Step 2: Determine intersection point s

% Get equation of waypoint line: ax+by=c
if Wii(x) ~= Wi(x)
	alpha = (Wii(y)-Wi(y))/(Wii(x)-Wi(x));
	beta = Wii(y)-alpha*Wii(x);
	a = alpha; b = -1; c = -beta;
else
	% Vertical line
	a = 1;
	b = 0;
	c = Wi(x);
end

% Apply algorithm ...
	(http://www.mathematik.tu-darmstadt.de/~ehartmann/cdgen0104.pdf, p. 17)
x_m = p(x); y_m = p(y);
cp = c-a*x_m-b*y_m;


% Calculate solution
r = L;
xi = nan(1,2);
eta = nan(1,2);
if r^2*(a^2+b^2)-cp^2 > 0
	% Two points from the line intersect with the circle
	xi(1) = ( a*cp + b*sqrt(r^2*(a^2+b^2)-cp^2) ) /(a^2+b^2);
	xi(2) = ( a*cp - b*sqrt(r^2*(a^2+b^2)-cp^2) ) /(a^2+b^2);
	eta(1) = ( b*cp - a*sqrt(r^2*(a^2+b^2)-cp^2) ) /(a^2+b^2);
	eta(2) = ( b*cp + a*sqrt(r^2*(a^2+b^2)-cp^2) ) /(a^2+b^2);
elseif r^2*(a^2+b^2)-cp^2 == 0
	% One point from the line intersects with the circle (tangent)
	xi(1) = a*cp;
	eta(1) = b*cp;
else
	error('A4-NLGL: No intersection exists between the generated waypoint path ...
	and the virtual circle.')
end

% Apply inverted change of variables
x_12 = x_m + xi;
y_12 = y_m + eta;

% Rename points
s1 = [x_12(1);y_12(1)];
s2 = [x_12(2);y_12(2)];

% Determine the wanted point s (closest intersection point to Wii)
if all(isnan(s2))
	x_t = s1(x);
	y_t = s1(y);
elseif norm(Wii-s1) < norm(Wii-s2)
	x_t = s1(x);
	y_t = s1(y);
else
	x_t = s2(x);
	y_t = s2(y);
end
s = [x_t;y_t];

% Step 3
alpha = atan2(s(y)-p(y),s(x)-p(x));

% Step 4
eta = alpha-psi;

% Step 5
u_lat = 2*v_a^2*sin(eta)/L;

% Step 6
dpsi_c = u_lat/v_a;

end