n = 7;
p = 2;

A = zeros(p^n, p^n);

for i = 1:p^n
    for j = 1:p^n
        if mod(p*i-(j^2-j),p^n)==0
            A(i, j) = 1;
        else
            A(i, j) = 0;
        end
    end
end

format long
disp(A)
eigenvalues = eig(A)
disp(max(abs(eigenvalues)))
