function [x,r] = circle_fit(A)

[m,n] = size(A);
b = [];
a = [2*A,ones(m,1)*-1];
for i=1:1:m
    b = [b (A(i,1)^2+A(i,2)^2)];
end
c = a\transpose(b);
x = [c(1),c(2)];
r = sqrt((c(1)^2+c(2)^2)-c(3));


