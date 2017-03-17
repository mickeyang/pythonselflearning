#compare two string to see whether one string exsits in another

text = 'abccsdcfd'
find = 'sd'
i = 0
k = 1
duplicate = False

for i in range(len(text) - 1):
    if(find[0] == text[i]):
        if(len(find) == 1):
            duplicate = True;
            start_index = i + 1;
            break;
        else:
            next_index = i + 1;
            start_index = i + 1;
            while(k < len(find)):
                if(find[k] != text[next_index]):
                    duplicate = False;
                    break;
                next_index = next_index + 1;
                k = k + 1;
                duplicate = True;
if(duplicate):
    print('Duplicate string starts from INDEX ' + str(start_index));
else:
    print('There is no duplicate');
