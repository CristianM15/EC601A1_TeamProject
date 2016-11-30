function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));
hx=sigmoid(X*theta);
J=-(y'*log(hx)+(1-y)'*log(1-hx))/m+lambda/(2*m)*theta(2:size(theta),:)'*theta(2:size(theta),:);
theta(1)=0;
grad=X'*(hx-y)/m+lambda/m*theta;


% =============================================================

end
