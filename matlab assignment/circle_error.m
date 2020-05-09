function [x,r] = circle_fit(A)
[m,n] = size(A);
b = [];
a = [2*A,ones(size(A),1)*-1];
for i=1:1:m
    b = [b sqrt(A(i,1)^2+A(i,2)^2)];
end
%b = [0;0.5;1;sqrt(2);1];
c = a\b;

x = [c(1),c(2)];
d = sqrt(c(1)^2+c(2)^2);
r = sqrt(d-c(3));

%circle(c(1),c(2),r,a)

