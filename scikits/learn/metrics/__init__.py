"""
Metrics module with score functions, performance metrics and
pairwise metrics or distances computation
"""

from .metrics import confusion_matrix, roc_curve, auc, precision_score, \
                recall_score, fbeta_score, f1_score, \
                precision_recall_fscore_support, classification_report, \
                precision_recall_curve, explained_variance_score, r2_score, \
                zero_one, mean_square_error
