%Gives the number of frequencies for a vector of integers in the 
%range of (0,31)

function result = getFreq(text)
    result = zeros(1,32);
    for i=1:32
        result(i)=sum(text==i-1);
    end
end