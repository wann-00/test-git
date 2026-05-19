#ถ้าตัวเลขที่เจอทั้งหมด แต่ละตัวหาร2ลงตัวจะได้เลข0
#โค้ดนี้ผิดอยู่หลายจุดแก้ด้วย
 
nums = [] #ใส่ตัวเลขคำตอบที่เจอทั้งหมด แต่ละตัวคือสมาชิกในarray

lastResult = ""

for i in range(len(nums) - 1):

    n = nums[i]

    if n % 2 != 0:
        lastResult += "0"
    else:
        lastResult += 1

print(lastresult) #คำใบ้ที่แท้จริง