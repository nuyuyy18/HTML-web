import sys
import time

def menjalankan_lirik () :
    lirik = [
         ("Up's the only direction I see", 0.08),
         ("As long as we keep this", 0.08),
         ("Low-low-low-low, low-low-low lowkey (Ah, ah)", 0.08),
         ("You ain't even gotta lo-lo-lo-lo", 0.08),
         ("Lo-lo-lo-love me (Ah, ah)", 0.08),
         ("Us in a king-size, keep it a secret", 0.08),
         ("Say I'm your queen, I don't wanna leave this", 0.08),
         ("Low-low-low-low, low-low-low lowkey", 0.08),
    ]

    delay = [0.3, 0.3, 0.4, 1, 0.2, 0.4, 0.3]
    print("\nLowkey - Niki")
    time.sleep(2)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i]) 
        print('')   
    print("// code by Nurul Azizah")  


menjalankan_lirik ()    

