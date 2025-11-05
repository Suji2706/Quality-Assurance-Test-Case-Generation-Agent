from django.shortcuts import render
import google.generativeai as genai
import logging

# Configure your Gemini API key
genai.configure(api_key="AIzaSyAOsDPLnteN6GUqe1CXRkKGIwtZZ1cfEe0")  # Replace with your actual key

def generate_testcases(request):
    testcases = None
    error_message = None

    if request.method == "POST":
        requirement = request.POST.get("requirement")

        try:
            # List all available models for your key
            available_models = [m.name for m in genai.list_models()]
            
            # Filter models that include "gemini" in their name (adjust as needed)
            candidate_models = [m for m in available_models if "gemini" in m.lower()]

            if not candidate_models:
                raise Exception("No valid Gemini models available for generate_content.")

            # Pick the first available model
            model_name = candidate_models[0]
            model = genai.GenerativeModel(model_name)

            # Generate test cases
            prompt = f"""
            You are a QA engineer. Generate detailed software test cases with steps,
            expected results, and conditions for the following requirement:
            "{requirement}"
            """
            response = model.generate_content(prompt)
            testcases = response.text

        except Exception as e:
            error_message = str(e)
            logging.error("Error generating test cases: %s", error_message)

    return render(
        request,
        "qa_generator/requirement_form.html",
        {"testcases": testcases, "error": error_message},
    )
