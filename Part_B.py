def calculate_scaling_factor(die_a, die_b):
    return sum(die_a) / sum(die_b)

def adjust_die_b_spots(die_b, scaling_factor, original_frequency, total_combinations_before):
    adjusted_frequency = [round(frequency * scaling_factor) for frequency in original_frequency]
    total_combinations_after = sum(adjusted_frequency)
    return [round(spots * total_combinations_before / total_combinations_after) for spots in die_b]

def calculate_probabilities(frequency_list, total_combinations):
    return [frequency / total_combinations for frequency in frequency_list]

def print_probabilities(probabilities, prefix=""):
    for i, probability in enumerate(probabilities):
        print("{}P(Sum={}) = {:.4f}".format(prefix, i, probability))

def undoom_dice(die_a, die_b):
    # Calculate the scaling factor based on the sum of Die A and Die B
    scaling_factor = calculate_scaling_factor(die_a, die_b)
    
    # Adjust Die A's spots to ensure they are within the limit
    a = [min(4, spots) for spots in die_a]
    
    # Calculate the total number of combinations before reattaching spots
    total_combinations_before = len(die_a) * len(die_b)
    
    # Calculate the original frequency of each sum
    original_frequency = [0] * (max(die_a) + max(die_b) + 1)
    for face_a in die_a:
        for face_b in die_b:
            original_frequency[face_a + face_b] += 1
    
    # Calculate the adjusted frequency of each sum after reattaching spots
    adjusted_frequency = [round(frequency * scaling_factor) for frequency in original_frequency]
    
    # Calculate the total number of combinations for each sum after reattaching spots
    total_combinations_after = sum(adjusted_frequency)
    
    # Adjust Die B's spots to maintain the original probabilities
    b = adjust_die_b_spots(die_b, scaling_factor, original_frequency, total_combinations_before)
    
    # Calculate probabilities before reattachment
    original_probabilities = calculate_probabilities(original_frequency, total_combinations_before)
    
    # Calculate probabilities after reattachment
    adjusted_probabilities = calculate_probabilities(adjusted_frequency, total_combinations_after)
    
    # Print probabilities before reattachment
    print("Probabilities before reattachment:")
    print_probabilities(original_probabilities, prefix="  ")
    
    # Print probabilities after reattachment
    print("\nProbabilities after reattachment:")
    print_probabilities(adjusted_probabilities, prefix="  ")
    
    return a, b

die_a = [1, 2, 3, 4, 5, 6]
die_b = die_a
new_die_a, new_die_b = undoom_dice(die_a, die_b)
print("\nModified Values of the dice:")
print("New Die A:", new_die_a)
print("New Die B:", new_die_b)
