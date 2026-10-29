"""Encode/decode the 21-byte ESP32 RcFrame payload. No radio transport is provided."""

from __future__ import annotations
import json
import struct

BODY=struct.Struct("<BBH8h")
FRAME_SIZE=BODY.size+1


def crc8(data: bytes) -> int:
    crc=0
    for byte in data:
        crc ^= byte
        for _ in range(8):
            crc=((crc << 1) ^ 0x07) & 0xff if crc & 0x80 else (crc << 1) & 0xff
    return crc


def encode_frame(channels, frame_id=0, version=1, flags=0) -> bytes:
    if len(channels)!=8:
        raise ValueError("RcFrame requires eight channels")
    body=BODY.pack(version,flags,frame_id,*channels)
    return body+bytes([crc8(body)])


def decode_frame(payload: bytes) -> dict:
    if len(payload)!=FRAME_SIZE:
        raise ValueError("Expected 21 bytes")
    if crc8(payload[:-1])!=payload[-1]:
        raise ValueError("CRC mismatch")
    version,flags,frame_id,*channels=BODY.unpack(payload[:-1])
    return {"protoVersion":version,"flags":flags,"frameId":frame_id,"channels":channels,"crc":payload[-1]}


if __name__=="__main__":
    frame=encode_frame([0,0,500,0,0,0,0,0],frame_id=1)
    print("Payload hex:",frame.hex(" "))
    print(json.dumps(decode_frame(frame),indent=2))
