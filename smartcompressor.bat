@echo off
python -m streamlit run gui_app.py --server.maxUploadSize=100000
pause