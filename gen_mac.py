#!/usr/bin/env python3
# vim:ts=2:sw=2:et:ai:sts=2

# Generate a MAC address suitable for KVM.

# If passed a parameter, a deterministic address is generated.
# E.g.: hostname-interface_name

import hashlib
import random
import sys

KVM_OUI = (0x52, 0x54, 0x0)

seed = sys.argv[1].encode() if len(sys.argv) > 1 else random.randbytes(8)
sha = hashlib.sha1(seed).digest()

mac = KVM_OUI + tuple(sha[:3])

print("%02x:%02x:%02x:%02x:%02x:%02x" % mac)
