%震后交通韧性评估_带入清华园路网，日常+应急+恢复，0.2g0.3g0.4g,全自动输出结果

%输入部分：1.节点编号与节点人数、2.道路编号与起止节点、各条道路长度与通行能力参数、
%          5.重要建筑（包括应急避难场所，医院，主要办公单位）的所在位置、6.桥梁位置与易损性参数、7.道路易损性参数（残骸阻塞、道路破坏）
%输出部分：1.应急避难场所可达性，各节点到达应急避难场所的及时性。2.医院可达性，各节点到达医院的及时性。3.关键地点（医院）的可达性恢复情况。
%          4.重要地点（主要办公单位）可达性恢复情况。5.整体可达性恢复情况。
clear

%输入部分：(o表示original)
onode = xlsread('input.xlsx','node');    %节点编号、人数
ostreet = xlsread('input.xlsx','street');%道路编号，起始节点编号，终止节点编号，道路长度，阻塞概率0.2g,0.3g,0.4g
orefuge = xlsread('input.xlsx','refuge');%避难场所位置
ohospital = xlsread('input.xlsx','hospital');    %医院所在节点编号
ocritical = xlsread('input.xlsx','critical');    %主要办公单位节点编号
obridge = xlsread('input.xlsx','bridge');    %桥梁编号，0.2g破坏概率，0.3g，0.4g，影响道路（4列，0则为不影响）
tolerance = xlsread('input.xlsx','tolerance');   %可接受的距离增大倍数
xiufusudu = xlsread('input.xlsx','restoration'); %每日道路可清障多少米


%数据处理
tmp = size(onode,1);
linjie = zeros(tmp,tmp);    %表示节点连接关系的邻接矩阵，1表示直接相连
juli = linjie;

for i = 1 : size(ostreet,1)
    linjie(ostreet(i,2),ostreet(i,3)) = 1;
    juli(ostreet(i,2),ostreet(i,3)) = ostreet(i,4);
end
linjie = linjie + linjie';
juli = juli + juli';
binan = [juli,zeros(tmp,1);zeros(1,tmp),0];
for i = orefuge
    %binan(tmp + 1,i) = 0.1;
    binan(i,tmp + 1) = 0.1;
end
yiyuan = [juli,zeros(tmp,1);zeros(1,tmp),0];
for i = ohospital
    yiyuan(i,tmp + 1) = 0.1;
end
zhongyao = [juli,zeros(tmp,1);zeros(1,tmp),0];
for i = ocritical
    zhongyao(i,tmp + 1) = 0.1;
end

%参数设定：模拟次数，pga
nsr = 20;
%pga = 0.2;
%k = 10 * pga - 1;  %0.3g对应第二种破坏概率
%tolerance = 2;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%日常情况：
ndis0bn = zeros(1,size(onode,1));
ndis0yy = zeros(1,size(onode,1));
ndis0zy = zeros(1,size(onode,1));

for i = 1 : size(onode,1)
    ndis0bn(i) = ZDL(i,size(binan,1),binan);
    ndis0yy(i) = ZDL(i,size(yiyuan,1),yiyuan);
    ndis0zy(i) = ZDL(i,size(zhongyao,1),zhongyao);
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%应急阶段：
sresultbn = zeros(1,nsr);   %system result 避难
nresultbn = ones(size(onode,1),nsr);   %nodal result 避难
ndisbn = zeros(size(onode,1),nsr);   %nodal distance 避难
sresultyy = zeros(1,nsr);   %system result 医院
nresultyy = ones(size(onode,1),nsr);   %nodal result 医院
ndisyy = zeros(size(onode,1),nsr);   %nodal distance 医院
sresultzy = zeros(1,nsr);   %system result 重要
nresultzy = ones(size(onode,1),nsr);   %nodal result 重要
ndiszy = zeros(size(onode,1),nsr);   %nodal distance 重要

bstate = zeros(size(obridge,1),nsr);    %bridge state,1为工作，0为破坏
sstate = zeros(size(ostreet,1),nsr);    %street state,1为工作，0为破坏

bnshuchu = zeros(size(onode,1),3);
yyshuchu = zeros(size(onode,1),3);
zyshuchu = zeros(size(onode,1),3);
xtshuchu = zeros(3,3);                   %输出用,应急结果

yyshuchu2 = zeros(9,7);
zyshuchu2 = zeros(9,7);
ztshuchu2 = zeros(9,7); %zt为整体
xtshuchu2 = zeros(3,3);                  %输出用，修复结果


for k = 1 : 3

for n = 1 : nsr
    %初始化各记录变量
    brstate = zeros(size(obridge,1),1);
    ststate = zeros(size(ostreet,1),1);
    tmpbn = binan;
    tmpyy = yiyuan;
    tmpzy = zhongyao;
    resultbn = ones(size(onode,1),1);
    resultyy = ones(size(onode,1),1);
    resultzy = ones(size(onode,1),1);
    
    %生成桥梁破坏
    for i = 1 : size(obridge,1)
        brstate(i) = (rand > obridge(i,k + 1));  %1为工作，0为破坏
        tmp = 1;
        bstate(i,n) = brstate(i);
        %修改路网拓扑
        while(1 - brstate(i))
            tmpbn(ostreet(obridge(i,tmp + 4),2),ostreet(obridge(i,tmp + 4),3)) = 0;
            tmpbn(ostreet(obridge(i,tmp + 4),3),ostreet(obridge(i,tmp + 4),2)) = 0;
            tmpyy(ostreet(obridge(i,tmp + 4),2),ostreet(obridge(i,tmp + 4),3)) = 0;
            tmpyy(ostreet(obridge(i,tmp + 4),3),ostreet(obridge(i,tmp + 4),2)) = 0;
            tmpzy(ostreet(obridge(i,tmp + 4),2),ostreet(obridge(i,tmp + 4),3)) = 0;
            tmpzy(ostreet(obridge(i,tmp + 4),3),ostreet(obridge(i,tmp + 4),2)) = 0;
            tmp = tmp + 1; 
            if tmp > 4
                break
            end
            if obridge(i,tmp + 4) == 0
                break
            end
        end
    end
    
    %生成道路破坏
    for i = 1 : size(ostreet,1)
        ststate(i) = (rand > ostreet(i,k + 4)); %1为通畅，0为阻塞
        sstate(i,n) = ststate(i);
        if ~ststate(i)
            tmpbn(ostreet(i,2),ostreet(i,3)) = 0;  %lj(ostreet(i,2),ostreet(i,3)) * 2;
            tmpbn(ostreet(i,3),ostreet(i,2)) = 0;  %lj(ostreet(i,3),ostreet(i,2)) * 2;
            tmpyy(ostreet(i,2),ostreet(i,3)) = 0;  %lj(ostreet(i,2),ostreet(i,3)) * 2;
            tmpyy(ostreet(i,3),ostreet(i,2)) = 0;  %lj(ostreet(i,3),ostreet(i,2)) * 2;
            tmpzy(ostreet(i,2),ostreet(i,3)) = 0;
            tmpzy(ostreet(i,3),ostreet(i,2)) = 0;
        end
    end
    
    
    %应急避难场所可达性判断
    for i = 1 : size(onode,1)
        
        %若该点无人、有应急避难场所、有医院、有政府，则跳过判断
        if onode(i,2) == 0
            continue
        end
        if size(find(orefuge == i),1)
            continue
        end
        if size(find(ohospital == i),1)
            continue
        end
        if size(find(ocritical == i),1)
            continue
        end
        
        %其余情况，根据日常状态找最近的避难所，以及最短路径，若被堵塞则认为无法到达
        dis1 = ndis0bn(i);
        dis2 = ZDL(i,size(tmpbn,1),tmpbn);
        ndisbn(i,n) = dis2;
        if dis2 > tolerance * ndis0bn(i)
            resultbn(i) = 0;
        end
        nresultbn(i,n) = resultbn(i);
    end
    
	sresultbn(n) = resultbn' * onode(:,2) / sum(onode(:,2));
    
    %医院可达性
    for i = 1 : size(onode,1)
        
        %若该点有医院,则跳过判断
        if size(find(ohospital == i),1)
            ndisyy(i,n) = 0;
            nresultyy(i,n) = 1;
            continue
        end

        
        %其余情况，根据日常状态找最近的医院，以及最短路径，若被堵塞则认为无法到达
        dis1 = ndis0yy(i);
        dis2 = ZDL(i,size(tmpyy,1),tmpyy);
        ndisyy(i,n) = dis2;
        if dis2 > tolerance * dis1
            resultyy(i) = 0;
        end
        nresultyy(i,n) = resultyy(i);
    end
    
    sresultyy(n) = resultyy' * onode(:,2) / sum(onode(:,2));
    
    %重要场所可达性
    for i = 1 : size(onode,1)
        
        %若该点为重要场所,则跳过判断
        if size(find(ocritical == i),1)
            ndiszy(i,n) = 0;
            nresultzy(i,n) = 1;
            continue
        end

        
        %其余情况，根据日常状态找最近的避难所，以及最短路径，若被堵塞则认为无法到达
        dis1 = ndis0zy(i);
        dis2 = ZDL(i,size(tmpzy,1),tmpzy);
        ndisyy(i,n) = dis2;
        if dis2 > tolerance * dis1
            resultzy(i) = 0;
        end
        nresultzy(i,n) = resultzy(i);
    end
    
	sresultzy(n) = resultzy' * onode(:,2) / sum(onode(:,2));

    
end

bnshuchu(:,k) = mean(nresultbn')';
yyshuchu(:,k) = mean(nresultyy')';
zyshuchu(:,k) = mean(nresultzy')';
xtshuchu(k,:) = [sum(sresultbn) / nsr, sum(sresultyy) / nsr, sum(sresultzy) / nsr];


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%修复阶段

%变量预定义
xiufust = zeros(1,size(ostreet,1)); %各条道路修复带来的系统收益，以通往重要地点的可达性作为指标
yyxiufu = zeros(nsr,7);
zyxiufu = zeros(nsr,7);
ztxiufu = zeros(nsr,7); %医院、重要场所和整体交通的恢复情况，每行表示一次模拟，每列表示几天之后

%先根据应急模拟结果，计算每条道路的修复收益
for i = 1 : size(ostreet,1)
    tmp1 = find(sstate(i,:) == 0);
    tmp2 = find(sstate(i,:) == 1);
    
    if size(tmp1,2) * size(tmp2,2) == 0;
        xiufust(i) = 0;
    else
        xiufust(i) = abs(mean(sresultzy(tmp2)) - mean(sresultzy(tmp1)));
    end
    
    %xiufust(i) = rand;
    
end

for n = 1 : nsr
    
    xiufugc = ones(4,size(ostreet,1)); %修复过程，第一行为修复道路长度，第二~四行分别为医院，重要场所，全部道路修复情况
    xiufugc(1,:) = 10000000;
    
    %第n次模拟的结果中，对道路修复排序
    stweixiu = 1 - sstate(:,n);
    weixiucx = stweixiu .* xiufust';
    tmp = sort(unique(weixiucx),'descend');
    tmpnum = size(weixiucx(weixiucx ~= 0),1);
    tmpst = [];
    for i = 1 : tmpnum
        if tmp(i) == 0
            break
        end
        tmpst = [tmpst find(weixiucx == tmp(i))'];
    end
    
    %根据破坏情况修改道路拓扑
    tmpyy = yiyuan;
    tmpzy = zhongyao;    
    tmp1 = find(sstate(:,n) == 0);
    for i = tmp1
        tmpyy(ostreet(i,2),ostreet(i,3)) = 0;  
        tmpyy(ostreet(i,3),ostreet(i,2)) = 0;  
        tmpzy(ostreet(i,2),ostreet(i,3)) = 0;
        tmpzy(ostreet(i,3),ostreet(i,2)) = 0;
    end
    tmp2 = find(bstate(:,n) == 0);
    for i = tmp2
        tmp = 1;
        while(1)
            tmpyy(ostreet(obridge(i,tmp + 4),2),ostreet(obridge(i,tmp + 4),3)) = 0;
            tmpyy(ostreet(obridge(i,tmp + 4),3),ostreet(obridge(i,tmp + 4),2)) = 0;
            tmpzy(ostreet(obridge(i,tmp + 4),2),ostreet(obridge(i,tmp + 4),3)) = 0;
            tmpzy(ostreet(obridge(i,tmp + 4),3),ostreet(obridge(i,tmp + 4),2)) = 0;
            tmp = tmp + 1;
            if tmp > 4
                break
            end
            if obridge(i,tmp + 4) == 0
                break
            end
        end
    end    
    
    %初始化修复过程
    xiufugc(1,1) = 0;
    xiufugc(2,1) = sresultyy(n);
    xiufugc(3,1) = sresultzy(n);
    xiufugc(4,1) = 1 - sum(ostreet(tmpst,4)) / sum(ostreet(:,4));
    
    %以道路为单位修复
    for i = 1 : tmpnum
        xiufugc(1,i + 1) = xiufugc(1,i) + ostreet(tmpst(i),4);
        
        %修改道路拓扑
        tmpyy(ostreet(tmpst(i),2),ostreet(tmpst(i),3)) = ostreet(tmpst(i),4);  
        tmpyy(ostreet(tmpst(i),3),ostreet(tmpst(i),2)) = ostreet(tmpst(i),4);  
        tmpzy(ostreet(tmpst(i),2),ostreet(tmpst(i),3)) = ostreet(tmpst(i),4);
        tmpzy(ostreet(tmpst(i),3),ostreet(tmpst(i),2)) = ostreet(tmpst(i),4);
        
        %计算修复后的系统指标
        %医院
        rtmp = ones(1,size(onode,1));
        for j = 1 : size(onode,1)
        
        %若该点有医院,则跳过判断
            if size(find(ohospital == j),1)
                rtmp(j) = 1;
                continue
            end
        
        %其余情况，找最近的医院
            dis1 = ndis0yy(j);
            dis2 = ZDL(j,size(tmpyy,1),tmpyy);
            if dis2 > tolerance * dis1
                rtmp(j) = 0;
            end
        end
        xiufugc(2,i + 1) = rtmp * onode(:,2) / sum(onode(:,2));
        xiufugc(2,i + 1) = max(xiufugc(2,i),xiufugc(2,i + 1));
        %重要
        rtmp = ones(1,size(onode,1));
        for j = 1 : size(onode,1)
        
        %若该点是重要场所,则跳过判断
            if size(find(ocritical == j),1)
                rtmp(j) = 1;
                continue
            end
        
        %其余情况，找最近的重要场所
            dis1 = ndis0zy(j);
            dis2 = ZDL(j,size(tmpzy,1),tmpzy);
            if dis2 > tolerance * dis1
                rtmp(j) = 0;
            end
        end
        xiufugc(3,i + 1) = rtmp * onode(:,2) / sum(onode(:,2));
        
        xiufugc(4,i + 1) = xiufugc(4,i) + ostreet(tmpst(i),4) / sum(ostreet(:,4));

    end
    
    %根据修复速度，转化为根据时间修复，并调整格式便于输出
    for i = 1 : 7
        tmp = i * xiufusudu;
        tmp = max(find(xiufugc(1,:) <= tmp)) ; 
        yyxiufu(n,i) = xiufugc(2,tmp);
        zyxiufu(n,i) = xiufugc(3,tmp);
        ztxiufu(n,i) = xiufugc(4,tmp);
        
    end

end

%数据输出
for i = 1 : 7
    tmp = yyxiufu(:,i);
    tmp = sort(tmp);
    yyshuchu2(3 * k - 2,i) = mean(tmp);
    yyshuchu2(3 * k - 1,i) = tmp(round(0.05*nsr));
    yyshuchu2(3 * k,i) = length(find(tmp > 0.9)) / nsr;
    tmp = zyxiufu(:,i);
    tmp = sort(tmp);
    zyshuchu2(3 * k - 2,i) = mean(tmp);
    zyshuchu2(3 * k - 1,i) = tmp(round(0.05*nsr));
    zyshuchu2(3 * k,i) = length(find(tmp > 0.9)) / nsr;
    tmp = ztxiufu(:,i);
    tmp = sort(tmp);
    ztshuchu2(3 * k - 2,i) = mean(tmp);
    ztshuchu2(3 * k - 1,i) = tmp(round(0.05*nsr));
    ztshuchu2(3 * k,i) = length(find(tmp > 0.9)) / nsr;
end



end

xlswrite('output.xlsx',bnshuchu,'refuge');
xlswrite('output.xlsx',yyshuchu,'hospital');
xlswrite('output.xlsx',zyshuchu,'critical');
xlswrite('output.xlsx',xtshuchu,'system_dur');

xlswrite('output.xlsx',yyshuchu2,'r_hospital');
xlswrite('output.xlsx',zyshuchu2,'r_critical');
xlswrite('output.xlsx',ztshuchu2,'r_all');