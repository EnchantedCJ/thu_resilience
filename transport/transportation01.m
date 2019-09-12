%���ͨ��������_�����廪԰·�����ճ�+Ӧ��+�ָ���0.2g0.3g0.4g,ȫ�Զ�������

%���벿�֣�1.�ڵ�����ڵ�������2.��·�������ֹ�ڵ㡢������·������ͨ������������
%          5.��Ҫ����������Ӧ�����ѳ�����ҽԺ����Ҫ�칫��λ��������λ�á�6.����λ���������Բ�����7.��·�����Բ������к���������·�ƻ���
%������֣�1.Ӧ�����ѳ����ɴ��ԣ����ڵ㵽��Ӧ�����ѳ����ļ�ʱ�ԡ�2.ҽԺ�ɴ��ԣ����ڵ㵽��ҽԺ�ļ�ʱ�ԡ�3.�ؼ��ص㣨ҽԺ���Ŀɴ��Իָ������
%          4.��Ҫ�ص㣨��Ҫ�칫��λ���ɴ��Իָ������5.����ɴ��Իָ������
clear

%���벿�֣�(o��ʾoriginal)
onode = xlsread('input.xlsx','node');    %�ڵ��š�����
ostreet = xlsread('input.xlsx','street');%��·��ţ���ʼ�ڵ��ţ���ֹ�ڵ��ţ���·���ȣ���������0.2g,0.3g,0.4g
orefuge = xlsread('input.xlsx','refuge');%���ѳ���λ��
ohospital = xlsread('input.xlsx','hospital');    %ҽԺ���ڽڵ���
ocritical = xlsread('input.xlsx','critical');    %��Ҫ�칫��λ�ڵ���
obridge = xlsread('input.xlsx','bridge');    %������ţ�0.2g�ƻ����ʣ�0.3g��0.4g��Ӱ���·��4�У�0��Ϊ��Ӱ�죩
tolerance = xlsread('input.xlsx','tolerance');   %�ɽ��ܵľ���������
xiufusudu = xlsread('input.xlsx','restoration'); %ÿ�յ�·�����϶�����


%���ݴ���
tmp = size(onode,1);
linjie = zeros(tmp,tmp);    %��ʾ�ڵ����ӹ�ϵ���ڽӾ���1��ʾֱ������
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

%�����趨��ģ�������pga
nsr = 500;
%pga = 0.2;
%k = 10 * pga - 1;  %0.3g��Ӧ�ڶ����ƻ�����
%tolerance = 2;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%�ճ������
ndis0bn = zeros(1,size(onode,1));
ndis0yy = zeros(1,size(onode,1));
ndis0zy = zeros(1,size(onode,1));

for i = 1 : size(onode,1)
    ndis0bn(i) = ZDL(i,size(binan,1),binan);
    ndis0yy(i) = ZDL(i,size(yiyuan,1),yiyuan);
    ndis0zy(i) = ZDL(i,size(zhongyao,1),zhongyao);
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Ӧ���׶Σ�
sresultbn = zeros(1,nsr);   %system result ����
nresultbn = ones(size(onode,1),nsr);   %nodal result ����
ndisbn = zeros(size(onode,1),nsr);   %nodal distance ����
sresultyy = zeros(1,nsr);   %system result ҽԺ
nresultyy = ones(size(onode,1),nsr);   %nodal result ҽԺ
ndisyy = zeros(size(onode,1),nsr);   %nodal distance ҽԺ
sresultzy = zeros(1,nsr);   %system result ��Ҫ
nresultzy = ones(size(onode,1),nsr);   %nodal result ��Ҫ
ndiszy = zeros(size(onode,1),nsr);   %nodal distance ��Ҫ

bstate = zeros(size(obridge,1),nsr);    %bridge state,1Ϊ������0Ϊ�ƻ�
sstate = zeros(size(ostreet,1),nsr);    %street state,1Ϊ������0Ϊ�ƻ�

bnshuchu = zeros(size(onode,1),3);
yyshuchu = zeros(size(onode,1),3);
zyshuchu = zeros(size(onode,1),3);
xtshuchu = zeros(3,3);                   %�����,Ӧ�����

yyshuchu2 = zeros(9,7);
zyshuchu2 = zeros(9,7);
ztshuchu2 = zeros(9,7); %ztΪ����
xtshuchu2 = zeros(3,3);                  %����ã��޸����


for k = 1 : 3

for n = 1 : nsr
    %��ʼ������¼����
    brstate = zeros(size(obridge,1),1);
    ststate = zeros(size(ostreet,1),1);
    tmpbn = binan;
    tmpyy = yiyuan;
    tmpzy = zhongyao;
    resultbn = ones(size(onode,1),1);
    resultyy = ones(size(onode,1),1);
    resultzy = ones(size(onode,1),1);
    
    %���������ƻ�
    for i = 1 : size(obridge,1)
        brstate(i) = (rand > obridge(i,k + 1));  %1Ϊ������0Ϊ�ƻ�
        tmp = 1;
        bstate(i,n) = brstate(i);
        %�޸�·������
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
    
    %���ɵ�·�ƻ�
    for i = 1 : size(ostreet,1)
        ststate(i) = (rand > ostreet(i,k + 4)); %1Ϊͨ����0Ϊ����
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
    
    
    %Ӧ�����ѳ����ɴ����ж�
    for i = 1 : size(onode,1)
        
        %���õ����ˡ���Ӧ�����ѳ�������ҽԺ�����������������ж�
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
        
        %��������������ճ�״̬������ı��������Լ����·����������������Ϊ�޷�����
        dis1 = ndis0bn(i);
        dis2 = ZDL(i,size(tmpbn,1),tmpbn);
        ndisbn(i,n) = dis2;
        if dis2 > tolerance * ndis0bn(i)
            resultbn(i) = 0;
        end
        nresultbn(i,n) = resultbn(i);
    end
    
	sresultbn(n) = resultbn' * onode(:,2) / sum(onode(:,2));
    
    %ҽԺ�ɴ���
    for i = 1 : size(onode,1)
        
        %���õ���ҽԺ,�������ж�
        if size(find(ohospital == i),1)
            ndisyy(i,n) = 0;
            nresultyy(i,n) = 1;
            continue
        end

        
        %��������������ճ�״̬�������ҽԺ���Լ����·����������������Ϊ�޷�����
        dis1 = ndis0yy(i);
        dis2 = ZDL(i,size(tmpyy,1),tmpyy);
        ndisyy(i,n) = dis2;
        if dis2 > tolerance * dis1
            resultyy(i) = 0;
        end
        nresultyy(i,n) = resultyy(i);
    end
    
    sresultyy(n) = resultyy' * onode(:,2) / sum(onode(:,2));
    
    %��Ҫ�����ɴ���
    for i = 1 : size(onode,1)
        
        %���õ�Ϊ��Ҫ����,�������ж�
        if size(find(ocritical == i),1)
            ndiszy(i,n) = 0;
            nresultzy(i,n) = 1;
            continue
        end

        
        %��������������ճ�״̬������ı��������Լ����·����������������Ϊ�޷�����
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
%�޸��׶�

%����Ԥ����
xiufust = zeros(1,size(ostreet,1)); %������·�޸�������ϵͳ���棬��ͨ����Ҫ�ص�Ŀɴ�����Ϊָ��
yyxiufu = zeros(nsr,7);
zyxiufu = zeros(nsr,7);
ztxiufu = zeros(nsr,7); %ҽԺ����Ҫ���������彻ͨ�Ļָ������ÿ�б�ʾһ��ģ�⣬ÿ�б�ʾ����֮��

%�ȸ���Ӧ��ģ����������ÿ����·���޸�����
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
    
    xiufugc = ones(4,size(ostreet,1)); %�޸����̣���һ��Ϊ�޸���·���ȣ��ڶ�~���зֱ�ΪҽԺ����Ҫ������ȫ����·�޸����
    xiufugc(1,:) = 10000000;
    
    %��n��ģ��Ľ���У��Ե�·�޸�����
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
    
    %�����ƻ�����޸ĵ�·����
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
    
    %��ʼ���޸�����
    xiufugc(1,1) = 0;
    xiufugc(2,1) = sresultyy(n);
    xiufugc(3,1) = sresultzy(n);
    xiufugc(4,1) = 1 - sum(ostreet(tmpst,4)) / sum(ostreet(:,4));
    
    %�Ե�·Ϊ��λ�޸�
    for i = 1 : tmpnum
        xiufugc(1,i + 1) = xiufugc(1,i) + ostreet(tmpst(i),4);
        
        %�޸ĵ�·����
        tmpyy(ostreet(tmpst(i),2),ostreet(tmpst(i),3)) = ostreet(tmpst(i),4);  
        tmpyy(ostreet(tmpst(i),3),ostreet(tmpst(i),2)) = ostreet(tmpst(i),4);  
        tmpzy(ostreet(tmpst(i),2),ostreet(tmpst(i),3)) = ostreet(tmpst(i),4);
        tmpzy(ostreet(tmpst(i),3),ostreet(tmpst(i),2)) = ostreet(tmpst(i),4);
        
        %�����޸����ϵͳָ��
        %ҽԺ
        rtmp = ones(1,size(onode,1));
        for j = 1 : size(onode,1)
        
        %���õ���ҽԺ,�������ж�
            if size(find(ohospital == j),1)
                rtmp(j) = 1;
                continue
            end
        
        %����������������ҽԺ
            dis1 = ndis0yy(j);
            dis2 = ZDL(j,size(tmpyy,1),tmpyy);
            if dis2 > tolerance * dis1
                rtmp(j) = 0;
            end
        end
        xiufugc(2,i + 1) = rtmp * onode(:,2) / sum(onode(:,2));
        xiufugc(2,i + 1) = max(xiufugc(2,i),xiufugc(2,i + 1));
        %��Ҫ
        rtmp = ones(1,size(onode,1));
        for j = 1 : size(onode,1)
        
        %���õ�����Ҫ����,�������ж�
            if size(find(ocritical == j),1)
                rtmp(j) = 1;
                continue
            end
        
        %������������������Ҫ����
            dis1 = ndis0zy(j);
            dis2 = ZDL(j,size(tmpzy,1),tmpzy);
            if dis2 > tolerance * dis1
                rtmp(j) = 0;
            end
        end
        xiufugc(3,i + 1) = rtmp * onode(:,2) / sum(onode(:,2));
        
        xiufugc(4,i + 1) = xiufugc(4,i) + ostreet(tmpst(i),4) / sum(ostreet(:,4));

    end
    
    %�����޸��ٶȣ�ת��Ϊ����ʱ���޸�����������ʽ�������
    for i = 1 : 7
        tmp = i * xiufusudu;
        tmp = max(find(xiufugc(1,:) <= tmp)) ; 
        yyxiufu(n,i) = xiufugc(2,tmp);
        zyxiufu(n,i) = xiufugc(3,tmp);
        ztxiufu(n,i) = xiufugc(4,tmp);
        
    end

end

%�������
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