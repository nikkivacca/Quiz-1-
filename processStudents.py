''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv

# create a file object to open the file in read mode

infile = open('students.csv', 'r')

# create a csv object from the file object

student_file = csv.reader(infile, delimiter = ',')

#skip the header row

next(student_file)

#create an outfile object for the pocessed record

outfile = open('processedStudents.csv', 'w')

#create a new dictionary named 'student_dict'

student_dict = dict()

#use a loop to iterate through each row of the file

    #check if the GPA is below 3.0. If so, write the record to the outfile
    
for student in student_file:
    if float(student[8]) < float(3.0):
        outfile.write(student[0] + ',' + student[1] + ',' + student[2] + ',' +
        student[3] + ',' + student[4] + ',' + student[5] + ',' +
        student[6] + ',' + student[7] + ',' + student[8] + '\n'
        )
            

    # append the record to the dictionary with the student id as the Key
    # and the value as the GPA
    
        student_dict[student[0]]= student[8]



#print the entire dictionary

print(student_dict)

#Print the student id 
student_id_choice = '567890123'

if student_id_choice in student_dict:
    print(student_id_choice)

#print out the corresponding GPA from the dictionary

    print(student_dict['567890123'])

else: 
    print('student is not in the list')
 
#close the outfile

outfile.close()






