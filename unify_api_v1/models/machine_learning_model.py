from unify_api_v1.models.base_resource import BaseResource
from unify_api_v1.models.operation import Operation
from unify_api_v1_proto.dataset_pb2 import Dataset as DatasetProto


class MachineLearningModel(BaseResource):
    """A Unify Machine Learning model."""

    @classmethod
    def from_json(cls, client, resource_json, api_path=None):
        return super().from_json(client, resource_json, DatasetProto, api_path)

    def train(self, **options):
        """Learn from verified labels.

        :param **options: Options passed to underlying :class:`~unify_api_v1.models.operation.Operation` .
            See :func:`~unify_api_v1.models.operation.Operation.apply_options` .
        """
        op_json = self.client.post(self.api_path + ":refresh").json()
        op = Operation.from_json(self.client, op_json)
        return op.apply_options(**options)

    def predict(self, **options):
        """Suggest labels for unverified records.

        :param **options: Options passed to underlying :class:`~unify_api_v1.models.operation.Operation` .
            See :func:`~unify_api_v1.models.operation.Operation.apply_options` .
        """
        dependent_dataset = "/".join(self.api_path.split("/")[:-1])
        op_json = self.client.post(dependent_dataset + ":refresh").json()
        op = Operation.from_json(self.client, op_json)
        return op.apply_options(**options)