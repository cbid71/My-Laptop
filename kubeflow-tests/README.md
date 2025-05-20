mkdir tests
python3 -m venv kubeflow-env
source kubeflow-env/bin/activate
pip install kfp
pip install pandas

python3 first-pipeline.py

on obtient un yaml qu'on peut uploadé sur kubeflow en tant que pipeline
