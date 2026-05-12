from controller import Robot

if __name__=='__main__':
    robot = Robot()
    
    timestep = 64
    max_speed = 6.45
    
    # --- تصحيح الأهداف ---
    # 12 راديان تعني حوالي 25 سم (طول مناسب لضلع المربع)
    target_forward = 12.0  
    
    # الدوران 90 درجة يحتاج حوالي 2.0 إلى 2.2
    target_turn = 2.1      
    
    state = "walk"
    
    left_motor = robot.getDevice("left wheel motor")
    right_motor = robot.getDevice("right wheel motor")
    left_motor.setPosition(float("inf"))
    right_motor.setPosition(float("inf"))
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

    right_sensor = robot.getDevice("right wheel sensor")
    right_sensor.enable(timestep)

    left_sensor = robot.getDevice("left wheel sensor")
    left_sensor.enable(timestep)

    # خطوة أولية لضمان قراءة الحساس
    robot.step(timestep)
    start_pos = left_sensor.getValue()
     
    while robot.step(timestep) != -1:
         left_rad = left_sensor.getValue()
         
         # حساب المسافة المقطوعة منذ آخر تصفير
         # (abs) مهمة جداً لأن عند الدوران القيمة قد تتناقص
         current_dist = abs(left_rad - start_pos) 
        
         # طباعة للمراقبة (راقب الـ Console)
         print(f"State: {state} | Goal: {target_forward if state=='walk' else target_turn} | Done: {current_dist:.2f}")  
         
         if state == "walk":
             # اذا لم نصل للهدف (12)، استمر بالمشي
             if current_dist < target_forward:
                 left_speed = 0.5 * max_speed
                 right_speed = 0.5 * max_speed
             else:
                 # وصلنا! توقف وغير الحالة
                 left_speed = 0
                 right_speed = 0
                 start_pos = left_sensor.getValue() # تصفير العداد
                 state = "turn"
                 print(">>> FINISHED WALKING, STARTING TURN")

         elif state == "turn":
             # اذا لم نصل لهدف الدوران (2.1)، استمر بالدوران
             if current_dist < target_turn:
                 left_speed = 0.2 * max_speed   # أبطأ قليلاً للدقة
                 right_speed = -0.2 * max_speed
             else:
                 # انتهى الدوران! ارجع للمشي
                 left_speed = 0
                 right_speed = 0
                 start_pos = left_sensor.getValue() # تصفير العداد
                 state = "walk"
                 print(">>> FINISHED TURN, WALKING STRAIGHT")
          
         left_motor.setVelocity(left_speed)
         right_motor.setVelocity(right_speed)