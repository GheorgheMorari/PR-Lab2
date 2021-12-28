import torch
from transformers import AutoModelWithLMHead, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-small')
# model = AutoModelWithLMHead.from_pretrained('/content/output-small') # Use this if you trained the model
model = AutoModelWithLMHead.from_pretrained("microsoft/DialoGPT-small")  # This is a generic chatbot, lame

step = 0
chat_history_ids = None


def get_response(string):
    global chat_history_ids
    global step
    step %= 5

    new_user_input_ids = tokenizer.encode(string + tokenizer.eos_token, return_tensors='pt')

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

    # generated a response while limiting the total chat history to 1000 tokens,
    chat_history_ids = model.generate(
        bot_input_ids, max_length=200,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=3,
        do_sample=True,
        top_k=100,
        top_p=0.7,
        temperature=0.8
    )

    return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
