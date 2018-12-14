%Transforms a vector of integers to a vector of characters

function result = IntToStr(IntLst)        
    result = [];
    for i=1:length(IntLst)
        if (IntLst(i) >= 0) && (IntLst(i) <= 25)
			result = [result, char(IntLst(i)+97)];
        end
        switch(IntLst(i))
            case 26
                result = [result, 'å'];
            case 27
                result = [result, 'ä'];
            case 28
                result = [result, 'ö'];
            case 29
                result = [result, ' '];
            case 30
                result = [result, ',']; 
            case 31
                result = [result, '.'];   
        end
    end
end