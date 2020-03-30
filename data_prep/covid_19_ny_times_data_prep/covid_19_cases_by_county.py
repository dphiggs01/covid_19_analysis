import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
BASE_DIR = '../../covid-19-data'

# date,county,state,fips,cases,deaths
def fetch_data():
    # Load the data to be processed
    file_name="{}/us-counties.csv".format(BASE_DIR)
    data_set = pd.read_csv(file_name, sep=',',converters={'fips': lambda x: str(x)},parse_dates=[0],
                 date_parser=lambda t:pd.to_datetime(str(t),
                                            format='%Y-%m-%d'))
    print(data_set.columns)
    print("data_set (rows, columns) {}\n".format(data_set.shape))
    print("data_set missing values \n{}\n".format(data_set.isnull().sum()))
    dataTypeSeries = data_set.dtypes

    print('Data type of each column of Dataframe :')
    print(dataTypeSeries)
    return data_set

def select_cases_by_date(data_set, dt_str):
    #2020-03-27
    #cases_data_set = data_set.groupby('fips').agg({'county':'min','state':'min','date':'max'})
    search_dt = pd.to_datetime(str(dt_str),format='%Y-%m-%d')
    query_str = 'date == "{}"'.format(search_dt)
    cases_data_set = data_set.query(query_str)
    del cases_data_set['date']
    #cases_data_set['state_county'] = cases_data_set[['state', 'county']].agg(', '.join, axis=1)
    #cases_data_set['state_county'] = cases_data_set[['state', 'county']].apply(lambda x: ', '.join(x), axis=1)
    print(cases_data_set.head())
    return cases_data_set

def write_data(data_set):
    file_name = "{}/covid_19_cases_by_county.csv".format(BASE_DIR)
    data_set.to_csv(file_name, header=True, index=False)

if __name__=='__main__':
    print("Starting")
    data_set = fetch_data()
    data_set = select_cases_by_date(data_set,"2020-03-28")
    write_data(data_set)
