import numpy as np

student_scores = np.array([
    [90, 85, 78, 92],
    [75, 92, 88, 78],
    [85, 80, 95, 89],
    [56, 67, 58, 90]
   
])

average_scores = np.mean(student_scores, axis=0)
subject_with_highest_avg = np.argmax(average_scores)

subject_names = ['Math', 'Science', 'English', 'History']
subject_with_highest_avg_name = subject_names[subject_with_highest_avg]

print("Average scores for each subject:", average_scores)
print("Subject with the highest average score:", subject_with_highest_avg_name)
