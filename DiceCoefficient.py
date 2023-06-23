import MeasureExecTimes
@MeasureExecTimes.add_logging
def get_dice_coefficient_score(str1, str2):

    sizestr1, sizestr2 = len(set(str1)), len(set(str2))
    # Calculate the intersection between the sets
    intersection = len(set(str1).intersection(set(str2)))

    # Calculate the Dice coefficient
    dice_coeff = (2 * intersection) / (sizestr1 + sizestr2)

    return dice_coeff