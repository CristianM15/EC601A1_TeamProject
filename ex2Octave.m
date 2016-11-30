
%% Initialization

clear ; close all; clc

%% Load Data
%  The first two columns contains the exam scores and the third column
%  contains the label.

data = load('ex2data1.txt');
X = data(:, [1, 2]); y = data(:, 3);

%% ==================== Part 1: Plotting ====================

plotDataOctave(X, y);

% Put some labels 
% Labels and Legend
xlabel('parameter_1')
ylabel('parameter_2')

% Specified in plot order
legend('Had fire', 'Not had fire')



%% ============ Part 2: Compute Cost and Gradient ============

%  Setup the data matrix appropriately, and add ones for the intercept term
[m, n] = size(X);

% Add intercept term to x and X_test
X = [ones(m, 1) X];

% Initialize fitting parameters
initial_theta = zeros(n + 1, 1);
% Compute and display initial cost and gradient
[cost, grad] = costFunctionOctave(initial_theta, X, y);



%% ============= Part 3: Optimizing using fminunc  =============
%  In this exercise, you will use a built-in function (fminunc) to find the
%  optimal parameters theta.

%  Set options for fminunc
options = optimset('GradObj', 'on', 'MaxIter', 400);

%  Run fminunc to obtain the optimal theta
%  This function will return theta and the cost 
[theta, cost] = ...
    fminunc(@(t)(costFunctionOctave(t, X, y)), initial_theta, options);
% Plot Boundary
plotDecisionBoundaryOctave(theta, X, y);

% Put some labels 
hold on;
% Labels and Legend
xlabel('parameter_1')


ylabel('parameter_2')

% Specified in plot order
legend('Had fire', 'Not had fire')
hold off;


%% ============== Part 4: Predict and Accuracies ==============


prob = sigmoidOctave([1 45 85] * theta);
fprintf([' ' ...
         'probability of %f\n\n'], prob);

% Compute accuracy on our training set
p = predict(theta, X);



