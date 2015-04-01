import csv

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file in the links below:
    
    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    '''
    for name in filenames:
        with open('updated_'+name, 'wb') as updated:
            writer = csv.writer(updated, delimiter='\n')
            with open(name, 'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter='\n')
                for row in reader:
                    row_details=csv.reader(row, delimiter=',')
                    for rd in row_details:
                        row_length=len(rd)
                        index_count=1
                        for index in range(row_length): 
                            if index>2:
                                if (index_count%5)==0:
                                    writer.writerow([rd[0]+','+rd[1]+','+rd[2]+','+rd[index-4]+','+rd[index-3]+','+rd[index-2]+','+rd[index-1]+','+rd[index]])
                                index_count+=1
if __name__ == "__main__":
    
    filenames=['turnstile_110528.txt','turnstile_110604.txt']
    fix_turnstile_data(filenames)