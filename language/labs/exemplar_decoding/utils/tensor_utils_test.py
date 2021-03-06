# coding=utf-8
# Copyright 2018 The Google AI Language Team Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for tensor_utils.py."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from language.labs.exemplar_decoding.utils import tensor_utils

import tensorflow as tf


class TensorUtilsTest(tf.test.TestCase):

  def test_linear_interpolation(self):
    with tf.Graph().as_default():
      result = tensor_utils.linear_interpolation([1, 2, 3, 4, 5], 2, 10)
      with tf.Session("") as sess:
        tf_result = sess.run(result)
        self.assertAllEqual(tf_result, [2, 4, 6, 8, 10])


if __name__ == "__main__":
  tf.test.main()
