# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems


class V1ReplicationControllerStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Swagger model

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'replicas': 'int',
            'fully_labeled_replicas': 'int',
            'observed_generation': 'int'
        }

        self.attribute_map = {
            'replicas': 'replicas',
            'fully_labeled_replicas': 'fullyLabeledReplicas',
            'observed_generation': 'observedGeneration'
        }

        self._replicas = None
        self._fully_labeled_replicas = None
        self._observed_generation = None

    @property
    def replicas(self):
        """
        Gets the replicas of this V1ReplicationControllerStatus.
        Replicas is the most recently oberved number of replicas. More info: http://releases.k8s.io/release-1.2/docs/user-guide/replication-controller.md#what-is-a-replication-controller

        :return: The replicas of this V1ReplicationControllerStatus.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """
        Sets the replicas of this V1ReplicationControllerStatus.
        Replicas is the most recently oberved number of replicas. More info: http://releases.k8s.io/release-1.2/docs/user-guide/replication-controller.md#what-is-a-replication-controller

        :param replicas: The replicas of this V1ReplicationControllerStatus.
        :type: int
        """
        self._replicas = replicas

    @property
    def fully_labeled_replicas(self):
        """
        Gets the fully_labeled_replicas of this V1ReplicationControllerStatus.
        The number of pods that have labels matching the labels of the pod template of the replication controller.

        :return: The fully_labeled_replicas of this V1ReplicationControllerStatus.
        :rtype: int
        """
        return self._fully_labeled_replicas

    @fully_labeled_replicas.setter
    def fully_labeled_replicas(self, fully_labeled_replicas):
        """
        Sets the fully_labeled_replicas of this V1ReplicationControllerStatus.
        The number of pods that have labels matching the labels of the pod template of the replication controller.

        :param fully_labeled_replicas: The fully_labeled_replicas of this V1ReplicationControllerStatus.
        :type: int
        """
        self._fully_labeled_replicas = fully_labeled_replicas

    @property
    def observed_generation(self):
        """
        Gets the observed_generation of this V1ReplicationControllerStatus.
        ObservedGeneration reflects the generation of the most recently observed replication controller.

        :return: The observed_generation of this V1ReplicationControllerStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """
        Sets the observed_generation of this V1ReplicationControllerStatus.
        ObservedGeneration reflects the generation of the most recently observed replication controller.

        :param observed_generation: The observed_generation of this V1ReplicationControllerStatus.
        :type: int
        """
        self._observed_generation = observed_generation

    def to_dict(self):
        """
        Return model properties dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Return model properties str
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
