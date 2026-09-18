import gradio as gr
import numpy as np
from theis_drawdown_curve_calculator import calculate_theis_drawdown

def run_calculation(T, S, Q, r, t_max, N):
    if T <= 0 or S <= 0 or S > 1 or Q <= 0 or r <= 0 or t_max <= 0:
        return gr.Plot(value=None), gr.Dataframe(value=None), gr.File(value=None), "Error: All parameters must be positive and S must be between 0 and 1"
    
    try:
        results_df = calculate_theis_drawdown(T, S, Q, r, t_max, N)
        
        # Create plot
        import plotly.graph_objects as go
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=results_df['time'], y=results_df['drawdown'], mode='lines+markers', name='Drawdown'))
        fig.update_layout(
            title='Theis Drawdown Curve',
            xaxis_title='Time (days)',
            yaxis_title='Drawdown (m)',
            xaxis_type='log'
        )
        
        # Prepare CSV download
        csv_path = "/tmp/theis_results.csv"
        results_df.to_csv(csv_path, index=False)
        
        return fig, results_df, csv_path, ""
    except Exception as e:
        return gr.Plot(value=None), gr.Dataframe(value=None), gr.File(value=None), f"Error: {str(e)}"

with gr.Blocks() as demo:
    gr.Markdown("# Theis Drawdown Curve Calculator")
    with gr.Row():
        with gr.Column():
            T = gr.Number(label="Transmissivity T (m²/day)", value=100.0)
            S = gr.Number(label="Storativity S", value=0.0001)
            Q = gr.Number(label="Pumping Rate Q (m³/day)", value=500.0)
            r = gr.Number(label="Radial Distance r (m)", value=50.0)
            t_max = gr.Number(label="Max Pumping Time t_max (days)", value=1.0)
            N = gr.Slider(label="Number of Points N", minimum=20, maximum=200, step=1, value=80)
            btn = gr.Button("Calculate")
    
    with gr.Row():
        plot_output = gr.Plot(label="Drawdown vs Time")
    
    with gr.Row():
        table_output = gr.Dataframe(label="Data Table")
    
    with gr.Row():
        csv_output = gr.File(label="Download CSV")
        error_output = gr.Textbox(label="Error Message", interactive=False)
    
    btn.click(
        fn=run_calculation,
        inputs=[T, S, Q, r, t_max, N],
        outputs=[plot_output, table_output, csv_output, error_output]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
