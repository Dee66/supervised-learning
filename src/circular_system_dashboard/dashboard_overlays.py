from ipywidgets import VBox, Label, FloatSlider, IntSlider
import plotly.graph_objects as go

class DashboardOverlay:
    def __init__(self):
        self.layout = VBox()
        self.metrics = {}
        self.create_overlays()

    def create_overlays(self):
        self.layout.children = [
            Label("Dashboard Metrics"),
            FloatSlider(value=0, min=0, max=100, description='Metric 1:'),
            FloatSlider(value=0, min=0, max=100, description='Metric 2:'),
            IntSlider(value=0, min=0, max=10, description='Failures:')
        ]

    def update_metrics(self, metric_values):
        for i, value in enumerate(metric_values):
            self.layout.children[i + 1].value = value

    def display(self):
        return self.layout

    def clear(self):
        self.update_metrics([0] * len(self.metrics))