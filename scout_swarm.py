import time
import random

def run_orion_protocol():
    print("🛰️  ORION AI: System Boot Sequence Initialized...")
    time.sleep(1.5)
    print("📡 AETHER: Connecting to Interplanetary Ledger Mesh Network...")
    time.sleep(1)
    print("🟢 STATUS: ScoutBot Swarm active in Lunar Sector Charlie-4.\n")
    
    # Simulate scanning for a water-ice deposits
    for scan_cycle in range(1, 4):
        print(f"🔄 Scanning terrain matrix... Cycle {scan_cycle}/3")
        time.sleep(1)
        
    # Simulate finding high-purity ice
    ice_mass_kg = round(random.uniform(45.5, 120.3), 2)
    print(f"\n🎯 TARGET ACQUIRED: Found Subsurface Water Ice Pocket! Estimated Mass: {ice_mass_kg} kg")
    time.sleep(1)
    
    # Trigger the automated M2M financial transaction
    print("🔗 AETHER: Generating cryptographic Proof-of-Resource token...")
    time.sleep(1.5)
    
    token_payout = round(ice_mass_kg * 1.5, 2)
    print(f"💰 M2M TRANSACTION SUCCESS: Deposited {token_payout} AETHER-Fuel Credits into local Swarm Wallet.")
    print("🚀 Next Directive: Relaying coordinates to ProcessBot-Alpha for extraction.")

if __name__ == "__main__":
    run_orion_protocol()