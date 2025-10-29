from transformers import pipeline
import re
class Gpt2TextGeneration:
    def c1(self,full_name,age,skills,education):
            # Load GPT-2 model
        generator = pipeline("text-generation", model="gpt2")
        # Prompt definition
        prompt = f"""
        {full_name} is a {age}-year-old technology professional with strong skills in {skills}. 
        They have a background in {education} and are passionate about creativity, innovation, and continuous learning. 
        Known for their problem-solving abilities and collaborative mindset, {full_name} consistently applies their knowledge to develop practical and meaningful solutions. 
        They take initiative, explore new ideas, and are dedicated to personal and professional growth. 
        With a positive attitude and a drive to make a real impact, {full_name} is focused on contributing to exciting projects in the technology field.
        """



    # Generate text
        output = generator(
            prompt,
            max_new_tokens=250,
            num_return_sequences=1,
            temperature=0.9,
            top_p=0.9,
            pad_token_id=50256
        )

        # -----------------------------
        # POST-PROCESSING
        # -----------------------------
        raw_text = output[0]["generated_text"]

        # Remove everything before or including "Now generate" or the original prompt
        text = re.sub(r"(?is)^.*?Now generate the full paragraph:\s*", "", raw_text)
        text = text.replace(prompt, "").strip()

        # Clean extra prompt echoes or repeated labels
        text = re.sub(r"Example style:.*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"Write a professional.*?:", "", text, flags=re.IGNORECASE)
        text = re.sub(r"Name:.*|Age:.*|Skills:.*|Education:.*", "", text)
        text = re.sub(r"\s+", " ", text).strip()

        # Remove duplicated sentences (optional)
        sentences = re.split(r'(?<=[.!?]) +', text)
        seen, unique_sentences = set(), []
        for s in sentences:
            s_clean = s.strip().lower()
            if s_clean not in seen and len(s_clean) > 3:
                seen.add(s_clean)
                unique_sentences.append(s.strip())
        text = " ".join(unique_sentences)

        print("*****************"*60, text)
        return text