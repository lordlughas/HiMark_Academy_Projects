"""
Assignment:
Creates an admission program to calculate the aggregate score and tell the students the faculty and department he
or she is likely to be admitted to.
Date given: 19th Oct. 2022
Instructor: Mr Samuel Abimbola
"""
# student inputs scores offered on the following subjects; maths, english, biology, physics
student_name = input("Full name:")
maths = int(input("Mathemetics= "))
english = int(input("English= "))
biology = int(input("Biology= "))
physics = int(input("Physics= "))

# aggregate of the students score
agg_score = int((maths + english + biology + physics)/ 4)

print(agg_score)
#conditional  statement to inform the students of the admitted department
if agg_score >= 80 and agg_score <= 100:
    print("Congratulations, make a choice for your admission into Medicine or Law")
elif agg_score >= 75 and agg_score <= 79:
    print("Congratulations, maake a choice for your admission into Banking and Finance, Insurance or Accountancy")
elif agg_score >= 71 and agg_score <= 74:
    print("Congratulations, make a choice for your admission into Pharmacy, Physiology, Pharmacology or Nursing")
elif agg_score >= 61 and agg_score <= 70:
    print("Congratulations, make a choice for your admission into Computer Science, Psychology or Statistics")
elif agg_score >= 55 and agg_score <= 60:
    print("Congratulations, make a choice for your addmission into Botany or Zoology")
elif agg_score >= 50 and agg_score <= 54:
    print("Congratulations, make a choice for your admission into Agric Science, Animal Science or Soil Science")
elif agg_score >= 0 and agg_score <= 49:
    print("Sorry, You have not been admitted. Better Luck next time!")



