import pandas as pd
import numpy as np
import sys

def modified_min_max_scaling(data, min_val=1, max_val=10):

    # Convert data to numpy array
    data = np.array(data)

    # Shift the data to ensure non-zero minimum value
    data_shifted = data - np.min(data) + min_val

    # Scale the shifted data between min_val and max_val
    normalized_data = (data_shifted - np.min(data_shifted)) / (np.max(data_shifted) - np.min(data_shifted)) * (max_val - min_val) + min_val

    return normalized_data

def normalize_dataframe(df, min_value, max_value):

    # Normalize the values between 1 and 10
    normalized_df = ((df - min_value) / (max_value - min_value)) * 9 + 1

    # return df
    return normalized_df

def min_max_scaling(data, min_val=1, max_val=10):
    # Convert data to numpy array
    data = np.array(data)
    # Ensure non-zero minimum value and avoid division by zero
    min_data = np.min(data)
    max_data = np.max(data)
    if min_data == max_data:
        min_data -= 0.01
    # Normalize the data to the range [0, 1]
    normalized_data = (data - min_data) / (max_data - min_data)
    
    # Scale the normalized data to the new range [min_val, max_val]
    scaled_data = normalized_data * (max_val - min_val) + min_val
    
    return scaled_data

def get_priorities_T(df):
    skip_rows = 3 # no of rows to skip
    column_index = 1
    priorities_T = df.iloc[skip_rows:, column_index]
    priorities_T = priorities_T.reset_index(drop=True)
    # priorities_T = normalize_dataframe(priorities_T, priorities_T.min(), priorities_T.max())
    # print('Technical Priority List')
    # print(priorities_T)
    return priorities_T

def get_priorities_DIM(df, priorities_T): 
    skip_cols = 2
    row_index = 1
    priorities_DIM = df.iloc[row_index, skip_cols:]
    priorities_DIM = priorities_DIM.reset_index(drop=True)
    # print('DIM Priority list')
    # print(priorities_DIM)
    # priorities_DIM = normalize_dataframe(priorities_DIM, priorities_T.min(), priorities_T.max() )
    return priorities_DIM

def get_impacts(df):
    pd.set_option('future.no_silent_downcasting', True)

    df_D = df.iloc[2:, 2:]
    df_D.fillna(0, inplace=True)
    df_D.replace('U', 0, inplace=True)
    df_D.replace('+', 1, inplace=True)
    df_D.replace('-', -1, inplace=True)
    # df_D = df_D.drop(df_D.columns[[1,2]], axis=1, inplace=True)
    impacts = df_D.values.tolist()
    # print(impacts)
    return impacts

def calculate_impact_score(priorities_T, priorities_DIM, impacts):
    n = len(priorities_T)
    m = len(priorities_DIM)
    score = 0
    # print(f'Length n and m {n} {m}')

    for i in range(n):
        for j in range(m):
            score += (priorities_T[i] + priorities_DIM[j]) * impacts[i][j]
            # print(f"Impacts {j} {i}  Score: {score}")
    # score = np.log1p(score)
    # score = round(score, 2)
    return score

def get_impact_from_dfs(list_of_dfs, my_sheets):
    impact_scores = []
    for i, df in enumerate(list_of_dfs):
        # print(f"DataFrame {i+1}:")
        priorities_T = get_priorities_T(df)
        priorities_DIM = get_priorities_DIM(df, priorities_T)

        impacts = get_impacts(df)
        impact_score = calculate_impact_score(priorities_T, priorities_DIM, impacts)
        impact_scores.append(impact_score)
    #impact_scores = min_max_scaling(impact_scores, 0.1, 10)
    i=0
    for score in impact_scores:
        print(f"{my_sheets[i]} score {score}")
        i = i+1
def main():

    arguments = sys.argv
    print("Command-line arguments:", arguments)

    if len(arguments) > 1:
        filepath = arguments[1]
        decision_option = arguments[2]
        xls = pd.ExcelFile(filepath) #'../data/dmatrix.xlsx'
        sheet_names = xls.sheet_names
        sheet_Ec = decision_option+'-TEc'
        sheet_E = decision_option+'-TE'
        sheet_S = decision_option+'-TS'
        #my_sheets = [sheet_Ec, sheet_E, sheet_S]
        #list_of_dfs = []
        my_sheets = []
        df_TEc = []
        df_TE = []
        df_TS = []
        options_TEc = []
        options_TE = []
        options_TS = []
        for name in sheet_names:
            if decision_option in name:
                df_sheet= pd.read_excel(xls, name, header=None)
                if 'TEc' in name:
                    df_TEc.append(df_sheet)
                    options_TEc.append(name)
                elif 'TE' in name:
                    df_TE.append(df_sheet)
                    options_TE.append(name)
                elif 'TS' in name:
                    df_TS.append(df_sheet) 
                    options_TS.append(name)                    
                #list_of_dfs.append(df_sheet) # adding names of all sheets
        
        
        get_impact_from_dfs(df_TEc, options_TEc)
        get_impact_from_dfs(df_TE, options_TE)
        get_impact_from_dfs(df_TS, options_TS)

        # min_v = min(impact_scores)
        # max_v = max(impact_scores)
        # normalized_scores = modified_min_max_scaling(impact_scores)
        # print(normalized_scores.values)
        # for i in range(len(normalized_scores)):
        # print(f"Sustainability Impact Score ({my_sheets[i]}):" , normalized_scores)

    else:
        print("No arguments provided")


if __name__ == "__main__":
    main()