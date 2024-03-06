from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import gradio as gr
# initialize the models
openai = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key="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"
)
def chatbot(user_input):
    # defining a template
    template = """Question: {question}
    Buatlah step step dari jawaban yang diberikan
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])
    formated_prompt =prompt.format(question=str(user_input))
    return openai.invoke(formated_prompt).content
demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")
demo.launch(share=True)