import openai
import creds

def generate_cover_letter(first_name: str, last_name: str, company: str, position: str):
	openai.api_key = creds.OPENAI_API_KEY
	enriched_prompt = f"Generate a long-form cover letter for a candidate with the name {first_name} {last_name}, who is applying for the position {position} at the company {company}: "
	print(enriched_prompt)

	response = openai.Completion.create(
		model="text-davinci-003",
		prompt=enriched_prompt,
		max_tokens=550,
		temperature=0.8
	)

	cover_letter_text = response["choices"][0]["text"] 	# Get the output text.

	return cover_letter_text