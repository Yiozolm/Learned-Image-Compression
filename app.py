from flask import Flask, render_template
import plotly.express as px
import plotly.graph_objects as go
import plotly.utils
import json
import pandas as pd
import numpy as np
from pathlib import Path

app = Flask(__name__)

def load_evaluation_data():
    data_dir = Path('./Evaluation Result/json')
    all_data = []
    
    for json_file in data_dir.glob('*.json'):
        model_name = json_file.stem
        with open(json_file, 'r') as f:
            model_data = json.load(f)
            # Convert array format to points
            num_points = len(model_data['bpp'])
            for i in range(num_points):
                point = {
                    'model': model_name,
                    'lambda': model_data['λ'][i],
                    'bpp': model_data['bpp'][i],
                    'psnr': model_data['psnr'][i],
                    'ms-ssim': model_data['ms-ssim'][i],
                    'fid': model_data['FID'][i],
                    'lpips': model_data['LPIPS'][i],
                    'dists': model_data['DISTS'][i]
                }
                all_data.append(point)
    
    return pd.DataFrame(all_data)

def create_metric_plot(df, metric, title):
    # Create scatter plot with lines
    fig = px.scatter(df, x='bpp', y=metric, color='model',
                    title=title,
                    labels={'bpp': 'Bits Per Pixel (BPP)',
                           metric: metric.upper(),
                           'model': 'Model'},
                    template='plotly_white')
    
    # Add lines connecting points for each model
    for model in df['model'].unique():
        model_data = df[df['model'] == model].sort_values('bpp')
        fig.add_trace(
            go.Scatter(x=model_data['bpp'], y=model_data[metric],
                      mode='lines',
                      name=model + ' (line)',
                      showlegend=False,
                      line=dict(dash='solid'))
        )
    
    # Add lambda values as text labels
    for model in df['model'].unique():
        model_data = df[df['model'] == model]
        fig.add_trace(
            go.Scatter(
                x=model_data['bpp'],
                y=model_data[metric],
                mode='text',
                text=model_data['lambda'].round(4),
                textposition="top center",
                showlegend=False,
                textfont=dict(size=8, color='black')
            )
        )
    
    # Calculate x-axis range
    max_bpp = df['bpp'].max()
    dtick = 0.2  # Set tick interval to 0.2
    num_ticks = int(np.ceil(max_bpp / dtick))
    x_range = [0, (num_ticks + 0.5) * dtick]  # Add 0.5 tick space for padding
    
    # Customize layout
    fig.update_layout(
        hovermode='closest',
        plot_bgcolor='white',
        paper_bgcolor='white',
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(255, 255, 255, 0.8)'
        ),
        height=500,  # Fixed height for each plot
        xaxis=dict(
            dtick=dtick,  # Set tick interval
            range=x_range,  # Set axis range
            tickformat='.1f',  # Format ticks to 1 decimal place
            gridcolor='rgba(128, 128, 128, 0.2)',  # Light grid lines
            showgrid=True,
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='rgba(0, 0, 0, 0.3)',
            tickfont=dict(color='black')
        ),
        yaxis=dict(
            gridcolor='rgba(128, 128, 128, 0.2)',  # Light grid lines
            showgrid=True,
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='rgba(0, 0, 0, 0.3)',
            tickfont=dict(color='black')
        ),
        title=dict(
            font=dict(color='black')
        )
    )
    
    return fig

def create_all_plots(df):
    metrics = {
        'psnr': 'Rate-Distortion Curve (PSNR)',
        'ms-ssim': 'Rate-Distortion Curve (MS-SSIM)',
        'fid': 'Rate-Distortion Curve (FID)',
        'lpips': 'Rate-Distortion Curve (LPIPS)',
        'dists': 'Rate-Distortion Curve (DISTS)'
    }
    
    plots = {}
    for metric, title in metrics.items():
        if metric in df.columns:
            fig = create_metric_plot(df, metric, title)
            plots[metric] = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return plots

@app.route('/')
def index():
    df = load_evaluation_data()
    plots_json = create_all_plots(df)
    return render_template('index.html', plots_json=plots_json)

if __name__ == '__main__':
    app.run(debug=True) 