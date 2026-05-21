class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        i = 0

        while i != len(students):
            
            if students[0] == sandwiches[0]:
                print(f"Student {students[0]} takes sandwich {sandwiches[0]}")
                del students[0]
                del sandwiches[0]
                print(f"New queue {students} with sandwiches availible {sandwiches}")
                i=0
            else:
                print(f"No match with {students[0]} and sandwich {sandwiches[0]}")
                students.append(students[0])
                del students[0]
                i+=1
                print(f"New queue {students}, did {i} rotations")

        return len(students)

