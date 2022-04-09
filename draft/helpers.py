import glob
from typing import TypeVar, List, Mapping

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from dateutil import tz

PandasDataFrame = TypeVar('pandas.core.frame.DataFrame')

melbourne_tz = tz.gettz('Australia/Melbourne')


class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""

    def __init__(self, *args):
        self.args = args

    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)

    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)


def append_csvs_into_df(file_pattern: str, ignore_index: bool = True, sort: bool = False) -> PandasDataFrame:
    data_frames = []
    for file in glob.glob(file_pattern):
        print(f'loading: {file}')
        data_frames.append(pd.read_csv(file))
    full_dataset = pd.concat(data_frames, ignore_index=ignore_index, sort=sort)
    return full_dataset


def subset_by_meter(meter_id: int, start: str, end: str, data: List) -> PandasDataFrame:
    # ensure start and end dates are within dataset range
    if len(data) != 2:
        raise RuntimeError('max of two datasets are accepted')
    df1 = data[0].loc[pd.IndexSlice[meter_id, :], :], data[0][]]
    meter_data = dataset.loc[pd.IndexSlice[meter_id, :], :].droplevel('meter')
    min_date, max_date = meter_data.reset_index()['time'][[0, len(meter_data) - 1]]
    start = max(pd.to_datetime(start).tz_localize(melbourne_tz), min_date)
    end = min(pd.to_datetime(end).tz_localize(melbourne_tz), max_date)
    meter_data = meter_data.loc[start:end]
    return meter_data


def plot_subplots_common_x(meter_data: PandasDataFrame, hours_interval: int = 12) -> None:
    fig, ax = plt.subplots(figsize=(25, 8))
    # plot at a time

    meter_data[variables[0]].plot(ax=ax, label=f'{meter_id}', x_compat=True)
    ax.set_title(variables[0])
    ax.set_xlabel("")
    # X axis labels
    date_locator = mdates.DayLocator(interval=1)
    date_form = mdates.DateFormatter("%m-%d        ")
    ax.xaxis.set_major_locator(date_locator)
    ax.xaxis.set_major_formatter(date_form)
    if hours_interval is not None:
        hour_locator = mdates.HourLocator(interval=hours_interval)
        hour_form = mdates.DateFormatter("%H")
        ax.xaxis.set_minor_locator(hour_locator)
        ax.xaxis.set_minor_formatter(hour_form)
