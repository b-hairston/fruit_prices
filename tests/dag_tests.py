from airflow.models import DagBag

def test_dag_loaded():
    dag_bag = DagBag(dag_folder='/path/to/your/dags/folder', include_examples=False)
    assert 'your_dag_id' in dag_bag.dags
    assert len(dag_bag.import_errors) == 0, "DAG import failures: {}".format(dag_bag.import_errors)