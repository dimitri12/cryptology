%word search
%can be used to search for specific words in the text
trueKey=shiftKey;


key = zeros(191,1);
key = IntToStr(key);
word = 'inte';
word = StrToInt(word);
keyInt=StrToInt(key);
wL = length(word);
for j = 0:210
    for i = 0:wL-1
        keyInt(mod(i+j,keyLength)+1)=mod(word(i+1)-cryptInt(j+i+1),32);
    end
    key2=IntToStr(mod(-keyInt,32));
crypt2=encrypt(crypt,key2,1);
f=mod(j,keyLength);
cc=(crypt2(f+1:f+wL));
for i=1:3
 cc = [cc,' $ '];   
 cc = [cc,crypt2(i*keyLength+1+f:i*keyLength+wL+f)];
end
disp(j)
disp(cc)
end