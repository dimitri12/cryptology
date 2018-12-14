%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%% IC analysis %%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Load crypted file in this case saved in the folder
%CryptTexts
fileID = fopen('CryptTexts/cryptGroup01.txt','r');
crypt = fscanf(fileID,'%c');
fclose(fileID);

%change to integers
cryptInt = StrToInt(crypt);

%number of points to do the IC analysis of
ICpoints = 21;
IC = zeros(ICpoints,ICpoints);

for n = 1:ICpoints
    m=length(cryptInt)-rem(length(cryptInt),n);
    samples = zeros(n,m/n);
    for i = 1:n
        samples(i,:)=cryptInt(i:n:m);
        IC(n,i)=getIC(samples(i,:));
    end
end

meanIC = sum(IC,2)./(1:ICpoints)';

figure(1)
plot(1:ICpoints, meanIC);
xlim([0 ICpoints+1]);
xlabel('Key length');
ylabel('Mean IC-value');

%get key length
[~, keyLength] = max(meanIC);


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%% Cracking the cipher %%%%%%%%%%%%%%%%%%%%

% m is the length of the crypttext with the remainder 
% after division with keylength is removed

m=length(crypt)-rem(length(crypt),keyLength);

% Get the frequencies
freq = zeros(keyLength,32);
samples = zeros(keyLength,m/keyLength);

for i = 1:keyLength
    samples(i,:)=cryptInt(i:keyLength:m);
    freq(i,:)=getFreq(samples(i,:));
end

figure(2)
hold on
for i=1:keyLength
    plot(1:32,freq(i,:));
end
hold off



%%%%%%%  Maximum likelihood fit %%%%%%%%%%%%%

%Swedish pdf of letters gotten from
%https://www.sttmedia.com/characterfrequency-swedish
SwePdf = [10.04, 1.31, 1.71, 4.9, 9.85, 1.81, 3.44, 2.85, 5.01, 0.9, 3.24, ...
    4.81, 3.55, 8.45, 4.06, 1.57, 0.01, 7.88, 5.32, 8.89, 1.86, 2.55, 0.01,0.11, ...
    0.49, 0.04, 2.1, 1.66, 1.5, 14.44, 0.42, 0.81];
SwePdf = SwePdf/sum(SwePdf);

probability = zeros(1,32);
shiftKey=zeros(1,keyLength);

for j=1:keyLength
    x = freq(j,:);
    %Shift the distribution of the frequencies and store
    %the probability P(x|y) in the probability vector
    %here y is the SwePdf
    for i = 0:31
        temp = circshift(x,i);
        %calculate probability given that temp comes from a 
        %multinomial distribution
        probability(i+1) = mnpdf(temp,SwePdf);  
    end
    %Get the index of the shift which had the highest probability
    [~,maxIndex] = max(probability);
    %Store this index in the key (-1) since matlab starts vectors at 1
    shiftKey(j) = maxIndex-1;
end

%transform the integer vector to a text key
shiftKey = IntToStr(mod(-shiftKey,32));

%decrypt using this key
crypt2 = encrypt(crypt,shiftKey,1);

%show results might need adjustments
disp(shiftKey)
disp(crypt2)



