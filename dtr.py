day = 1
TWH = 0
TU = 0
TL = 0
for i in range(5):
hrs_in = int(input("HOURS IN: "))
min_in = int(input("MINUTES IN: "))
print("")
hrs_out = int(input("HOURS OUT: "))
min_out = int(input("MINUTES OUT: "))
print("------------------------")
print("Day", day)
print(f"am in = {hrs_in}:{min_in}")
print(f"am out = {hrs_out}:{min_out}")
TI = hrs_in * 60 + min_in #Make the time into minutes for easier computation
TO = hrs_out * 60 + min_out

# TIME IN NOT LATE
if TI >= 300 and TI <= 450: # 5am-7:30am
   L = 0
# TIME IN LATE
if TI > 450 and TI < 721: # 7:31am - 12am
   L = TI - 450

#---------------------------------------------------
if TO >= 690 and TO <=721: # 11:30am - 12am
   UT = 0
if TO < 690: # 11:29am and below
   UT = 690 - TO

if L >= 0 and L <= 240:
   LH = L // 60
   LM = L % 60
if UT >= 0 and UT <= 240:
   UH = UT // 60
   UM = UT % 60

Hrswork = 240 - (L + UT)
HWH = Hrswork // 60
HWM = Hrswork % 60
print(f"Hours work = {HWH}:{HWM}") # HOURS WORK
print(f"late = {LH}:{LM}")
print(f"undertime = {UH}:{UM}")
print("------------------------")
day = day + 1
TWH = TWH + Hrswork # TO GET THE TOTAL HOURS WORK
TL = TL + L # TO GET THE TOTAL LATE
TU = TU + UT # TO GET THE TOTAL UNDERTIME
#---------------------------------------------------
print("--------TOTAL--------")
TWH_H = TWH // 60 # Total Hours work in hours form
TWH_M = TWH % 60 # Total Hours work in minutes form
TL_H = TL // 60 # Total late in hours form
TL_M = TL % 60 # Total late in minutes form
TU_H = TU // 60 # Total undertime in hours form
TU_M = TU % 60 # Total undertime in minutes form
WS = TWH / 60 * 100
FWS = round(WS, 2)
print(f"Total Hours work = {TWH_H}:{TWH_M}       WEEKLY SALARIES:{FWS}")
print(f"Total late = {TL_H}:{TL_M}")
print(f"Total undertime = {TU_H}:{TU_M}")
