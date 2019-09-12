function dis = ZDL(qd,zd,juli)

n = size(juli,1);
b = zeros(1,n);
%c = zeros(n);
b(qd) = 1;
l(n) = 0;
lt = ones(1,n) * 100000000000;

while(1)
    for i = 1 : n
        if b(i) == 1
            for j = 1 : n
                if b(j) == 0 && juli(i,j) ~= 0
                    lt(j) = min(l(i) + juli(i,j), lt(j));
                end
            end
        end
    end
    
    i = find(lt == min(lt));
    b(i) = 1;
    l(i) = lt(i);
    lt = ones(1,n) * 100000000000;
    if b(zd) == 1
        break
    end
    if prod(b) ~= 0
        break
    end
end

dis = l(zd);

