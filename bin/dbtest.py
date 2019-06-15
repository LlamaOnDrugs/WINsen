# -*- coding: utf-8 -*-
import pdb
from pprint import pprint
import re
import sys
import os
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), '../lib')))
import config
from models import Superblock, Proposal, GovernanceObject, Setting, Signal, Vote, Outcome, Watchdog
from models import VoteSignals, VoteOutcomes
from peewee import PeeweeException  # , OperationalError, IntegrityError
from QuantisNetd import QuantisNetDaemon
import QuantisNetlib
from decimal import Decimal
QuantisNetd = QuantisNetDaemon.from_QuantisNet_conf(config.QuantisNet_conf)
import misc
# ==============================================================================
# do stuff here

pr = Proposal(
    name='proposal7',
    url='https://testproposal.com/proposal7',
    payment_address='QM1sn2HmMcuVWtRXLbYP8RvwsZfGCK9tD1',
    payment_amount=39.23,
    start_epoch=1483250400,
    end_epoch=1491022800,
)

# sb = Superblock(
#     event_block_height = 62500,
#     payment_addresses = "QM1sn2HmMcuVWtRXLbYP8RvwsZfGCK9tD1|QMFF2uEjWCRMS8U8pjjcNQXxaHgHJhm5wL",
#     payment_amounts  = "5|3"
# )


# TODO: make this a test, mock 'QuantisNetd' and tie a test block height to a
# timestamp, ensure only unit testing a within_window method
#
# also, create the `within_window` or similar method & use that.
#
bh = 131112
bh_epoch = QuantisNetd.block_height_to_epoch(bh)

fudge = 72000
window_start = 1483689082 - fudge
window_end = 1483753726 + fudge

print("Window start: %s" % misc.epoch2str(window_start))
print("Window end: %s" % misc.epoch2str(window_end))
print("\nbh_epoch: %s" % misc.epoch2str(bh_epoch))


if (bh_epoch < window_start or bh_epoch > window_end):
    print("outside of window!")
else:
    print("Within window, we're good!")

# pdb.set_trace()
# QuantisNetd.get_object_list()
# ==============================================================================
# pdb.set_trace()
1
