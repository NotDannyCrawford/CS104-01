Set first to 0
Set last to length -1
Set found to FALSE
WHILE (first <= last AND NOT found)
    Set middle to (first + last)/2
    IF (item equals data[middle])
        Set found to TRUE
    ELSE
        IF (item <data[middle])
            Set last to middle - 1
    ELSE
        Set first to middle + 1
RETURN found
    
