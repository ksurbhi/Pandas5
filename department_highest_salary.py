import pandas as pd
# Pythons solution 
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    sal_dict = {}
    for i in range(len(employee)):
        d_id = employee['departmentId'][i]
        salary = employee['salary'][i]
        if d_id in sal_dict:
            if salary > sal_dict[d_id]:
                sal_dict[d_id] = salary
        else:
            sal_dict[d_id] = salary
    result = []
    for i in range(len(employee)):
        name = employee['name'][i]
        salary = employee['salary'][i]
        departId = employee['departmentId'][i]
        if salary == sal_dict[departId]:
            result.append([departId, name, salary])
    deprt_dict = {}
    for j in range(len(department)):
        d_id = department['id'][j]
        name = department['name'][j]
        deprt_dict[d_id] = name
    for ele in result:
        ele[0] = deprt_dict[ele[0]]
    return pd.DataFrame(result, columns = ['Department','Employee','Salary'])

# Pandas Solution
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    df = employee.merge(department, left_on = 'departmentId',
    right_on = 'id', how = 'left')
    max_salary = df.groupby('name_y')['salary'].transform('max')
    df = df[df['salary'] == max_salary]
    return df[['name_y','name_x','salary']].rename(columns = {'name_y':'Department',
    'name_x':'Employee'})



    
