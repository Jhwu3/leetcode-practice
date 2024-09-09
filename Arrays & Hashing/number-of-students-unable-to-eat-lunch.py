class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        total = [0, 0]
        for stu in students:
            total[stu] += 1
        
        answer = len(students) 
        for sand in sandwiches: 
            if total[sand] == 0:
                return answer 
            else: 
                total[sand] -= 1
                answer -= 1
        return 0
    
# This problem gives us two lists of 0 and 1's where one of the lists represent the student preferences for sandwiches and the
# other list represents the sandwiches avaliable indicated in a stack. This problem has the students line up in a queue, which they line
# up for the sandwiches, if the sandwich on the top of the stack is not the same as their preference, they will go to the back of the line 
# The way i solved this was through a list that stored the two types of students in a list. We needed to return the number of students that 
# are not able to eat so we initiate the answer to be the length of the students list. Then we just loop through the sandwiches list and 
# when we encounter a sandwich that a student wants, we just decrease from the toal list. But if we come to a sandwich that is no longer
# the preference of any students on the remaining queue. we will return our answer. This is because even if we have more sandwiches of the other 
# type, we can't give those out until someone takes from the top of the stack.