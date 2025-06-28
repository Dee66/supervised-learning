import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def compute_classification_metrics(y_true, y_pred):
    """Return a dict of standard classification metrics."""
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, average='weighted', zero_division=0),
        "recall": recall_score(y_true, y_pred, average='weighted', zero_division=0),
        "f1": f1_score(y_true, y_pred, average='weighted', zero_division=0),
    }

def compute_drift_metric(y_true, y_pred_prev, y_pred_new):
    """Example: simple drift metric as % change in predictions."""
    return np.mean(y_pred_prev != y_pred_new)