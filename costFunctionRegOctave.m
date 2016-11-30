function [J, grad] = costFunctionRegOctave(theta, X, y, lambda)  
  
% Initialize some useful values  
m = length(y); % number of training examples  
  
% You need to return the following variables correctly   
J = 0;  
grad = zeros(size(theta));  
  
Jtmp=0;  
h= zeros(m,1);  
  
%step1:compute hx  
hx = X*theta;  
  
%step2:compute h(hx)  
h = sigmoidOctave(hx);  
  
%step3:compute cost function's sum part  
for i=1:m,  
    Jtmp=Jtmp+(-y(i)*log(h(i))-(1-y(i))*log(1-h(i)));  
end;  
J=(1/m)*Jtmp + (lambda/(2*m))*sum(theta(2:size(X,2)).^2);  
  
%step4:compute gradient's sum part      
sum1 =zeros(size(X,2),1);%#features row  
for i=1:m  
    sum1 = sum1+(h(i)-y(i)).*X(i,:)';  
end;  
grad(1)= (1/m)*sum1(1);  
grad(2:size(X,2))= (1/m)*sum1(2:size(X,2)) + (lambda/m).*theta(2:size(X,2)); 