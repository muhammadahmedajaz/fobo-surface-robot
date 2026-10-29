"""Reference vectors and invariants for the documentation tools."""
import importlib.util
from pathlib import Path
import unittest
import numpy as np
from scipy import signal

ROOT=Path(__file__).resolve().parents[1]


def load(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/"tools"/(name+".py"))
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


plots=load("generate_figures")
protocol=load("protocol_example")


class ReferenceChecks(unittest.TestCase):
    def test_crc_known_check_value(self):
        self.assertEqual(protocol.crc8(b"123456789"),0xF4)

    def test_wire_layout_and_signed_values(self):
        channels=[-1000,-500,0,500,1000,0,0,0]
        frame=protocol.encode_frame(channels,frame_id=0x1234)
        self.assertEqual(len(frame),21)
        self.assertEqual(frame[2:6],bytes.fromhex("34 12 18 fc"))
        self.assertEqual(protocol.decode_frame(frame)["channels"],channels)

    def test_corruption_is_rejected(self):
        frame=bytearray(protocol.encode_frame([0]*8))
        frame[5]^=1
        with self.assertRaises(ValueError):protocol.decode_frame(bytes(frame))

    def test_arduino_map_truncates_toward_zero(self):
        self.assertEqual(plots.arduino_map(-3,0,10,0,5),-1)

    def test_servo_neutral_and_clipping(self):
        cfg=plots.parameters()["firmware"]
        self.assertEqual(plots.servo_command(0,cfg),(90,1500,307))
        self.assertEqual(plots.servo_command(-1000,cfg)[0],0)
        self.assertEqual(plots.servo_command(1000,cfg)[0],180)
        for ch in range(-1000,1001):
            angle,pulse,ticks=plots.servo_command(ch,cfg)
            self.assertTrue(0<=angle<=180 and 600<=pulse<=2400 and 0<=ticks<=4095)

    def test_motor_neutral_drive_and_turn(self):
        cfg=plots.parameters()["firmware"]
        self.assertEqual(plots.motor_commands(0,50,cfg),(0,0))
        self.assertEqual(plots.motor_commands(0,1000,cfg),(1023,1023))
        self.assertEqual(plots.motor_commands(1000,0,cfg),(-1023,1023))
        self.assertEqual(plots.motor_commands(-1000,0,cfg),(1023,-1023))

    def test_heading_model_stability_and_disturbance_rejection(self):
        ref,dist,den=plots.heading_systems(plots.parameters()["heading"])
        self.assertTrue(np.all(np.roots(den).real<0))
        t=np.linspace(0,60,2401)
        _,tracking,_=signal.lsim(ref,np.ones_like(t),t)
        _,rejection,_=signal.lsim(dist,np.ones_like(t)*.3,t)
        self.assertAlmostEqual(tracking[-1],1,places=6)
        self.assertAlmostEqual(rejection[-1],0,places=6)


if __name__=="__main__":unittest.main()
