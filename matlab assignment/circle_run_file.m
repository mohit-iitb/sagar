A = [0,0;0.5,0;1,0;1,1;0,1];%input
[m,n] = size(A);

%for i=-2:1:2
 %  A(i+3,1) = i;
  %  A(i+3,2) = sqrt(4-i^2); 
%end %To check base case for a circle

%function call
[x,r] = circle_fit(A);

%plotting function
hold on
th = 0:pi/50:2*pi;
xunit = r * cos(th) + x(1);
yunit = r * sin(th) + x(2);
h = plot(xunit, yunit);
for i=1:1:m
    plot(A(i,1),A(i,2),'-r*');
end
hold off