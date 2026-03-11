# LLM-Evaluation-Agent-Dashboard
## Liberary Install
```bash
pip install -r requirements.txt
```

## Run backend (Fast API) at Terminal one
```bash
uvicorn api.main:app --reload
```

## Run frontend (Streamlit) at Terminal two
```bash
streamlit run dashboard/app.py
```