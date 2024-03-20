class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # queue for student line
        # stack for sandwiches
        # output is num of students who doesnt get preferred sandwich

        # [ 1, 1, 1, 0, 0, 1 ] students
        # [ 1, 0, 0, 0, 1, 1 ] sandwich

        '''
         - front student leaves with top of the sandwich
         [ 1, 1, 0, 0, 1 ]
         [ 0, 0, 0, 1, 1 ]
         
         - front student returns the back of the line
         [1, 0, 0, 1, 1]
         [0, 0, 0, 1, 1]

         - front student returns the back of the line
         [0, 0, 1, 1, 1]
         [0, 0, 0, 1, 1]

         - front student leaves with top of the sandwich
         [ 0, 1, 1, 1]
         [ 0, 0, 1, 1]

         - front student leaves with top of the sandwich
         [ 1, 1, 1]
         [ 0, 1, 1]


        '''

        while len(students) is not 0:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else: 
                top = students.pop(0)
                students.append(top)

                if sandwiches[0] not in students:
                    break


        
        return len(students)




        