# Copyright (c) 2020 Emanuele Bellocchia
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

# BIP-0049 specifications:
# https://github.com/bitcoin/bips/blob/master/bip-0049.mediawiki

# Imports
from .bip32_utils       import Bip32Utils
from .bip44_base        import Bip44Base, Bip44Coins
from .bip49_coin_helper import *


class Bip49Const:
    """ Class container for BIP44 constants. """

    # Specification name
    SPEC_NAME = "BIP-0049"
    # Purpose
    PURPOSE   = Bip32Utils.HardenIndex(49)
    # Allowed coins
    ALLOWED_COINS = \
        [
            Bip44Coins.BITCOIN , Bip44Coins.BITCOIN_TESTNET ,
            Bip44Coins.LITECOIN, Bip44Coins.LITECOIN_TESTNET,
            Bip44Coins.DOGECOIN, Bip44Coins.DOGECOIN_TESTNET,
            Bip44Coins.DASH    , Bip44Coins.DASH_TESTNET,
        ]
    # Map from Bip44Coins to helper classes
    COIN_TO_HELPER = \
        {
            Bip44Coins.BITCOIN  : Bip49BitcoinHelper,
            Bip44Coins.LITECOIN : Bip49LitecoinHelper,
            Bip44Coins.DOGECOIN : Bip49DogecoinHelper,
            Bip44Coins.DASH     : Bip49DashHelper,
        }


class Bip49(Bip44Base):
    """ BIP49 class. """

    def Purpose(self):
        """ Derive a child key from the purpose and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It calls the underlying _PurposeGeneric method with the current object as parameter.
        Bip44DepthError is raised is chain depth is not suitable for deriving keys.
        Bip32KeyError is raised (by Bip32) if the purpose results in an invalid key.

        Returns (Bip object):
            Bip object
        """
        return self._PurposeGeneric(self)

    def Coin(self):
        """ Derive a child key from the coin type specified at construction and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It calls the underlying _CoinGeneric method with the current object as parameter.
        Bip44DepthError is raised is chain depth is not suitable for deriving keys.
        Bip32KeyError is raised (by Bip32) if the purpose results in an invalid key.

        Returns (Bip object):
            Bip object
        """
        return self._CoinGeneric(self)

    def Account(self, acc_idx):
        """ Derive a child key from the specified account index and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It calls the underlying _AccountGeneric method with the current object as parameter.
        Bip44DepthError is raised is chain depth is not suitable for deriving keys.
        Bip32KeyError is raised (by Bip32) if the purpose results in an invalid key.

        Args:
            acc_idx (int) : account index

        Returns (Bip object):
            Bip object
        """
        return self._AccountGeneric(self, acc_idx)

    def Change(self, change_idx):
        """ Derive a child key from the specified account index and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It calls the underlying _ChangeGeneric method with the current object as parameter.
        TypeError is raised if chain type is not a Bip44Changes enum.
        Bip44DepthError is raised is chain depth is not suitable for deriving keys.
        Bip32KeyError is raised (by Bip32) if the change results in an invalid key.

        Args:
            change_idx (Bip44Changes) : change index, must a Bip44Changes enum

        Returns (Bip object):
            Bip object
        """
        return self._ChangeGeneric(self, change_idx)

    def AddressIndex(self, addr_idx):
        """ Derive a child key from the specified account index and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It calls the underlying _AddressIndexGeneric method with the current object as parameter.
        Bip44DepthError is raised is chain depth is not suitable for deriving keys.
        Bip32KeyError is raised (by Bip32) if the purpose results in an invalid key.

        Args:
            addr_idx (int) : address index

        Returns (Bip object):
            Bip object
        """
        return self._AddressIndexGeneric(self, addr_idx)

    @staticmethod
    def SpecName():
        """ Get specification name

        Returns (str):
            Specification name
        """
        return Bip49Const.SPEC_NAME

    @staticmethod
    def IsCoinAllowed(coin_idx):
        """ Get if the specified coin is allowed.
        TypeError is raised if coin_idx is not of Bip44Coins enum.

        Args:
            coin_idx (Bip44Coins) : coin index, must be a Bip44Coins enum

        Returns (bool):
            True if allowed, false otherwise
        """
        if not isinstance(coin_idx, Bip44Coins):
            raise TypeError("Coin index is not an enumerative of Bip44Coins")

        return coin_idx in Bip49Const.ALLOWED_COINS

    @staticmethod
    def _GetPurpose():
        """ Get purpose.

        Returns (int):
            Purpose
        """
        return Bip49Const.PURPOSE

    @staticmethod
    def _GetCoinHelper(coin_idx):
        """ Get coin helper.

        Args:
            coin_idx (Bip44Coins) : coin index, must be a Bip44Coins enum

        Returns (CoinHelperBase object):
            CoinHelperBase object
        """
        return Bip49Const.COIN_TO_HELPER[coin_idx]
