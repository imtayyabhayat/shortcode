# Function to calculate the number of 5-star reviews needed
def calculate_reviews(current_reviews, current_rating, desired_rating):
    total_stars = 5.0
    existing_reviews = current_reviews
    
    current_percent = (current_rating/total_stars) * 100 # 82.0
    desired_percent = (desired_rating/total_stars) * 100 # 98.0
    
    simplify_score = current_percent * current_reviews #820
    
    while True:
        if current_percent >= round(desired_percent, 2):
            break
        current_reviews += 1
        simplify_score += 100 # add 5 star i.e 100% to existing rating
        current_percent = (simplify_score)/current_reviews
        # print(current_reviews, current_percent)
        
        
    existing_reviews = current_reviews - existing_reviews
    # Check if the desired rating is achievable
    if existing_reviews < 0:
        print("The desired rating is not achievable with the current number of reviews.")
    else:
        print(f"You need approximately {existing_reviews:.2f} 5-star reviews to reach your desired rating.")

# Get user input
current_reviews = float(input("Number of Current Google Reviews: "))
current_rating = float(input("Your Current Google Star Rating (out of 5): "))
desired_rating = float(input("Desired Google Star Rating: "))

# Call the function to calculate
calculate_reviews(current_reviews, current_rating, desired_rating)
