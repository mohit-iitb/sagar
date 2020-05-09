randn('seed',314);
x=linspace(0,1,30);
y=2*x.^2-3*x+1+0.05*randn(size(x));

p = polyfit(x,y,2);

y1 = polyval(p,x);

plot(x,y,'o','LineWidth',2);
hold on;
plot(x,y1,'LineWidth',2,'MarkerEdgeColor','k','MarkerFaceColor','g','MarkerSize',10);
legend({'noisy points','The Best Quadratic-curve fit'});
xlabel('X values','FontSize',16);
ylabel('Y values','FontSize',16);
hold off
