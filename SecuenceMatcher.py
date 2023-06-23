# imports for sequence_matcher_score method
import difflib
import MeasureExecTimes
@MeasureExecTimes.measure_execution_time
def get_sequence_matcher_score(info_1, info_2):
    sequence_matcher_score_similarity = difflib.SequenceMatcher(None, info_1, info_2).ratio()
    return sequence_matcher_score_similarity