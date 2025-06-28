import plotly.express as px
import plotly.graph_objects as go

def plot_confusion_matrix(cm, class_names):
    """Plot a confusion matrix as a heatmap."""
    fig = px.imshow(
        cm,
        x=class_names,
        y=class_names,
        color_continuous_scale="Blues",
        labels=dict(x="Predicted", y="Actual", color="Count"),
        text_auto=True
    )
    fig.update_layout(title="Confusion Matrix", autosize=True)
    return fig

def plot_cost_curve(costs, gradients):
    """Plot cost curve with gradient (slope) at each point."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=costs, mode='lines+markers', name='Cost'))
    fig.add_trace(go.Scatter(y=gradients, mode='lines+markers', name='Gradient', yaxis='y2'))
    fig.update_layout(
        title="Cost Curve and Gradient",
        yaxis=dict(title="Cost"),
        yaxis2=dict(title="Gradient", overlaying='y', side='right')
    )
    return fig