from datetime import datetime


def analyze_age(dob_tuple):
   
    day, month, year = dob_tuple
    date_of_birth = datetime(year, month, day)
    
    # Hardcode today's date for consistency
    today = datetime(2026, 6, 21)
    
    # Calculate exact age in years, months, and days
    exact_years = today.year - date_of_birth.year
    exact_months = today.month - date_of_birth.month
    exact_days = today.day - date_of_birth.day
    
    # Adjust for negative days (day not reached yet in current month)
    if exact_days < 0:
        exact_months -= 1
        
        # Calculate days in the previous month
        if today.month == 1:
            prev_month = 12
            prev_year = today.year - 1
        else:
            prev_month = today.month - 1
            prev_year = today.year
        
        # Days in each month (accounting for leap years)
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Adjust February for leap year
        if (prev_year % 4 == 0 and prev_year % 100 != 0) or (prev_year % 400 == 0):
            days_per_month[1] = 29
        
        exact_days += days_per_month[prev_month - 1]
    
    # Adjust for negative months (birthday not reached yet this year)
    if exact_months < 0:
        exact_years -= 1
        exact_months += 12
    
    # Determine life stage using if-elif chains
    if exact_years < 1:
        life_stage = "Infant"
    elif exact_years < 13:
        life_stage = "Child"
    elif exact_years < 20:
        life_stage = "Teen"
    elif exact_years < 30:
        life_stage = "Young Adult"
    elif exact_years < 60:
        life_stage = "Adult"
    elif exact_years < 75:
        life_stage = "Senior"
    else:
        life_stage = "Elderly"
    
    # Return a detailed report string
    report = f"Age: {exact_years} years, {exact_months} months, {exact_days} days | Life Stage: {life_stage}"
    return report


def compare_ages(person_list):

    if not person_list:
        return "No people in the list"
    
    oldest_name = None
    youngest_name = None
    max_age_in_days = -1
    min_age_in_days = float('inf')
    
    # Fixed reference date
    today = datetime(2026, 6, 21)
    
    # Loop through all people to find oldest and youngest
    for person_name, birth_date_tuple in person_list:
        day, month, year = birth_date_tuple
        date_of_birth = datetime(year, month, day)
        
        # Calculate age in days for accurate comparison
        age_in_days = (today - date_of_birth).days
        
        # Track oldest person (maximum age in days)
        if age_in_days > max_age_in_days:
            max_age_in_days = age_in_days
            oldest_name = person_name
        
        # Track youngest person (minimum age in days)
        if age_in_days < min_age_in_days:
            min_age_in_days = age_in_days
            youngest_name = person_name
    
    # Convert days to approximate years for display
    oldest_approximate_years = max_age_in_days // 365
    youngest_approximate_years = min_age_in_days // 365
    
    return f"Oldest: {oldest_name} (~{oldest_approximate_years} years) | Youngest: {youngest_name} (~{youngest_approximate_years} years)"


# Main program: Test with family members
if __name__ == "__main__":
    # Define family members with their dates of birth (day, month, year)
    family_members = [
        ("Grandpa John", (15, 3, 1950)),
        ("Grandma Mary", (22, 7, 1952)),
        ("Dad Robert", (10, 5, 1975)),
        ("Mom Susan", (8, 9, 1978)),
        ("Me (Alex)", (21, 12, 2000)),
        ("Sister Emma", (14, 6, 2003)),
    ]
    
    # Display detailed age analysis for each family member
    print("=" * 70)
    print("DETAILED AGE ANALYSIS FOR FAMILY MEMBERS")
    print("=" * 70)
    
    for name, dob_tuple in family_members:
        report = analyze_age(dob_tuple)
        print(f"{name:20} : {report}")
    
    # Display age comparison results
    print("\n" + "=" * 70)
    print("AGE COMPARISON RESULTS")
    print("=" * 70)
    comparison_result = compare_ages(family_members)
    print(comparison_result)
    print("=" * 70)
