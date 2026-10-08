# ====================================================================
# SOVEREIGN NEURAL LABS // MASTER BACKEND ANALYTICS ENGINE
# ENGINE TYPE: DATABASE QUERY AGGREGATOR // STATUS: ISOLATED PRODUCTION
# ====================================================================

import sqlite3

DB_FILE = "sovereignty.db"

def query_historical_ledger():
    """
    Connects to sovereignty.db and outputs a parsed analytical summary
    of all saved logs currently committed to the data directories.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Select active records inside the vetting ledger
        cursor.execute("""
            SELECT entry_id, timestamp, asset_token, tdi_ratio, silence_spikes, system_verdict 
            FROM vetting_ledger 
            ORDER BY entry_id ASC;
        """)
        records = cursor.fetchall()
        conn.close()
        
        if not records:
            print("\n[DATABASE QUERY LOG] STATUS: CLEAR // NO HISTORICAL MATRIX DATA FOUND.")
            return

        print("\n" + "="*80)
        print(" SOVEREIGN NEURAL LABS // HISTORICAL DATA ARCHIVE READOUT")
        print("="*80)
        print(f"{'ID':<4} | {'TIMESTAMP':<19} | {'ASSET IDENTIFIER':<18} | {'TDI':<5} | {'SILENCE':<7} | {'VERDICT':<15}")
        print("-"*80)
        
        purged_count = 0
        total_records = len(records)
        
        for row in records:
            entry_id, timestamp, token, tdi, silence, verdict = row
            if verdict == "PURGED_EJECTED":
                purged_count += 1
            print(f"{entry_id:<4} | {timestamp:<19} | {token:<18} | {tdi:<5.2f} | {silence:<7} | {verdict:<15}")
            
        print("-"*80)
        print(f"[SUMMARY METRICS] TOTAL ENTRIES COMPILED: {total_records}")
        print(f"[SUMMARY METRICS] SECURITY THREATS PURGED: {purged_count}")
        print("="*80 + "\n")
        
    except sqlite3.OperationalError:
        print("\n[DATABASE ERROR] SYSTEM ALERT: VETTING_LEDGER TABLE DOES NOT EXIST IN CACHE.")

if __name__ == "__main__":
    query_historical_ledger()
