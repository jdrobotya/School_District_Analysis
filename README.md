## School_District_Analysis

Overview: The purpose of this project is to perform school district analysis by using Pandas and determine whether or not eliminating of TSC School 9th grade values due to suspicion of academic dishonesty, will affect the overall analysis.

### Results:

Number of students that are in ninth grade at Thomas High School is  461. We had to remove their grades for math and reading scores. 
The new students count became  38,709. It used to be 39,170

Before THS 9th grade removal
![Screen Shot 2022-05-16 at 12 20 34 AM](https://user-images.githubusercontent.com/103322251/168519348-4257b943-48d6-4924-9dda-3adbb52488b5.png)

After THS 9th grade removal
![Screen Shot 2022-05-16 at 12 28 27 AM](https://user-images.githubusercontent.com/103322251/168519985-0f19aede-1579-4032-beff-94a9ba84a29a.png)


#### How is the district summary affected?

There was a slight change in passing  math percentage. It decreased  from 74.98% to 74.76%.
Passing reading percentage also had a negative impact after removal of THS school data. It decreased  from 85.80% to 85.65%
The overall passing  percentage decreased from %65.17 to 64.86%


#### How is the school summary affected?
There was a decrease in Average math score from 83.42% to 83.35%, and increase in Reading Average score from 83.84% to 83.89% after 9th Grade removal. 

Before 9th Grade removal 
![Screen Shot 2022-05-16 at 12 45 05 AM](https://user-images.githubusercontent.com/103322251/168521631-62a1a867-c523-4ad4-bb59-25d2e8817c91.png)

After 9th Grade removal
![Screen Shot 2022-05-16 at 12 46 59 AM](https://user-images.githubusercontent.com/103322251/168521645-0a675e7a-d641-4a3e-b704-affd8d16ecb6.png)

### How does replacing the ninth graders’ math and reading scores affect Thomas High School’s performance relative to the other schools

The replacing the ninth graders’ math and reading scores didn't affect THC school much. It still was number two out of top 5 schools, even though overall passing rate slightly decreased from 90.94% to 90.63%

Before 9th Grade removal 
![Screen Shot 2022-05-16 at 12 58 15 AM](https://user-images.githubusercontent.com/103322251/168522661-86a5b88d-e42d-4488-a03b-abf6e5cfca0b.png)

After 9th Grade removal
![Screen Shot 2022-05-16 at 12 59 28 AM](https://user-images.githubusercontent.com/103322251/168522735-51f7efa7-5f34-4f2b-b394-fe20d36225b2.png)

### How does replacing the ninth-grade scores affect the following:
Math and reading scores by grade - average reading score decreased 0.1%, reading score remained the same.
Scores by school spending - spending rate <$584 Overall passing % remains the same - 90%, $585-629	increased from 81% to 90%, $631-645 increased from 63% to 66%, $646-675 - remains the same. 
Scores by school type - overall passing percentage remains the same for all school size. 
Scores by school type - overall passing percentage remains the same for both District and Charter Schools. 

### Summary:
1. We've replaced all 9th grade THS school scores with Nan value. 
2. Replacement of reading and math scores didn't make a significant impact on  the overall passing rate results for THS school.
3. Overall passing score decreased less than 0.4%.
4. Change in THS scholl date caused some shifts in Average math and reading scores, but had no significant effect on Scores by school type, Scores by school type or Scores by school spendings. 

