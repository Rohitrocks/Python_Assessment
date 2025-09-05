<h2>✨ Project Features</h2>
<h3>File Uploads</h3>
  <p>Accepts both .pdf and .docx document formats, providing flexibility for different user needs.</p>
<h3>Comprehensive Analysis</h3>
  <p>The system performs a deep analysis of the document content, checking for:</p>
  <ul>
      <li>Grammar and spelling errors.</li>
      <li>Stylistic issues (e.g., passive voice, clichés).</li>
      <li>Nuanced feedback on tone, clarity, and structure from a Large Language Model (LLM).</li>
  </ul>
<h3>Detailed Reporting</h3>
  <p>Displays a clear report with an overall score and a categorized list of specific issues and actionable suggestions.</p>
<h3>AI-Powered Rewriting</h3>
  <p>Allows users to request a fully rewritten, compliant version of their document with a single click, saving significant editing time.</p>
<h3>Interactive UI</h3>
  <p>A simple and responsive user interface built with Streamlit, ensuring an intuitive and user-friendly experience.</p>
<h3>Robust API</h3>
  <p>A backend powered by FastAPI with Pydantic data validation and automatic, interactive API documentation.</p>
  
<h2>Python environment setup</h2>
<ul>
  <li>create Python virtual env and install all the dependecies from the requirements.txt</li>
  <li>add Groq model and api key in the .env file</li>
  <li>run the fastapi server in terminal 1 by - uvicorn main:app --reload</li>
  <li>run the streamlit app in terminal 2 by -> streamlit run .\streamlitapp.py</li>
</ul>

<h2>The FastAPI server exposes the following endpoints.</h2>  
<ul>
  <h3>POST /check-document/</h3>
  <li>
      Payload: multipart/form-data with a .pdf or .docx file.
      Response: A JSON object containing the detailed analysis report.\
  </li>
  <h3>POST /fix-document/</h3>
  <li>
      Payload: A JSON object with the original text: {"text": "..."}.
      Response: The rewritten document as a downloadable .docx file.
  </li>
</ul>



