class Employee:
    def __init__(
        self,
        name,
        domain,
        gender,
        completed_tasks,
        avg_working_hours,
        salary,
        previous_rating,
        presentations,
        experience,
        leaves
    ):
        self.name = name
        self.domain = domain
        self.gender = gender
        self.completed_tasks = completed_tasks
        self.avg_working_hours = avg_working_hours
        self.salary = salary
        self.previous_rating = previous_rating
        self.presentations = presentations
        self.experience = experience
        self.leaves = leaves

    
def get_employee_details():
    print("\nEnter the Following Employee Details:\n")
    name = input("\nEnter the Name of Employee: ")
    domain = input("\nEnter the Domain of the Employee: ")
    gender = input("\nEnter the Gender of the Employee: ")
    completed_tasks = int(input("\nEnter the Completed Tasks by the Employee: "))
    avg_working_hours = int(input("\nEnter the Average Working Hours of the Employee in a Week: "))
    salary = float(input("\nEnter the Salary of the Employee: "))
    previous_rating = float(input("\nEnter the Previous Rating given by the System: "))
    presentations = int(input("\nEnter the Number of Presentations Given: "))
    experience = float(input("\nEnter the Experience of the Employee (in years): "))
    leaves = int(input("\nEnter the Leaves taken by the Employee in the last year: "))

    return Employee(
        name=name,
        domain=domain,
        gender=gender,
        completed_tasks=completed_tasks,
        avg_working_hours=avg_working_hours,
        salary=salary,
        previous_rating=previous_rating,
        presentations=presentations,
        experience=experience,
        leaves=leaves
    )


def evaluate_employee(employee):
    score = 0
    explanation = []

    #completed tasks
    if employee.completed_tasks >= 100:
        score += 3
        explanation.append("High Number of Tasks Complted (+3).")
    elif employee.completed_tasks > 50:
        score += 2
        explanation.append("Moderate Number of Tasks Completed (+2).")
    else:
        score += 1
        explanation.append("Low Number of Tasks Completed (+1).")
    
    #avg_working_hours
    if employee.avg_working_hours > 40:
        score += 2
        explanation.append("Working more than 40 hours a Week (+2).")
    elif employee.avg_working_hours < 30:
        score -= 1
        explanation.append("Working less than 30 hours a Week (-1).")
    
    #salary
    if employee.salary > 70000:
        score += 2
        explanation.append("High Salary, indicating greater responsibility (+2).")
    elif employee.salary > 50000:
        score += 1
        explanation.append("Moderate Salary (+2).")
    else:
        score -= 1
        explanation.append("Less Salary (-1).")

    #previous_rating
    if employee.previous_rating >= 4:
        score += 2
        explanation.append("Previous High Performance Rating (+2).")
    elif employee.previous_rating >= 3:
        score += 1
        explanation.append("Previous Moderate Performance Rating (+1).")
    else:
        score -= 1
        explanation.append("Previous Low Performance Rating (-1).")

    #presentations
    if employee.presentations >= 10:
        score += 2
        explanation.append("Given at least 10 Presentations, indicating leadership skills (+2).")
    elif employee.presentations >= 5:
        score +=1
        explanation.append("Given 5 to 9 Presentations (+1).")
    
    #experience
    if employee.experience >= 10:
        score += 2
        explanation.append("More that 10 years of experience (+2).")
    elif employee.experience >= 5:
        score += 1
        explanation.append("More than 5 years of experience (+1).")
    else:
        score -= 1
        explanation.append("Less years of experience (-1).")

    #leaves
    if employee.leaves > 20:
        score -= 2
        explanation.append("More than 20 leaves in the last year (-2).")
    elif employee.leaves > 10:
        score -= 1
        explanation.append("10 to 20 leaves in the last year (-1).")

    # Determine the final performance evaluation
    if score >= 8:
        evaluation = "Excellent"
    elif score >= 5:
        evaluation = "Good"
    elif score >= 3:
        evaluation = "Satisfactory"
    else:
        evaluation = "Needs Improvement"
    

    # Generate a final verdict based on the evaluation
    if evaluation == "Excellent":
        verdict = (
            "The employee has demonstrated outstanding performance across several key "
            "metrics. This individual should be recognized for their efforts and considered "
            "for leadership roles or promotions."
        )
    elif evaluation == "Good":
        verdict = (
            "\nThe employee has shown solid performance with a few areas for improvement. Encouragement and development opportunities could help this individual reach even greater heights."
        )
    elif evaluation == "Satisfactory":
        verdict = (
            "\nThe employee has met the basic performance expectations, but there's room for growth. Consider providing additional training or guidance to help this individual improve."
        )
    else:
        verdict = (
            "\nThe employee's performance is below expectations. Address the areas of concern and consider closer supervision or performance improvement plans."
        )

    return evaluation, explanation, verdict



employee = get_employee_details()

performance, explanation, verdict = evaluate_employee(employee)

print(f"\nEmployee {employee.name} performance rating: {performance}\n")
print("Explanation:")
for line in explanation:
    print(f" - {line}")

print("Final Verdict:\n\n", verdict)
