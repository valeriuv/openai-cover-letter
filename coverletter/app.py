import openai
import os
from dotenv import load_dotenv
load_dotenv()
from pypdf import PdfReader


def generate_cover_letter(first_name: str, last_name: str, company: str, position: str, description: str, cv: str = None):
	openai.api_key = str(os.getenv("OPENAI_API_KEY"))
	if cv is not None:
		enriched_prompt = f"Generate a long-form cover letter for a candidate with the name {first_name} {last_name}, who is applying for the position {position}, position description: {description} at the company {company} and whose Curriculum Vitae is this: {cv}: "
	else:
		enriched_prompt = f"Generate a long-form cover letter for a candidate with the name {first_name} {last_name}, who is applying for the position {position}, position description: {description} at the company {company}: "
	print(enriched_prompt)

	response = openai.Completion.create(
		model="text-davinci-003",
		prompt=enriched_prompt,
		max_tokens=550,
		temperature=0.8
	)

	cover_letter_text = response["choices"][0]["text"] 	# Get the output text.

	return cover_letter_text

def parse_pdf(cv):
	reader = PdfReader(cv)
	number_of_pages = len(reader.pages)
	results = []
	for i in range(0, number_of_pages):
		page = reader.pages[i]
		text = page.extract_text()
		results.append(text)
	return ''.join(results)