import pandas as pd

def data_creation(df:pd.DataFrame, name_ids:str, name_dates:str, name_act:str):
    '''
    This code generates the main database, which then will be processed
    From the grouped by card_id dataframe time serieses are processed in list
    of numpy arrays, with dates and purchase amounts, where dates are in datetime format.
    Only authorized transactions were taken into account.

    df - data frame with three columns:
        1 - ids
        2 - dates
        3 - activities (ids or amounts)

    name_ids = name of column with ids
    name_dates = name of column in df, in which dates occur
    name_act = name of columns in df, in which activities are specified

    function returns np.array of time serieses and array of titles
    '''
    grouped = df.groupby(name_ids)
    counter = 0
    data = []
    titles = []
    for name, group in grouped:
        #     if counter == 20:
        #         break
        # ~ group = group.sort_values(by = 'purchase_date')

        titles.append(group[name_ids].iloc[0])
        data.append(np.array(group[[name_dates, name_act]]))
        counter += 1

        print(counter)

    for i in data:
        i[:, 0] = i[:, 0].astype('datetime64[s]').tolist()

    return data, titles