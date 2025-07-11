"""
* SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
* SPDX-License-Identifier: Apache-2.0
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
* https://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
"""

from __future__ import annotations

import abc

# Use typing module to handle forward reference to avoid circular imports
from typing import TYPE_CHECKING

from pxr import Usd

if TYPE_CHECKING:
    from .converter_base import ConverterBase


class ConverterBuilderBase:
    @abc.abstractmethod
    def build(self, input_material_prim: Usd.Prim, output_mdl_path: str) -> ConverterBase:
        raise NotImplementedError
