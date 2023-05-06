print("""\033[33m                                                    
   !YYGJ??????????????????????????G7   
   !G:^G.                          5?   
   ?5 ^G:                          57   
   7P ^G:              :::::.      57   
   7P ^G:       ..   ^^^7~:^!7.    57   
   7P ^G:      ^~^  ^! .:^:  ~5.   57   
   7P ^G:     ^~. .!..7~..:!.^Y~   57   
   7P ^G:       .^??:^~^~  !^!J.   57   
   7P ^G:    .^^^JY5?^!:7^^7YJ     57   
   7P ^G:   ^~^:^~^^^^^~!7777.     57   
   7P ^G:  !7~~~!!!!~^::..         57   
   7P ^G: .7!~^:..                 57   
   7P ^G:                          57   
   7P ^G.                          57   
   75 ^G.                          P?   
   7P7JPJ????????????????????????YJP!   
   7B!. ........................5Y:.    
   ~G:                          P7      
    !YJ?????????????????????????5B5J^\033[0m""")
print("====================================================")
print("Time Calculator for Bitcoin Brute forcing private keys")
print("Developed by: Corvus Codex - https://github.com/CorvusCodex")
print("Support my work:")
print("BTC: bc1q7wth254atug2p4v9j3krk9kauc0ehys2u8tgg3")
print("ETH: 0x68B6D33Ad1A3e0aFaDA60d6ADf8594601BE492F0")
print("====================================================")
def calculate_time_to_crack(num_keys_per_min):
    total_possible_keys = 2**256
    keys_per_second = num_keys_per_min / 60
    time_to_crack_seconds = total_possible_keys / keys_per_second
    time_to_crack_years = time_to_crack_seconds / (60 * 60 * 24 * 365)
    return time_to_crack_years

num_keys_per_min = float(input("Enter the number of private keys generated per minute: "))
time_to_crack = calculate_time_to_crack(num_keys_per_min)
print("====================================================")
print(f"The approximate time to crack a Bitcoin address is {time_to_crack:.2f} years.")
print("====================================================")
print("You think calculation is not correct? Sorry, but the calculation is correct. The number of possible private keys for a Bitcoin address is extremely large (2^256), so even with a very high rate of private key generation (1 billion per minute), it would still take an incredibly long time to crack a Bitcoin address by brute force. This is one of the reasons why Bitcoin is considered to be secure.")
print("====================================================")
