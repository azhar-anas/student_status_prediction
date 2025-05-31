# Addressing Challenges in an Educational Institution

## Business Understanding

Jaya Jaya Institut is a higher education institution established in 2000, with a strong reputation for producing quality graduates. However, in recent years, the institution has faced a serious challenge: an increasing number of students who do not complete their education, or dropout. This not only affects the institution's academic reputation but also reflects a lack of optimal early intervention for students potentially at risk of failing.

To address this, the management of Jaya Jaya Institut has taken the initiative to utilize collected student data to enable early detection of students at risk of dropping out. Through a data science-based approach, the institution hopes to implement proactive measures such as academic guidance, counseling, and financial assistance to improve graduation rates.

### Business Problems
Based on the business understanding outlined, the main problems faced are:
1. High student dropout rates, which negatively impact the institution's reputation.
2. The absence of a data-driven early detection system to identify students at risk of dropping out.
3. A lack of data-driven insights for strategic decision-making in supporting students.

### Project Scope
This project includes the following main stages:
1.  **Exploratory Data Analysis (EDA) and Initial Analysis**: Reviewing the `data.csv` dataset from the [Students Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance) to understand student profiles and data, as well as its distribution and correlation with their final status (graduate, enrolled, dropout). This includes:
    * Performing statistical analysis (such as chi-squared tests) to identify features significant to student status.
    * Creating visualizations to show the relationship between student status and various background factors as well as academic performance.
2.  **Data Cleaning and Preparation**: Preparing the data for analysis, including handling low-correlation data, encoding categorical features, normalizing numerical features, and upsampling data.
3.  **Analytical Dashboard Creation**: Providing an interactive dashboard that presents insights related to student performance, dropout risk factors, and filters for further exploration by the institution.
4.  **Predictive Model Development**: Developing a machine learning model capable of accurately predicting the final status of students (graduate, enrolled, dropout) using existing data and creating its prototype using Streamlit Cloud Community.
5.  **Conclusion and Strategic Recommendations**: Compiling a report of analysis results and data-driven strategic recommendations to help the institution reduce dropout rates.

### Preparation
**Data Source**:
The dataset used in this project is the [Students Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance) as recommended in the project submission guidelines. This dataset contains student details such as grades, number of credits passed, biodata, and student status like Dropout, Enrolled (still continuing studies), and Graduate (has graduated). Here are the details for each feature:
1.  `Marital status` (Categorical): Marital status of the student (1–single, 2–married, etc.).
2.  `Application mode` (Categorical): Application method used by the student.
3.  `Application order` (Categorical): Order of study program choice when applying (0 = first choice, 9 = last choice).
4.  `Course` (Categorical): Study program taken by the student.
5.  `Daytime/evening attendance` (Categorical): Class attendance time (1 = daytime, 0 = evening).
6.  `Previous qualification` (Categorical): Last qualification before university (e.g., High School, Bachelor's, Master's, etc.).
7.  `Previous qualification (grade)` (Numerical): Grade from the previous qualification (0–200).
8.  `Nacionality` (Categorical): Nationality of the student.
9.  `Mother's qualification` (Categorical): Mother's education level.
10. `Father's qualification` (Categorical): Father's education level.
11. `Mother's occupation` (Categorical): Mother's occupation.
12. `Father's occupation` (Categorical): Father's occupation.
13. `Admission grade` (Numerical): University admission grade (0–200).
14. `Displaced` (Categorical): Whether the student is from outside the region (1 = yes, 0 = no).
15. `Educational special needs` (Categorical): Whether the student has special needs (1 = yes, 0 = no).
16. `Debtor` (Categorical): Whether the student has outstanding payments (1 = yes, 0 = no).
17. `Tuition fees up to date` (Categorical): Whether the student's tuition payments are current (1 = yes).
18. `Gender` (Categorical): Gender of the student (1 = male, 0 = female).
19. `Scholarship holder` (Categorical): Whether the student receives a scholarship (1 = yes).
20. `Age at enrollment` (Numerical): Student's age at enrollment.
21. `International` (Categorical): Whether the student is an international student (1 = yes).
22. `Curricular units 1st sem (credited)` (Numerical): Number of ECTS credits credited in the 1st semester.
23. `Curricular units 1st sem (enrolled)` (Numerical): Number of ECTS credits enrolled in the 1st semester.
24. `Curricular units 1st sem (evaluations)` (Numerical): Number of evaluations in the 1st semester.
25. `Curricular units 1st sem (approved)` (Numerical): Number of ECTS credits approved in the 1st semester.
26. `Curricular units 1st sem (grade)` (Numerical): Average grade for the 1st semester (0–20).
27. `Curricular units 1st sem (without evaluations)` (Numerical): Number of curricular units without evaluations in the 1st semester.
28. `Curricular units 2nd sem (credited)` (Numerical): Number of ECTS credits credited in the 2nd semester.
29. `Curricular units 2nd sem (enrolled)` (Numerical): Number of ECTS credits enrolled in the 2nd semester.
30. `Curricular units 2nd sem (evaluations)` (Numerical): Number of evaluations in the 2nd semester.
31. `Curricular units 2nd sem (approved)` (Numerical): Number of ECTS credits approved in the 2nd semester.
32. `Curricular units 2nd sem (grade)` (Numerical): Average grade for the 2nd semester (0–20).
33. `Curricular units 2nd sem (without evaluations)` (Numerical): Number of curricular units without evaluations in the 2nd semester.
34. `Unemployment rate` (Numerical): Unemployment rate (%).
35. `Inflation rate` (Numerical): Inflation rate (%).
36. `GDP` (Numerical): Gross Domestic Product.
37. `Target` (Categorical, Target): Final student status (Dropout, Enrolled, Graduate).

**Environment Setup**:
   - Setup Environment - Anaconda -> Install Anaconda Manager first, then open a terminal and run the following commands:
      ```bash
      conda create --name ml_kit python=3.11
      conda activate ml_kit
      pip install -r requirements.txt
      ```
   - Setup Environment - Shell/Terminal (Not necessary if already installed via Anaconda)
      ```bash
      pip install pipenv
      pipenv install
      pipenv shell
      pip install -r requirements.txt
      ```
   - Setup Environment - Docker & Metabase -> Install Docker first, then open the Docker terminal and run the following commands:
      ```bash
      docker pull metabase/metabase:v0.46.4
      docker run -p 3000:3000 --name metabase metabase/metabase:v0.46.4
      ```

## Business Dashboard
The dashboard has been designed to monitor student performance based on various academic indicators and educational statuses identified during the analysis process. Here is an explanation of each component:

#### 1. Average Student Age at Enrollment
Shows that students who dropout have the highest average age, followed by those still enrolled and graduates. This indicates that age at entry may influence study success.

#### 2. Student Status Distribution
A donut/pie chart visualization shows the proportion of students with the following statuses:
- **Graduate**: 50%
- **Dropout**: 32%
- **Enrolled**: 18%

Total students: 4,424.

#### 3. Average Credits Passed
Displays a comparison of credits passed in the 1st and 2nd semesters. **Graduate** students have the most credits passed in both semesters, while **dropout** students have the fewest.

#### 4. Average Semester Grade
**Graduate** students have the highest average grades in both semesters, followed by **enrolled** and **dropout** students. This shows a correlation between early academic performance and graduation.

#### 5. Student Status by Study Program
A stacked bar chart shows a comparison of student status in each study program. Some programs like *Journalism and Communication* and *Biofuel Production Technologies* have high dropout proportions, while programs like *Informatics Engineering* have many graduates.

The dashboard is expected to help academic staff detect study programs with high dropout rates, assess the correlation between age, credits, and grades with graduation, and make data-driven decisions for more targeted academic interventions. Here's how to access the created Metabase Dashboard:

1.  Open Docker, then open its terminal and type the following command:
    ```bash
    docker start -a metabase
    ```
2.  Open a browser and type `http://localhost:3000/`
3.  Login with the following credentials:
    -   username: `name@mail.com`
    -   password: `root123`
4.  Load the `metabase.db.mv.db` file.

## Running the Machine Learning System
The Machine Learning system can be accessed as follows:
   - Running locally:
      ```bash
      streamlit run App.py
      ```
   - Running remotely/online via Streamlit Cloud Community:
      
      Access the following URL: [Student Status Prediction Jaya Jaya Institut](https://studentstatusprediction-gufymrfudm2uux6fuj9ydc.streamlit.app/)

## Conclusion
Based on the EDA process, numerical feature correlation analysis, Chi-Squared test analysis for categorical features, and feature importance results from the Random Forest model (which underwent feature selection using RFE), it was found that:
1.  **Academic features (grade and approval)** in the first and second semesters, particularly `Curricular_units_2nd_sem_approved` and `Curricular_units_2nd_sem_grade`, have the most dominant influence on predicting the final student status. This indicates that **academic performance** is a key indicator of graduation.
2.  **Admission grade (`Admission_grade`)** and **age at enrollment (`Age_at_enrollment`)** also play important roles. Higher age tends to correlate negatively with graduation, possibly related to external responsibilities or economic factors.
3.  From the categorical features perspective, the Chi-Squared test shows that **socio-economic and administrative factors** such as `Tuition_fees_up_to_date`, `Debtor`, `Scholarship_holder`, and `Parental_education/occupation` have a significant association with `Status`. This reinforces the role of **financial support and social environment** in student academic success.

## Recommended Action Items

1.  **Early Intervention for Students with Low Academic Performance**
    * Implement an early warning system based on important features like `Curricular_units_2nd_sem_approved` and `Curricular_units_2nd_sem_grade`. This system can utilize machine learning.
    * Provide mentoring or remedial programs for students who perform poorly in the early semesters.

2.  **Specialized Support for High-Risk Students**
    * Identify students who are older, married, or from vulnerable economic backgrounds (e.g., have tuition arrears or are not scholarship recipients).
    * Offer regular academic and financial counseling.

3.  **Financial Support Policies**
    * Consider expanding scholarship schemes and incentives for timely tuition fee payments.
    * Implement financial literacy education from the beginning of college to prevent students from acquiring `Debtor` status.

4.  **Curriculum and Teaching Method Evaluation**
    * Review the curriculum load in the early semesters, as early performance has been proven crucial to the final student status.

5.  **Data-Driven Analytics for Decision Making**
    * Utilize the developed machine learning model and dashboard to support the educational institution's policies for early detection and data-driven interventions (data-driven decision making).
