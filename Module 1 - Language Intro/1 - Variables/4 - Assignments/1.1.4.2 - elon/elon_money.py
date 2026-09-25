"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
Note that Elon's capital will be $33B.
"""

### all your code below ###
#tenyrperiod
principal= 44000000000
rate10yrs=0.0396
n10yrs=10

#twentyyrperiod
principal2= 44000000000
rate20yrs=0.0432
n20yrs=20

# final answer for 10-year
ten_year_final = (principal*((1+rate10yrs/100))**n10yrs)
print(ten_year_final)
# final answer for 20-year
twenty_year_final = (principal2*((1+rate20yrs/100))**n20yrs)
print(twenty_year_final)