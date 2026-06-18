class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        vech = (360/12*hour + 360/12/60*minutes)%360
        vecm = (360/60*minutes)%360
        return min(abs(vech-vecm),abs(vecm-vech),abs(vech-vecm-360),abs(vecm-vech-360))
        