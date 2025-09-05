<h2>Python environment setup</h2>
<ul>
  <li>create Python virtual env and install all the dependecies from the requirements.txt</li>
  <li>add Groq model and api key in the .env file</li>
  <li>run the fastapi server in terminal 1 by - uvicorn main:app --reload</li>
  <li>run the streamlit app in terminal 2 by -> streamlit run .\streamlitapp.py</li>
</ul>

<h2>The FastAPI server exposes the following endpoints. You can see the full interactive documentation at http://127.0.0.1:8000/docs.</h2>  
<ul>
  <li>POST /check-document/
      Payload: multipart/form-data with a .pdf or .docx file.
      Response: A JSON object containing the detailed analysis report.\
  </li>
  <li>POST /fix-document/
      Payload: A JSON object with the original text: {"text": "..."}.
      Response: The rewritten document as a downloadable .docx file.
  </li>
</ul>

