import pandas as pd 

def calculate_demographic_data():
    df = pd.read_csv("dataset/adult.csv", header= None)

    df.columns = [
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race", "sex",
        "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"
    ]

    # Removing any leading and trailing whitespace from every string value in the DataFrame.
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # How many people of each race are represented in this dataset? (race column)
    race_count = df["race"].value_counts()

    # What is the average age of men?
    men = df[df["sex"] == "Male"]
    average_age_men = round(men["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_graduate = df[df["education"] == "Bachelors"]
    bachelor_percentage = round((bachelors_graduate.shape[0] / df.shape[0]) * 100, 1)

    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education_people = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])] 
    advanced_education_people_earning_more_than_50K = advanced_education_people[advanced_education_people["salary"] == ">50K"]
    higher_education_rich = round((advanced_education_people_earning_more_than_50K.shape[0] / advanced_education_people.shape[0]) * 100, 1)

    # What percentage of people without advanced education make more than 50K?
    people_without_advanced_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    people_without_advanced_education_earning_more_than_50K = people_without_advanced_education[people_without_advanced_education["salary"] == ">50K"]
    lower_education_rich = round((people_without_advanced_education_earning_more_than_50K.shape[0] / people_without_advanced_education.shape[0]) * 100, 1)

    # What is the minimum number of hours a person works per week?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_hours_workers = df[df["hours-per-week"] == min_work_hours]
    rich_min_hours = min_hours_workers[min_hours_workers["salary"] == ">50K"]
    rich_percentage = round((rich_min_hours.shape[0] / min_hours_workers.shape[0]) * 100, 1)

    # What country has the highest percentage of people that earn >50K and what is that percentage?
    rich_people = df[df["salary"] == ">50K"]
    country_counts_with_rich_people = rich_people["native-country"].value_counts(normalize=True) * 100
    highest_earning_country = country_counts_with_rich_people.idxmax()
    highest_earning_country_percentage = round(country_counts_with_rich_people.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_workers = df[df["native-country"] == "India"]
    india_rich_workers = india_workers[india_workers["salary"] == ">50K"]
    top_IN_occupation = india_rich_workers["occupation"].value_counts(normalize=True).idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'bachelor_percentage': bachelor_percentage,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

if __name__ == "__main__":
    results = calculate_demographic_data()
    for key, value in results.items():
        print(f"{key}:\n{value}\n")