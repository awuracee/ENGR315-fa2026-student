"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

JMU 2022-2023 Annual:
In-state total cost: 30792 USD
Out-of-state total cost: 47882 USD

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Your code here ###
#define variables for in state
in_state_principal= 30792
rate= 0.05
#n= # of years, since we are only looking for one year, n=1
n=1
ten_year_final = (in_state_principal/rate)

#define variables for out of state
out_of_state_principal=47882
rate= 0.05  
n=1
twenty_year_final= (out_of_state_principal/rate)

#printing the values
print(ten_year_final)
print(twenty_year_final)