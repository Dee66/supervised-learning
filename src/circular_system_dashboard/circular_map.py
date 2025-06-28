class CircularMap:
    def __init__(self, stages, descriptions):
        self.stages = stages
        self.descriptions = descriptions
        self.active_stage = 0

    def create_map(self):
        import plotly.graph_objects as go
        import numpy as np

        N = len(self.stages)
        angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
        radius = 1
        x = radius * np.cos(angles)
        y = radius * np.sin(angles)

        fig = go.Figure()

        # Draw arrows (circular flow)
        for i in range(N):
            j = (i + 1) % N
            fig.add_annotation(
                x=x[j], y=y[j], ax=x[i], ay=y[i],
                xref='x', yref='y', axref='x', ayref='y',
                showarrow=True, arrowhead=3, arrowsize=1.2, arrowwidth=2, opacity=0.6,
                arrowcolor="#888"
            )

        # Draw nodes
        for i in range(N):
            color = "#1976d2" if i == self.active_stage else "#e0e0e0"
            border = "#1565c0" if i == self.active_stage else "#bdbdbd"
            size = 60 if i == self.active_stage else 38
            fig.add_trace(go.Scatter(
                x=[x[i]], y=[y[i]], mode="markers+text",
                marker=dict(size=size, color=color, line=dict(width=4, color=border)),
                text=[f"<b>{self.stages[i]}</b>" if i == self.active_stage else self.stages[i]],
                textfont=dict(size=16 if i == self.active_stage else 13, color="#222"),
                textposition="bottom center",
                hoverinfo="text",
                showlegend=False
            ))

        # Highlight active stage with description
        fig.add_annotation(
            x=0, y=-1.35,
            text=f"<div style='font-size:16px;line-height:1.5;'><b>{self.stages[self.active_stage]}</b><br><span style='font-size:13px'>{self.descriptions[self.active_stage]}</span></div>",
            showarrow=False, align="center", bgcolor="#f7fbff", bordercolor="#1976d2", borderwidth=2, borderpad=8
        )

        fig.update_layout(
            width=700, height=600,
            margin=dict(l=20, r=20, t=30, b=30),
            xaxis=dict(visible=False, range=[-1.5, 1.5]),
            yaxis=dict(visible=False, range=[-1.6, 1.2]),
            plot_bgcolor='#f8f8fa',
            paper_bgcolor='#f8f8fa',
            title=dict(
                text="<b style='letter-spacing:1px;'>ML System: Production Feedback Loop</b>",
                x=0.5, y=0.98, xanchor='center', yanchor='top', font=dict(size=22, color="#222")
            )
        )
        return fig

    def update_active_stage(self, index):
        if 0 <= index < len(self.stages):
            self.active_stage = index

    def visualize_feedback_loop(self):
        return self.create_map()