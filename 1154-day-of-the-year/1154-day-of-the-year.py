class Solution(object):
    def dayOfYear(self, date):
        d = {
            '01':0, '02':31, '03':59, '04':90,
            '05':120, '06':151, '07':181, '08':212,
            '09':243, '10':273, '11':304, '12':334
            }
        x = int(date[:4])
        a = 1 if ((not x%4 and x%100) or not x%400) and int(date[5:7])>2 else 0
        a += d[date[5:7]]
        a += int(date[-2:])
        return a