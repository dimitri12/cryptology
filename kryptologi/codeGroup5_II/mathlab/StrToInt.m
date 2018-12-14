%Transforms a vector of characters to a vector of integers mod 32

function result = StrToInt(s)        
    result = [];
    for i=1:length(s)
        k = double(s(i));
        if (k >= 97) && (k <= 122)
			result = [result (k-97)];
        elseif (k >= 65) && (k <= 90)
            result = [result (k-65)];    
        end
        switch(k)
            case 229
                result = [result (k-203)];
            case 197
                result = [result (k-171)];
            case 228
                result = [result (k-201)];
            case 196
                result = [result (k-169)];
            case 246
                result = [result (k-218)]; 
            case 214
                result = [result (k-186)];
            case 32
                result = [result (k-3)];
            case 44
                result = [result (k-14)];
            case 46
                result = [result (k-15)];    
        end
    end
end