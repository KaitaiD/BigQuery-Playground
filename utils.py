import bq_helper


def read_bq_query(query,
                  activate_project="bigquery-public-data",
                  dataset_name="openaq"):
    """Create a helper function to execute differernt queries. """
    # initiate bq object
    open_aq = bq_helper.BigQueryHelper(active_project=activate_project,
                                       dataset_name=dataset_name)
    query_result = open_aq.query_to_pandas_safe(query)
    return query_result
