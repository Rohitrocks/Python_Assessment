<h2>Project Features</h2>
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
<hr>
<h2>Tech Stack</h2>
  <ul>
    <li>Backend: FastAPI, Uvicorn</li>
    <li>Frontend: Streamlit</li>
    <li>AI & NLP: Groq SDK, OpenAI SDK, language-tool-python</li>
    <li>Data Validation: Pydantic</li>
    <li>Document Parsing: python-docx, PyMuPDF</li>
    <li>Core Language: Python 3.10+</li>
</ul>
<hr>
<h2>Test Repots</h2>
  <p>Documents used for testing are also available in the src->test-reports folder</p>
  <p>Test the agent for .pdf and .docx documents to check the adherence with English guidelines</p>
  <P>Analysis report screenshot
    <img width="940" height="361" alt="image" src="https://github.com/user-attachments/assets/8907ccd8-865b-453f-9518-f59632b63d74" />
  </P>
  <p>Issues in the documents
    <img width="940" height="379" alt="image" src="https://github.com/user-attachments/assets/7167a84c-00bc-480f-b821-a4c62d74ff78" />
  </p>
<h2>Python environment setup</h2>
<ul>
  <li>create Python virtual env and install all the dependecies from the requirements.txt</li>
  <li>add Groq model and api key in the .env file</li>
  <li>run the fastapi server in terminal 1 by - uvicorn main:app --reload</li>
  <li>run the streamlit app in terminal 2 by -> streamlit run .\streamlitapp.py</li>
</ul>
<hr>
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





