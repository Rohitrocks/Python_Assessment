from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from src.model import models
import src.operations.services as services


app = FastAPI(title="AI Document Compliance API")


@app.post("/upload-and-check-compliance/", response_model=models.CheckDocumentResponse)
async def check_document_compliance(file: UploadFile = File(...)):
    """
    Accepts a pdf/word document, extracts text, and returns a compliance report.
    """
    
    if not file.filename.endswith(('.pdf', '.docx')):
        raise HTTPException(status_code=400, detail="Invalid file type.")
    
    contents = await file.read()
    
    try:
        text = services.extract_text(contents, file.filename)
        report = services.check_document_rules(text)
        # Return the original text along with the report
        return {"filename": file.filename, "report": report, "original_text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/modify-document/")
async def modify_document_compliance(payload: models.FixDocumentRequest):
    """
    Takes text, modifies it, and returns a downloadable docx file.
    """
    
    original_text = payload.text
    if not original_text:
        raise HTTPException(status_code=400, detail="No text provided.")
        
    try:
        modified_text = services.modify_document_with_agent(original_text)
        output_buffer = services.create_docx_from_text(modified_text)
        
        return StreamingResponse(
            iter([output_buffer.getvalue()]),
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            headers={"Content-Disposition": "attachment; filename=modified_document.docx"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))