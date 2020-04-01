if [ -d "/home/ubuntu/Applications/python_envs" ]; then
    source /home/ubuntu/Applications/python_envs/bin/activate
    PORT=80
fi
cd /home/ubuntu/Applications/covid_19_analysis
git pull
cd -

python covid_19_cases_by_county.py
python covid_19_cases_by_state.py
