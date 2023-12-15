--- 
+++ 
@@ -0,0 +1,27 @@
+from transformers import GPT2LMHeadModel, GPT2Tokenizer
+
+
+class Chatbot:
+    def __init__(self):
+        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
+        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
+
+    def process_input(self, user_input):
+        return self.tokenizer.encode(user_input, return_tensors='pt')
+
+    def generate_response(self, processed_input):
+        output = self.model.generate(processed_input, max_length=1000, pad_token_id=self.tokenizer.eos_token_id)
+        return self.tokenizer.decode(output[:, processed_input.shape[-1]:][0], skip_special_tokens=True)
+
+    def respond(self, user_input):
+        processed_input = self.process_input(user_input)
+        response = self.generate_response(processed_input)
+        return response
