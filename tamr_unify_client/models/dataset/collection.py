from tamr_unify_client.models.base_collection import BaseCollection
from tamr_unify_client.models.dataset.resource import Dataset


class DatasetCollection(BaseCollection):
    """Collection of :class:`~tamr_unify_client.models.dataset.resource.Dataset` s.

    :param client: Client for API call delegation.
    :type client: :class:`~tamr_unify_client.Client`
    :param api_path: API path used to access this collection.
        E.g. ``"projects/1/inputDatasets"``.
        Default: ``"datasets"``.
    :type api_path: str
    """

    def __init__(self, client, api_path="datasets"):
        super().__init__(client, api_path)

    def by_resource_id(self, resource_id):
        """Retrieve a dataset by resource ID.

        :param resource_id: The resource ID. E.g. ``"1"``
        :type resource_id: str
        :returns: The specified dataset.
        :rtype: :class:`~tamr_unify_client.models.dataset.resource.Dataset`
        """
        return super().by_resource_id("datasets", resource_id)

    def by_relative_id(self, relative_id):
        """Retrieve a dataset by relative ID.

        :param relative_id: The resource ID. E.g. ``"datasets/1"``
        :type relative_id: str
        :returns: The specified dataset.
        :rtype: :class:`~tamr_unify_client.models.dataset.resource.Dataset`
        """
        return super().by_relative_id(Dataset, relative_id)

    def stream(self):
        """Stream datasets in this collection. Implicitly called when iterating
        over this collection.

        :returns: Stream of datasets.
        :rtype: Python generator yielding :class:`~tamr_unify_client.models.dataset.resource.Dataset`

        Usage:
            >>> for dataset in collection.stream(): # explicit
            >>>     do_stuff(dataset)
            >>> for dataset in collection: # implicit
            >>>     do_stuff(dataset)
        """
        return super().stream(Dataset)

    def by_name(self, dataset_name):
        """Lookup a specific dataset in this collection by exact-match on name.

        :param dataset_name: Name of the desired dataset.
        :type dataset_name: str
        :return: Dataset with matching name in this collection.
        :rtype: :class:`~tamr_unify_client.models.dataset.resource.Dataset`
        :raises KeyError: If no dataset with specified name was found.
        """
        for dataset in self:
            if dataset.name == dataset_name:
                return dataset
        raise KeyError(f"No dataset found with name: {dataset_name}")
