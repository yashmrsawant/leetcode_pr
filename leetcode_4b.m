clear; clc;

%%
% Generate random integers for N and M
S = [10 : 10 : 50000];

T = [];
MN = [];
for s = S
N = ceil(s/2);
M = ceil(s/2);

MN = [MN; M+N];

% Generate and sort array A
A = randi(99, N, 1);
A = sort(A)';

% Generate and sort array B
B = randi(99, M, 1);
B = sort(B)';


E = [];
for it = 1 : 100

% % Display information about arrays
% fprintf('Len(A) = %d, Med(A) = %d, A: \n', N, A(ceil(N/2)));
% disp(A);
% 
% fprintf('Len(B) = %d, Med(B) = %d, B: \n', M, B(ceil(M/2)));
% disp(B);
%
% Initialize pointers

% 
% % Handle cases where length of array is <= 2
% if N <= 2 || M <= 2
%     % Combine arrays and sort
%     C = [A; B];
%     C = sort(C);
% 
%     % Display combined and sorted array
%     fprintf('Combined and sorted: \n');
%     disp(C);
% end
i1 = 0;
j1 = N - 1;
i2 = 0;
j2 = M - 1;

% Calculate effective array lengths
k1 = j1 - i1 + 1;
k2 = j2 - i2 + 1;

ed = 0;
while k1 > 2 && k2 > 2
    % Find medians
    ed = ed + 1;
    medA = A(i1 + floor((j1 - i1) / 2));
    medB = B(i2 + floor((j2 - i2) / 2));

    % Swap arrays if necessary
    if medA > medB
        [A, B] = swap(A, B);
        [i1, i2] = swap(i1, i2);
        [j1, j2] = swap(j1, j2);
        [k1, k2] = swap(k1, k2);
    end

    % Remove parts of arrays based on lengths
    if k1 <= k2
        k = floor((j1 - i1) / 2);
        i1 = i1 + k;
        j2 = j2 - k;
    else
        k = floor((j2 - i2) / 2);
        i1 = i1 + k;
        j2 = j2 - k;
    end

    % Recalculate effective array lengths
    k1 = j1 - i1 + 1;
    k2 = j2 - i2 + 1;
end
E = [E; ed];
end


T = [T; mean(E)];
end

%%


figure(1); clf; 
subplot(1, 2, 1); hold on;

a = gamrnd(1, 2,500, 1) - 2;
b = randn(500, 1) + 2;
histogram(a, 'Normalization', 'pdf', 'FaceColor', 'r');
medA = median(a);
line([medA, medA], [0, 1000], 'LineWidth', 2, 'LineStyle', '--', 'Color', 'r');

histogram(b, 'Normalization', 'pdf', 'FaceColor', 'b');
medB = median(b);
line([medB, medB], [0, 1000], 'LineWidth', 2, 'LineStyle', '--', 'Color', 'b');


ylim([0, 0.5]);

subplot(1, 2, 2); hold on;

a = gamrnd(1, 2,500, 1) + 2;
b = randn(500, 1);

histogram(a, 'Normalization', 'pdf', 'FaceColor', 'r');
medA = median(a);
line([medA, medA], [0, 1000], 'LineWidth', 2, 'LineStyle', '--', 'Color', 'r');

histogram(b, 'Normalization', 'pdf', 'FaceColor', 'b');
medB = median(b);
line([medB, medB], [0, 1000], 'LineWidth', 2, 'LineStyle', '--', 'Color', 'b');


ylim([0, 0.5]);