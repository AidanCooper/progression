import json
import os
import numpy as np
import pandas as pd
import time

def get_date(time_string):
    """Convert 13 digit timestampe to date"""
    # Use American date format for proper conversion to DateTime later
    return time.strftime("%m-%d-%Y %H:%M:%S", time.gmtime(float(time_string) / 1000))


def convert_to_csv():
    """Convert fws.json file to csv"""
    with open("fws.json") as f:
        raw = f.read()
    parsed = json.loads(raw)

    df = pd.DataFrame()
    for session in parsed:
        # Create row for session in DataFrame
        session_date = get_date(session["startTime"])
        df = pd.concat([df, pd.DataFrame(index=[session_date])], sort=False)
        
        for exercise in session["activities"]:
            # Collect exercise information
            name = exercise["name"]
            sets = exercise["performance"]["completedSets"]
            sets_list = []
            for s in sets:
                reps = s["reps"]
                weight = s["weight"]
                sets_list.append((weight, reps))
            # Populate DataFrame with exercise information
            if name not in df.columns:
                df[name] = np.nan
                df[name] = df[name].astype("object")
            df.loc[session_date, name] = sets_list

    return df.to_csv("output.csv", index=True)

if __name__ == "__main__":
    convert_to_csv()
