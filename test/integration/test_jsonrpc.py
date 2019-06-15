import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

from quantisnetd import quantisnetDaemon
from quantisnet_config import quantisnetConfig


def test_quantisnetd():
    config_text = quantisnetConfig.slurp_config_file(config.quantisnet_conf)
    network = 'mainnet'
    is_testnet = False
    # genesis_hash = u'00000ffd590b1485b3caadc19b22e6379c733355108f107a430458cdf3407ab6'
    genesis_hash = u'00000000804bbc6a621a9dbb564ce469f492e1ccf2d70f8a6b241e26a277afa2'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'00000000a48f093611895d7452e456b646d213d238e86dc2c0db7d15fe6c555d'

    creds = quantisnetConfig.get_rpc_creds(config_text, network)
    quantisnetd = quantisnetDaemon(**creds)
    assert quantisnetd.rpc_command is not None

    assert hasattr(quantisnetd, 'rpc_connection')

    # quantisnet testnet block 0 hash == 00000000a48f093611895d7452e456b646d213d238e86dc2c0db7d15fe6c555d
    # test commands without arguments
    info = quantisnetd.rpc_command('getinfo')
    info_keys = [
        'blocks',
        'connections',
        'difficulty',
        'errors',
        'protocolversion',
        'proxy',
        'testnet',
        'timeoffset',
        'version',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    assert quantisnetd.rpc_command('getblockhash', 0) == genesis_hash
