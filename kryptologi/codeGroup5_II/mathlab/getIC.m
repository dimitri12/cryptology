%Get IC value

function result = getIC(text)
    tt = getFreq(text);
    n = sum(tt);
    t2 = tt.*(tt-1);
    result=sum(t2)/(n*(n-1));
end