source venv/bin/activate
python3 json_to_txt.py
mkdir input
python3 split.py
rm input/input_0*
head -n 15 input_10.txt
mv input_10.txt input_00.txt
gsutil cp -r input/ gs://input_translation/
export GOOGLE_APPLICATION_CREDENTIALS="/home/hardy/Downloads/BTP/Translation-b6982f821804.json"
python3 auth_check.py
python3 translation.py
mkdir output
gsutil cp -r gs://out_translation/ output/
python3 merge.py
