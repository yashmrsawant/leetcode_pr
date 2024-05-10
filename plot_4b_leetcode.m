clear; clc;


load('./4b_leetcode.mat');

MS = double(MS);


M_un = unique(MS(:));

T_un = zeros(size(M_un));
for m_i = 1 : length(M_un)
    i = MS == M_un(m_i);
    T_i = T(i);
    T_un(m_i) = mean(T_i);
end
%%

xx = M_un;
yy = T_un;
scatter(xx, yy, 10, 'filled');

xlabel("Size of the array");
ylabel("Time taken");