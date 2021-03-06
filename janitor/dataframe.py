from pandas import DataFrame, Series

from .functions import (clean_names, coalesce, convert_excel_date,
                        encode_categorical, fill_empty, get_dupes,
                        get_features_targets, remove_empty, rename_column)


class JanitorSeries(Series):
    @property
    def _constructor(self):
        return JanitorSeries

    @property
    def _constructor_expanddim(self):
        return JanitorDataFrame


class JanitorDataFrame(DataFrame):
    @property
    def _constructor(self):
        return JanitorDataFrame

    @property
    def _constructor_sliced(self):
        return JanitorSeries

    def clean_names(self):
        return clean_names(self)

    def remove_empty(self):
        return remove_empty(self)

    def get_dupes(self, columns=None):
        return get_dupes(self, columns)

    def encode_categorical(self, columns):
        return encode_categorical(self, columns)

    def rename_column(self, old, new):
        return rename_column(self, old, new)

    def get_features_targets(self, target_columns, feature_columns=None):
        return get_features_targets(self, target_columns, feature_columns)

    def coalesce(self, columns, new_column_name):
        return coalesce(self, columns, new_column_name)

    def convert_excel_date(self, column):
        return convert_excel_date(self, column)

    def fill_empty(self, columns, value):
        return fill_empty(self, columns, value)
