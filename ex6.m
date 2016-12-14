
%% Initialization
%clear ; close all; clc
function Predict= ex6(file,Test, prediction)

fprintf('Loading and Visualizing Data ...\n')

% Load from ex6data2: 
% You will have X, y in your environment
data = load(file);
X = data(:, [1, 3]); y = data(:, 2);

data2 = load(Test);
test = data2(:, [1, 3]); y = data2(:, 2);

% Plot training data
plotData(X, y);



%  SVM classifier.
% 
fprintf('\nTraining SVM with RBF Kernel (this may take 1 to 2 minutes) ...\n');


% SVM Parameters
C = 1; sigma = 0.1;

% We set the tolerance and max_passes lower here so that the code will run
% faster. However, in practice, you will want to run the training to
% convergence.
model= svmTrain(X, y, C, @(x1, x2) gaussianKernel(x1, x2, sigma)); 
visualizeBoundary(X, y, model);

p = svmPredict(model, test);
fprintf('Training Accuracy: %f\n', mean(double(p == y)) * 100);
p2 = svmPredict(model, prediction);
Predict = p2
fprintf('prediction: %f\n', p2)
end

