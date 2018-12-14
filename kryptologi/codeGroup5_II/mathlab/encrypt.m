%encryption of text using key
%flag = 1 means decryption instead

function result = encrypt(text, key, flag)
    
    key = StrToInt(key);
    if flag == 1
        key = -key;
    end
    text = StrToInt(text);
    
    n = length(key);
    m = length(text);
    remainder = rem(m,n);
    keymat = repmat(key,1,floor(m/n));
    if remainder ~= 0
        keymat = [keymat, key(1:remainder)];
    end
    result = mod(text+keymat,32);
    result = IntToStr(result);
end