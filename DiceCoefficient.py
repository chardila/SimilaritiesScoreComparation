def dice_coefficient(str1, str2, sizestr1, sizestr2):
    # Calculate the intersection between the sets
    intersection = len(set(str1).intersection(set(str2)))

    # Calculate the Dice coefficient
    dice_coeff = (2 * intersection) / (sizestr1 + sizestr2)

    return dice_coeff