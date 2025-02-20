from KKanjiRecognizer.recognize_kanji import recognize_kanji
import gradio as gr

def wrapped_function(image, black_background, confidence_threshold):
    if confidence_threshold == "":
        confidence_threshold = -999
    result = recognize_kanji(image, black_background, float(confidence_threshold))
    return f"<div style='font-size:96px; text-align:center; font-weight:bold'>{result}</div>"

with gr.Blocks(css="""
    #output-header {text-align: center; font-size: 128px !important; font-weight: bold;}
""") as demo:
    gr.Markdown("## Kanji Recognition Model")

    image_input = gr.Image(type="filepath", label="Upload Image")
    black_bg_checkbox = gr.Checkbox(label="Black Background", value=True)
    confidence_input = gr.Textbox(label="Confidence Threshold (0-1)", placeholder="Leave empty if you don't want to experiment")

    submit_btn = gr.Button("Recognize")

    gr.Markdown("### Model's Output", elem_id="output-header")  # Added text above output
    output_text = gr.Markdown("", elem_id="output-text")  # Markdown for large centered text
    
    submit_btn.click(wrapped_function, inputs=[image_input, black_bg_checkbox, confidence_input], outputs=output_text)

demo.launch()
