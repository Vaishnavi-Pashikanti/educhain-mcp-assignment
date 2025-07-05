from educhain.generators import QuestionGenerator

generator = QuestionGenerator()
mcqs = generator.generate_mcqs("Python Programming Basics", num_questions=5)

for i, mcq in enumerate(mcqs, 1):
    print(f"{i}. {mcq['question']}")
