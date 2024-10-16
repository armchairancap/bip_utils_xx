# Copyright (c) 2021 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""Module for getting Substrate coins configuration."""

# Imports
from typing import Dict

from bip_utils.substrate.conf.substrate_coin_conf import SubstrateCoinConf
from bip_utils.substrate.conf.substrate_coins import SubstrateCoins
from bip_utils.substrate.conf.substrate_conf import SubstrateConf


class SubstrateConfGetterConst:
    """Class container for Substrate configuration getter constants."""

    # Map from SubstrateCoins to configuration classes
    COIN_TO_CONF: Dict[SubstrateCoins, SubstrateCoinConf] = {
        SubstrateCoins.ACALA: SubstrateConf.Acala,
        SubstrateCoins.BIFROST: SubstrateConf.Bifrost,
        SubstrateCoins.CHAINX: SubstrateConf.ChainX,
        SubstrateCoins.EDGEWARE: SubstrateConf.Edgeware,
        SubstrateCoins.GENERIC: SubstrateConf.Generic,
        SubstrateCoins.KARURA: SubstrateConf.Karura,
        SubstrateCoins.KUSAMA: SubstrateConf.Kusama,
        SubstrateCoins.MOONBEAM: SubstrateConf.Moonbeam,
        SubstrateCoins.MOONRIVER: SubstrateConf.Moonriver,
        SubstrateCoins.PHALA: SubstrateConf.Phala,
        SubstrateCoins.PLASM: SubstrateConf.Plasm,
        SubstrateCoins.POLKADOT: SubstrateConf.Polkadot,
        SubstrateCoins.SORA: SubstrateConf.Sora,
        SubstrateCoins.STAFI: SubstrateConf.Stafi,
        SubstrateCoins.XX: SubstrateConf.XX,
    }


class SubstrateConfGetter:
    """
    Substrate configuration getter class.
    It allows to get the Substrate configuration of a specific coin.
    """

    @staticmethod
    def GetConfig(coin_type: SubstrateCoins) -> SubstrateCoinConf:
        """
        Get coin configuration.

        Args:
            coin_type (SubstrateCoins): Coin type

        Returns:
            SubstrateCoinConf: Coin configuration

        Raises:
            TypeError: If coin type is not of a SubstrateCoins enumerative
        """
        if not isinstance(coin_type, SubstrateCoins):
            raise TypeError("Coin type is not an enumerative of SubstrateCoins")
        return SubstrateConfGetterConst.COIN_TO_CONF[coin_type]
