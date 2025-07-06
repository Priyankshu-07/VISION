from backend.langchain_helper import question_chain

def generate_questions(text, enabled=True):
    if not enabled or not text.strip():
        return []
    try:
        result = question_chain.run(context=text)
        questions = []
        for line in result.strip().split("\n"):
            clean_line = line.strip().lstrip("0123456789.-) ")
            if clean_line:
                questions.append(clean_line)
        return questions
    except Exception as e:
        return [f"Error in generate_questions: {str(e)}"]
