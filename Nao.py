from naoqi import ALProxy

class Nao:
    def __init__(self):

        # Nao configuration

        IP = "192.168.1.108"
        self.motion = ALProxy("ALMotion", IP, 9559)
        self.posture = ALProxy("ALRobotPosture", IP, 9559)
        self.tts = ALProxy("ALTextToSpeech", IP, 9559)

    def standUp(self):
        print "Stand Up"

        # Choregraphe simplified export in Python.
        
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([ 0.60000, 0.76000, 0.92000, 1.40000, 2.04000, 2.80000, 3.60000, 4.40000])
        keys.append([ 0.37119, 0.36965, 0.22689, 0.27576, 0.15708, 0.34971, 0.37886, 0.37886])

        names.append("HeadYaw")
        times.append([ 0.60000, 0.76000, 0.92000, 1.40000, 2.04000, 2.80000, 3.60000, 4.40000])
        keys.append([ 0.00149, -0.27925, -0.34826, -0.47124, -0.52360, -0.28690, -0.00940, -0.00940])

        names.append("LAnklePitch")
        times.append([ 0.60000, 0.76000, 0.92000, 1.16000, 1.40000, 1.72000, 2.04000, 2.24000, 2.48000, 2.80000, 3.60000, 4.00000, 4.40000])
        keys.append([ 0.77616, 0.75542, 0.75542, 0.92258, 0.75398, 0.28449, -0.45379, -0.68068, -0.82729, -1.09956, -1.18944, -1.18944, -0.73636])

        names.append("LAnkleRoll")
        times.append([ 0.60000, 0.76000, 0.92000, 1.40000, 2.04000, 2.24000, 2.48000, 2.80000, 3.60000, 4.00000, 4.40000])
        keys.append([ -0.05058, -0.00550, 0.02671, -0.17453, -0.39573, -0.08681, -0.30369, -0.10379, 0.01078, -0.01683, -0.08893])

        names.append("LElbowRoll")
        times.append([ 0.60000, 0.76000, 0.92000, 1.40000, 1.72000, 2.04000, 2.80000, 3.00000, 3.60000, 4.40000])
        keys.append([ -1.06302, -0.93416, -0.79304, -0.94183, -1.06762, -0.62430, -0.89121, -0.85133, -1.23636, -1.07836])

        names.append("LElbowYaw")
        times.append([ 0.60000, 0.76000, 0.92000, 1.40000, 1.72000, 2.04000, 2.80000, 3.00000, 3.60000, 4.40000])
        keys.append([ -0.54461, -0.71182, -0.73636, -0.81766, -0.29764, -0.16265, -0.86982, -1.01402, -0.92044, -0.36513])

        names.append("LHand")
        times.append([ 0.60000, 0.76000, 0.92000])
        keys.append([ 0.00032, 0.00116, 0.00126])

        names.append("LHipPitch")
        times.append([ 0.60000, 0.76000, 0.92000, 1.40000, 2.04000, 2.24000, 2.80000, 3.00000, 3.60000, 4.00000, 4.40000])
        keys.append([ -1.57077, -1.53589, -1.53589, -1.53589, -0.85706, -0.59586, -0.05236, -0.40143, -0.69026, -0.75469, -0.73014])

        names.append("LHipRoll")
        times.append([ 0.60000, 0.76000, 0.92000, 1.40000, 2.04000, 2.24000, 2.80000, 3.60000, 4.00000, 4.40000])
        keys.append([ 0.13964, 0.14501, 0.14808, 0.54105, 0.15498, -0.02526, -0.17453, 0.18259, 0.44030, 0.13043])

        names.append("LHipYawPitch")
        times.append([ 0.60000, 0.76000, 0.92000, 2.04000, 2.24000, 2.80000, 3.60000, 4.00000, 4.40000])
        keys.append([ -0.67645, -0.65173, -0.75144, -0.49909, -0.64559, -0.85897, -0.43408, -0.28221, -0.17330])

        names.append("LKneePitch")
        times.append([ 0.60000, 0.76000, 0.92000, 1.40000, 2.04000, 2.24000, 2.80000, 3.60000, 4.00000, 4.40000])
        keys.append([ 0.72401, 0.95923, 1.18473, 1.17810, 2.11255, 2.11255, 2.11255, 2.00182, 2.11253, 1.61833])

        names.append("LShoulderPitch")
        times.append([ 0.60000, 0.76000, 0.92000, 1.40000, 1.72000, 2.04000, 2.80000, 3.00000, 3.60000, 4.40000])
        keys.append([ 0.49567, 0.57421, 0.62657, 1.01393, 0.65101, 0.18675, 1.12050, 1.17286, 1.40848, 1.06814])

        names.append("LShoulderRoll")
        times.append([ 0.60000, 0.68000, 0.76000, 0.92000, 1.40000, 1.72000, 2.04000, 2.80000, 3.00000, 3.60000, 4.40000])
        keys.append([ 0.24386, 0.49393, 0.41567, 0.50964, 0.75398, 0.61087, 0.51078, 0.07666, 0.15489, 0.68872, 0.59208])

        names.append("LWristYaw")
        times.append([ 0.60000, 0.76000, 0.92000])
        keys.append([ -0.74250, -0.77164, -0.73636])

        names.append("RAnklePitch")
        times.append([ 0.60000, 0.76000, 0.92000, 1.16000, 1.40000, 1.72000, 2.04000, 2.24000, 2.36000, 2.48000, 2.80000, 3.00000, 3.20000, 3.60000, 4.00000, 4.40000])
        keys.append([ 0.78545, 0.76027, 0.76027, 0.87092, 0.66323, 0.93201, 0.78540, 0.66976, 0.71384, 0.24260, 0.78540, 0.78540, 0.59341, 0.71384, -0.36965, -0.78843])

        names.append("RAnkleRoll")
        times.append([ 0.60000, 0.76000, 0.92000, 1.40000, 2.04000, 2.24000, 2.48000, 2.80000, 3.00000, 3.20000, 3.60000, 4.00000, 4.40000])
        keys.append([ 0.04913, 0.00073, -0.00081, 0.17453, 0.00929, 0.07436, -0.15708, -0.10472, 0.24435, 0.39776, 0.39776, 0.39776, 0.09055])

        names.append("RElbowRoll")
        times.append([ 0.60000, 0.76000, 0.92000, 1.16000, 1.40000, 2.04000, 2.36000, 2.80000, 3.00000, 3.60000, 4.40000])
        keys.append([ 1.21650, 1.02936, 0.68114, 0.85521, 0.03491, 0.07981, 0.05987, 0.03491, 0.33292, 0.49706, 0.97260])

        names.append("RElbowYaw")
        times.append([ 0.60000, 0.76000, 0.92000, 1.40000, 2.04000, 2.36000, 2.80000, 3.00000, 3.60000, 4.40000])
        keys.append([ 0.48010, 1.82235, 2.05399, -0.08727, -0.08134, -0.07674, -0.06600, 0.31596, 1.67969, 0.96638])

        names.append("RHand")
        times.append([ 0.60000, 0.76000, 0.92000])
        keys.append([ 0.00032, 0.00221, 0.00244])

        names.append("RHipPitch")
        times.append([ 0.60000, 0.76000, 0.92000, 1.40000, 2.04000, 2.24000, 2.80000, 3.60000, 4.00000, 4.40000])
        keys.append([ -1.55245, -1.53589, -1.53589, -1.53589, -1.52484, -1.53589, -1.53589, -0.84988, -0.67807, -0.64892])

        names.append("RHipRoll")
        times.append([ 0.60000, 0.76000, 0.92000, 1.40000, 2.04000, 2.24000, 2.80000, 3.60000, 4.00000, 4.40000])
        keys.append([ -0.14415, -0.13336, -0.21006, -0.54105, -0.55842, -0.73468, -0.61087, -0.25460, -0.08126, -0.07512])

        names.append("RKneePitch")
        times.append([ 0.60000, 0.76000, 0.92000, 1.40000, 2.04000, 2.24000, 2.80000, 3.20000, 3.60000, 4.00000, 4.40000])
        keys.append([ 0.84374, 0.95426, 1.21504, 1.03323, 1.22173, 1.27333, 1.09956, 0.95295, 0.59523, 1.44047, 1.58006])

        names.append("RShoulderPitch")
        times.append([ 0.60000, 0.68000, 0.76000, 0.92000, 1.16000, 1.40000, 2.04000, 2.36000, 2.80000, 3.00000, 3.60000, 4.40000])
        keys.append([ 0.56609, 0.73304, 1.32695, 1.96664, 2.08567, 2.08560, 2.06787, 2.08560, 2.02799, 1.61381, 1.42359, 1.21650])

        names.append("RShoulderRoll")
        times.append([ 0.60000, 0.76000, 0.92000, 1.16000, 1.40000, 2.04000, 2.36000, 2.80000, 3.00000, 3.60000, 4.40000])
        keys.append([ -0.35133, -0.67500, -0.63819, -0.82729, -0.00873, -0.50933, -0.55382, -0.56455, -0.66580, -0.57683, -0.26236])

        names.append("RWristYaw")
        times.append([ 0.60000, 0.76000, 0.92000])
        keys.append([ 1.07529, 1.09523, 1.08756])

        try:
          # uncomment the following line and modify the IP if you use this script outside Choregraphe.
          # motion = ALProxy("ALMotion", IP, 9559)
          motion = ALProxy("ALMotion")
          motion.angleInterpolation(names, keys, times, True);
        except BaseException, err:
          print err

        pass

    def sitDown(self):
        print "Sit Down"
        self.posture.goToPosture("Sit", .8)
        pass

    def crouch(self):
        print "Crouch"
        self.posture.goToPosture("Crouch", .8)
        pass
    
    def stop(self):
        print "Stop"
        self.motion.walkTo(0.0, 0.0, 0.0)
        pass

    def moveForwardShort(self):
        print "Move Forward (Short)"
        self.motion.walkTo(0.2, 0.0, 0.0)
        pass

    def moveForwardLong(self):
        print "Move Forward (Long)"
        self.motion.walkTo(0.6, 0.0, 0.0)
        pass
        
    def moveBackward(self):
        print "Move Backward"
        self.motion.walkTo(-0.15, 0.0, 0.0)
        pass

    def turnLeft(self):
        print "Turn Left"
        self.motion.walkTo(0.0, 0.0, 0.5)
        pass

    def turnRight(self):
        print "Turn Right"
        self.motion.walkTo(0.0, 0.0, -0.5)
        pass

    def leftKick(self):
        print "Left Kick"

        # Choregraphe simplified export in Python.
        
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([ 1.16000, 2.68000, 3.20000, 4.24000, 5.12000, 7.48000])
        keys.append([ 0.04363, 0.26180, 0.17453, -0.27925, -0.26180, -0.24241])

        names.append("HeadYaw")
        times.append([ 1.16000, 2.68000, 3.20000, 4.24000, 5.12000, 7.48000])
        keys.append([ -0.00464, 0.00149, -0.00311, 0.04905, 0.03371, 0.02459])

        names.append("LAnklePitch")
        times.append([ 1.04000, 1.32000, 1.76000, 2.24000, 2.56000, 2.84000, 3.08000, 3.36000, 3.68000, 4.12000, 5.00000, 7.16000])
        keys.append([ 0.08727, -0.08727, -0.59341, -0.40143, 0.12217, -0.05236, -0.12217, 0.24435, -0.12217, -0.64403, -0.21991, 0.11356])

        names.append("LAnkleRoll")
        times.append([ 1.04000, 2.56000, 3.08000, 3.36000, 4.12000, 5.00000, 7.16000])
        keys.append([ -0.40143, -0.10887, -0.13802, 0.00000, -0.18097, -0.34558, -0.05066])

        names.append("LElbowRoll")
        times.append([ 1.00000, 2.52000, 3.04000, 4.08000, 4.96000, 7.00000])
        keys.append([ -0.64117, -1.15353, -1.38056, -1.36062, -0.96024, -0.45564])

        names.append("LElbowYaw")
        times.append([ 1.00000, 2.52000, 3.04000, 4.08000, 4.96000, 7.00000])
        keys.append([ -0.99714, -0.86368, -0.90970, -0.63205, -0.84834, -1.49714])

        names.append("LHand")
        times.append([ 1.00000, 2.52000, 3.04000, 4.08000, 4.96000, 7.00000])
        keys.append([ 0.00129, 0.00136, 0.00132, 0.00128, 0.00133, 0.00391])

        names.append("LHipPitch")
        times.append([ 1.04000, 2.56000, 3.08000, 3.36000, 4.12000, 5.00000, 7.16000])
        keys.append([ 0.16265, -0.39726, -1.11876, -1.11978, -0.78540, -0.29142, 0.21318])

        names.append("LHipRoll")
        times.append([ 1.04000, 2.56000, 3.08000, 3.36000, 4.12000, 5.00000, 7.16000])
        keys.append([ 0.47124, 0.54001, 0.32218, 0.12276, 0.36360, 0.41713, 0.05825])

        names.append("LKneePitch")
        times.append([ 1.04000, 2.56000, 2.84000, 3.08000, 3.36000, 4.12000, 5.00000, 7.16000])
        keys.append([ -0.08901, 1.97575, 1.97222, 1.23918, 0.24435, 1.53589, 0.62430, -0.07666])

        names.append("LShoulderPitch")
        times.append([ 1.00000, 2.52000, 3.04000, 4.08000, 4.96000, 7.00000])
        keys.append([ 1.52782, 1.46033, 1.47413, 1.24096, 1.51862, 1.54938])

        names.append("LShoulderRoll")
        times.append([ 1.00000, 2.52000, 3.04000, 4.08000, 4.96000, 7.00000])
        keys.append([ 0.12268, 0.04138, 0.14569, 0.13955, 0.14722, 0.03993])

        names.append("LWristYaw")
        times.append([ 1.00000, 2.52000, 3.04000, 4.08000, 4.96000, 7.00000])
        keys.append([ 0.08727, 0.07359, 0.05058, 0.06285, -0.05680, -0.00149])

        names.append("RAnklePitch")
        times.append([ 1.04000, 1.76000, 2.56000, 4.12000, 5.00000, 7.16000])
        keys.append([ 0.03226, 0.01745, 0.01745, 0.03491, 0.03491, 0.11501])

        names.append("RAnkleRoll")
        times.append([ 1.04000, 1.76000, 2.56000, 4.12000, 5.00000, 7.16000])
        keys.append([ -0.33161, -0.36652, -0.36652, -0.36652, -0.34732, 0.08433])

        names.append("RElbowRoll")
        times.append([ 1.08000, 2.60000, 3.12000, 4.16000, 5.04000, 7.32000])
        keys.append([ 0.74096, 1.03396, 1.36990, 1.02015, 0.70722, 0.37732])

        names.append("RElbowYaw")
        times.append([ 1.08000, 2.60000, 3.12000, 4.16000, 5.04000, 7.32000])
        keys.append([ 1.15353, 0.95411, 0.90809, 1.23023, 1.55697, 1.14441])

        names.append("RHand")
        times.append([ 1.08000, 2.60000, 3.12000, 4.16000, 5.04000, 7.32000])
        keys.append([ 0.00317, 0.00328, 0.00329, 0.00317, 0.00325, 0.00187])

        names.append("RHipPitch")
        times.append([ 1.04000, 2.56000, 3.08000, 3.36000, 4.12000, 5.00000, 7.16000])
        keys.append([ 0.23159, 0.10580, 0.12217, 0.08433, 0.09046, 0.19171, 0.21020])

        names.append("RHipRoll")
        times.append([ 1.04000, 2.56000, 3.08000, 3.36000, 4.12000, 5.00000, 7.16000])
        keys.append([ 0.34366, 0.36820, 0.36820, 0.36513, 0.36667, 0.36513, -0.10129])

        names.append("RHipYawPitch")
        times.append([ 1.04000, 2.56000, 3.08000, 3.36000, 4.12000, 5.00000, 7.16000])
        keys.append([ -0.18097, -0.25307, -0.06285, -0.05058, -0.18711, -0.24386, -0.31903])

        names.append("RKneePitch")
        times.append([ 1.04000, 1.76000, 2.56000, 3.08000, 3.36000, 4.12000, 5.00000, 7.16000])
        keys.append([ -0.08727, -0.08727, -0.09235, -0.07973, -0.07973, -0.07819, -0.07666, -0.09208])

        names.append("RShoulderPitch")
        times.append([ 1.08000, 2.60000, 3.12000, 4.16000, 5.04000, 7.32000])
        keys.append([ 1.48649, 1.35917, 1.41746, 1.59847, 1.63835, 1.50021])

        names.append("RShoulderRoll")
        times.append([ 1.08000, 2.60000, 3.12000, 4.16000, 5.04000, 7.32000])
        keys.append([ -0.02305, -0.01998, -0.13197, -0.11816, -0.02305, -0.03524])

        names.append("RWristYaw")
        times.append([ 1.08000, 2.60000, 3.12000, 4.16000, 5.04000, 7.32000])
        keys.append([ -0.24435, -0.23935, -0.22094, -0.20253, -0.19026, 0.12736])

        try:
          # uncomment the following line and modify the IP if you use this script outside Choregraphe.
          # motion = ALProxy("ALMotion", IP, 9559)
          motion = ALProxy("ALMotion")
          motion.angleInterpolation(names, keys, times, True);
        except BaseException, err:
          print err

        pass

    def rightKick(self):
        print "Right Kick"
        
        # Choregraphe simplified export in Python.
        
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([ 1.16000, 2.68000, 3.20000, 4.24000, 5.12000, 7.48000])
        keys.append([ 0.04363, 0.26180, 0.17453, -0.27925, -0.26180, -0.24241])

        names.append("HeadYaw")
        times.append([ 1.16000, 2.68000, 3.20000, 4.24000, 5.12000, 7.48000])
        keys.append([ 0.00464, -0.00149, 0.00311, -0.04905, -0.03371, -0.02459])

        names.append("LAnklePitch")
        times.append([ 1.04000, 1.76000, 2.56000, 4.12000, 5.00000, 7.16000])
        keys.append([ 0.03226, 0.01745, 0.01745, 0.03491, 0.03491, 0.11501])

        names.append("LAnkleRoll")
        times.append([ 1.04000, 1.76000, 2.56000, 4.12000, 5.00000, 7.16000])
        keys.append([ 0.33161, 0.36652, 0.36652, 0.36652, 0.34732, -0.08433])

        names.append("LElbowRoll")
        times.append([ 1.08000, 2.60000, 3.12000, 4.16000, 5.04000, 7.32000])
        keys.append([ -0.74096, -1.03396, -1.36990, -1.02015, -0.70722, -0.37732])

        names.append("LElbowYaw")
        times.append([ 1.08000, 2.60000, 3.12000, 4.16000, 5.04000, 7.32000])
        keys.append([ -1.15353, -0.95411, -0.90809, -1.23023, -1.55697, -1.14441])

        names.append("LHand")
        times.append([ 1.08000, 2.60000, 3.12000, 4.16000, 5.04000, 7.32000])
        keys.append([ 0.00317, 0.00328, 0.00329, 0.00317, 0.00325, 0.00187])

        names.append("LHipPitch")
        times.append([ 1.04000, 2.56000, 3.08000, 3.36000, 4.12000, 5.00000, 7.16000])
        keys.append([ 0.23159, 0.10580, 0.12217, 0.08433, 0.09046, 0.19171, 0.21020])

        names.append("LHipRoll")
        times.append([ 1.04000, 2.56000, 3.08000, 3.36000, 4.12000, 5.00000, 7.16000])
        keys.append([ -0.34366, -0.36820, -0.36820, -0.36513, -0.36667, -0.36513, 0.10129])

        names.append("LHipYawPitch")
        times.append([ 1.04000, 2.56000, 3.08000, 3.36000, 4.12000, 5.00000, 7.16000])
        keys.append([ -0.18097, -0.25307, -0.06285, -0.05058, -0.18711, -0.24386, -0.31903])

        names.append("LKneePitch")
        times.append([ 1.04000, 1.76000, 2.56000, 3.08000, 3.36000, 4.12000, 5.00000, 7.16000])
        keys.append([ -0.08727, -0.08727, -0.09235, -0.07973, -0.07973, -0.07819, -0.07666, -0.09208])

        names.append("LShoulderPitch")
        times.append([ 1.08000, 2.60000, 3.12000, 4.16000, 5.04000, 7.32000])
        keys.append([ 1.48649, 1.35917, 1.41746, 1.59847, 1.63835, 1.50021])

        names.append("LShoulderRoll")
        times.append([ 1.08000, 2.60000, 3.12000, 4.16000, 5.04000, 7.32000])
        keys.append([ 0.02305, 0.01998, 0.13197, 0.11816, 0.02305, 0.03524])

        names.append("LWristYaw")
        times.append([ 1.08000, 2.60000, 3.12000, 4.16000, 5.04000, 7.32000])
        keys.append([ 0.24435, 0.23935, 0.22094, 0.20253, 0.19026, -0.12736])

        names.append("RAnklePitch")
        times.append([ 1.04000, 1.32000, 1.76000, 2.24000, 2.56000, 2.84000, 3.08000, 3.36000, 3.68000, 4.12000, 5.00000, 7.16000])
        keys.append([ 0.08727, -0.08727, -0.59341, -0.40143, 0.12217, -0.05236, -0.12217, 0.24435, -0.12217, -0.64403, -0.21991, 0.11356])

        names.append("RAnkleRoll")
        times.append([ 1.04000, 2.56000, 3.08000, 3.36000, 4.12000, 5.00000, 7.16000])
        keys.append([ 0.40143, 0.10887, 0.13802, 0.00000, 0.18097, 0.34558, 0.05066])

        names.append("RElbowRoll")
        times.append([ 1.00000, 2.52000, 3.04000, 4.08000, 4.96000, 7.00000])
        keys.append([ 0.64117, 1.15353, 1.38056, 1.36062, 0.96024, 0.45564])

        names.append("RElbowYaw")
        times.append([ 1.00000, 2.52000, 3.04000, 4.08000, 4.96000, 7.00000])
        keys.append([ 0.99714, 0.86368, 0.90970, 0.63205, 0.84834, 1.49714])

        names.append("RHand")
        times.append([ 1.00000, 2.52000, 3.04000, 4.08000, 4.96000, 7.00000])
        keys.append([ 0.00129, 0.00136, 0.00132, 0.00128, 0.00133, 0.00391])

        names.append("RHipPitch")
        times.append([ 1.04000, 2.56000, 3.08000, 3.36000, 4.12000, 5.00000, 7.16000])
        keys.append([ 0.16265, -0.39726, -1.11876, -1.11978, -0.78540, -0.29142, 0.21318])

        names.append("RHipRoll")
        times.append([ 1.04000, 2.56000, 3.08000, 3.36000, 4.12000, 5.00000, 7.16000])
        keys.append([ -0.47124, -0.54001, -0.32218, -0.12276, -0.36360, -0.41713, -0.05825])

        names.append("RKneePitch")
        times.append([ 1.04000, 2.56000, 2.84000, 3.08000, 3.36000, 4.12000, 5.00000, 7.16000])
        keys.append([ -0.08901, 1.97575, 1.97222, 1.23918, 0.24435, 1.53589, 0.62430, -0.07666])

        names.append("RShoulderPitch")
        times.append([ 1.00000, 2.52000, 3.04000, 4.08000, 4.96000, 7.00000])
        keys.append([ 1.52782, 1.46033, 1.47413, 1.24096, 1.51862, 1.54938])

        names.append("RShoulderRoll")
        times.append([ 1.00000, 2.52000, 3.04000, 4.08000, 4.96000, 7.00000])
        keys.append([ -0.12268, -0.04138, -0.14569, -0.13955, -0.14722, -0.03993])

        names.append("RWristYaw")
        times.append([ 1.00000, 2.52000, 3.04000, 4.08000, 4.96000, 7.00000])
        keys.append([ -0.08727, -0.07359, -0.05058, -0.06285, 0.05680, 0.00149])

        try:
          # uncomment the following line and modify the IP if you use this script outside Choregraphe.
          # motion = ALProxy("ALMotion", IP, 9559)
          motion = ALProxy("ALMotion")
          motion.angleInterpolation(names, keys, times, True);
        except BaseException, err:
          print err

        pass


class GUIMenu:
    def __init__(self):
        
        self.nao = Nao()

        # Tkinter

        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()

    def initUI(self):
      
        self.parent.title("NaoSoccer")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        # First menu column

        standUpButton = Button(self, text="Stand", command=self.nao.standUp)
        standUpButton.place(x=50, y=20)

        sitDownButton = Button(self, text="Sit", command=self.nao.sitDown)
        sitDownButton.place(x=50, y=60)

        crouchButton = Button(self, text="Crouch", command=self.nao.crouch)
        crouchButton.place(x=50, y=100)        

        leftKickButton = Button(self, text="Left Kick", command=self.nao.leftKick)
        leftKickButton.place(x=50, y=140)
        
        rightKickButton = Button(self, text="Right Kick", command=self.nao.rightKick)
        rightKickButton.place(x=50, y=180)

        # Second menu column
        
        turnLeftButton = Button(self, text="Forward (Short)", command=self.nao.moveForwardShort)
        turnLeftButton.place(x=180, y=20)

        turnLeftButton = Button(self, text="Forward (Long)", command=self.nao.moveForwardLong)
        turnLeftButton.place(x=180, y=60)

        turnLeftButton = Button(self, text="Backward", command=self.nao.moveBackward)
        turnLeftButton.place(x=180, y=100)

        turnLeftButton = Button(self, text="Turn Left", command=self.nao.turnLeft)
        turnLeftButton.place(x=180, y=140)

        turnRightButton = Button(self, text="Turn Right", command=self.nao.turnRight)
        turnRightButton.place(x=180, y=180)

        # Stop button

        stopButton = Button(self, text="Stop", command=self.nao.standUp)
        stopButton.place(x=115, y=220)

        # quitButton = Button(self, text="Quit", command=self.quit)
        # quitButton.place(x=50, y=50)

def main():
  
    root = Tk()
    root.geometry("320x240+300+300")
    app = GUIMenu(root)
    root.mainloop()  


if __name__ == '__main__':
    main()