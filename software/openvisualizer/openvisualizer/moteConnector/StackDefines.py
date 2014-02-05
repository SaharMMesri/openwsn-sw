# DO NOT EDIT DIRECTLY!
# This file was generated automatically by GenStackDefines.py
# on Fri, 11 Oct 2013 11:22:57
#

components = {
   0: "NULL",
   1: "OPENWSN",
   2: "IDMANAGER",
   3: "OPENQUEUE",
   4: "OPENSERIAL",
   5: "PACKETFUNCTIONS",
   6: "RANDOM",
   7: "RADIO",
   8: "IEEE802154",
   9: "IEEE802154E",
  10: "RES_TO_IEEE802154E",
  11: "IEEE802154E_TO_RES",
  12: "RES",
  13: "NEIGHBORS",
  14: "SCHEDULE",
  15: "OPENBRIDGE",
  16: "IPHC",
  17: "FORWARDING",
  18: "ICMPv6",
  19: "ICMPv6ECHO",
  20: "ICMPv6ROUTER",
  21: "ICMPv6RPL",
  22: "OPENTCP",
  23: "OPENUDP",
  24: "OPENCOAP",
  25: "TCPECHO",
  26: "TCPINJECT",
  27: "TCPPRINT",
  28: "UDPECHO",
  29: "UDPINJECT",
  30: "UDPPRINT",
  31: "RSVP",
  32: "OHLONE",
  33: "HELI",
  34: "IMU",
  35: "RLEDS",
  36: "RREG",
  37: "RWELLKNOWN",
  38: "RT",
  39: "REX",
  40: "RXL1",
  41: "RINFO",
  42: "RHELI",
  43: "RRUBE",
  44: "LAYERDEBUG",
  45: "UDPRAND",
  46: "UDPSTORM",
  47: "UDPLATENCY",
  48: "TEST",
  49: "R6TUS",
}

errorDescriptions = {
   1: "received an echo request",
   2: "received an echo reply",
   3: "getData asks for too few bytes, maxNumBytes={0}, fill level={1}",
   4: "the input buffer has overflown",
   5: "the command is not allowerd, command = {0}",
   6: "unknown transport protocol {0} (code location {1})",
   7: "wrong TCP state {0} (code location {1})",
   8: "TCP reset while in state {0} (code location {1})",
   9: "unsupported port number {0} (code location {1})",
  10: "unexpected DAO (code location {0})",
  11: "unsupported ICMPv6 type {0} (code location {1})",
  12: "unsupported 6LoWPAN parameter {1} at location {0}",
  13: "no next hop",
  14: "invalid parameter",
  15: "invalid forward mode",
  16: "large DAGrank {0}, set to {1}",
  17: "packet discarded hop limit reached",
  18: "loop detected due to previous rank {0} lower than current node rank {1}",
  19: "upstream packet set to be downstream, possible loop.",
  20: "neighbors table is full (max number of neighbor is {0})",
  21: "there is no sent packet in queue",
  22: "there is no received packet in queue",
  23: "schedule overflown",
  24: "wrong celltype {0} at slotOffset {1}",
  25: "unsupported IEEE802.15.4 parameter {1} at location {0}",
  26: "got desynchronized at slotOffset {0}",
  27: "synchronized at slotOffset {0}",
  28: "large timeCorr.: {0} ticks (code loc. {1})",
  29: "wrong state {0} in end of frame+sync",
  30: "wrong state {0} in startSlot, at slotOffset {1}",
  31: "wrong state {0} in timer fires, at slotOffset {1}",
  32: "wrong state {0} in start of frame, at slotOffset {1}",
  33: "wrong state {0} in end of frame, at slotOffset {1}",
  34: "maxTxDataPrepare overflows while at state {0} in slotOffset {1}",
  35: "maxRxAckPrepapare overflows while at state {0} in slotOffset {1}",
  36: "maxRxDataPrepapre overflows while at state {0} in slotOffset {1}",
  37: "maxTxAckPrepapre overflows while at state {0} in slotOffset {1}",
  38: "wdDataDuration overflows while at state {0} in slotOffset {1}",
  39: "wdRadio overflows while at state {0} in slotOffset {1}",
  40: "wdRadioTx overflows while at state {0} in slotOffset {1}",
  41: "wdAckDuration overflows while at state {0} in slotOffset {1}",
  42: "busy sending",
  43: "sendDone for packet I didn't send",
  44: "no free packet buffer (code location {0})",
  45: "freeing unused memory",
  46: "freeing memory unsupported memory",
  47: "unsupported command {0}",
  48: "unknown message type {0}",
  49: "wrong address type {0} (code location {1})",
  50: "isBridge mismatch (code location {0})",
  51: "header too long, length {1} (code location {0})",
  52: "input length problem, length={0}",
  53: "booted",
  54: "invalid serial frame",
  55: "invalid packet frome radio, length {1} (code location {0})",
  56: "busy receiving when stop of serial activity, buffer input length {1} (code location {0})",
  57: "wrong CRC in input Buffer (input length {0})",
}