import math

def solution(w,h):
    # w, h의 최대공약수
    k = math.gcd(w, h)
    
    # 제거되는 사각형의 수
    del_box = ((w+h)//k -1)*k
      
    return w*h - del_box
  
