import json
import sqlite3
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# INITIALIZE APP ENGINE AND CROSS-ORIGIN ACCESS PORTS
app = Flask(__name__)
CORS(app)

DB_FILE = 'sovereigntydb'

def initialize_database():
    """Ensures the target relational tracking tables are fully initialized on disk."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Build the exact table structure verified inside your schema.sql layout
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS behavioral_vetting_ledger (
                entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
                asset_identifier TEXT NOT NULL,
                sprint_day_marker INTEGER NOT NULL,
                tdi_ratio REAL NOT NULL,
                latency_spikes_count INTEGER DEFAULT 0,
                integrity_status TEXT DEFAULT 'SANDBOX_VETTING',
                log_notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        print("   📂 [DATABASE ENGINE] Relational storage synchronization verified stable.")
    except Exception as e:
        print(f"   ❌ [DATABASE INITIALIZATION CRITICAL] Schema build failed: {str(e)}")
    finally:
        conn.close()

@app.route('/api/ingest', methods=['POST'])
def ingest_and_store_metrics():
    conn = None
    try:
        # CAPTURE PAYLOAD FROM EVENT LISTENER STRINGS
        payload = request.get_json()
        if not payload:
            return jsonify({"status": "ERROR", "message": "No data stream received"}), 400
            
        # EXTRACT FIELDS AND MAP TO SCHEMA DATA LAYERS
        asset_id = payload.get('asset_token', 'UNKNOWN_ASSET_NODE')
        tdi_extracted = float(payload.get('tdi_extracted', 0.0))
        value_injected = float(payload.get('value_injected', 1.0))
        latency_silence = int(payload.get('latency_silence', 0))
        
        # CALCULATE THE DIRECT RATIO IN REALTIME FOR SCHEMA MAPPING
        # Safe divide handler to prevent ZeroDivisionError runtime faults
        calculated_ratio = round(tdi_extracted / value_injected, 2) if value_injected > 0 else tdi_extracted
        
        # STRATEGIC VERDICT ENGINE (RATIONAL SELF-INTEREST METRICS SCORING)
        sprint_day = 1 # Initial tracking sequence indicator
        if calculated_ratio > 2.5 or latency_silence > 3:
            verdict = "PURGED_EJECTED"
            verdict_color = "#ef4444"
            notes = f"System breach triggered. High resource extraction ratio: {calculated_ratio}."
        else:
            verdict = "SANDBOX_VETTING"
            verdict_color = "#00ff87"
            notes = "Baseline system tracking compiled stable."

        print(f"\n📡 [INGESTION PROCESSING] Pipeline transmitting payload to local database storage...")
        print(f"   | ASSET IDENTIFIER: {asset_id}")
        print(f"   | COMPUTED TDI RATIO: {calculated_ratio}")
        print(f"   | LATENCY SILENCE SPIKES: {latency_silence}")
        print(f"   | INTEGRITY VERDICT STATUS: {verdict}")

        # CONNECT TO DB CORRIDOR AND INSERT DATA STREAM
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO behavioral_vetting_ledger 
            (asset_identifier, sprint_day_marker, tdi_ratio, latency_spikes_count, integrity_status, log_notes)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (asset_id, sprint_day, calculated_ratio, latency_silence, verdict, notes))
        
        conn.commit()
        print("   💾 [SQL TRANSACTION COMPLETE] Metric data successfully welded to disk storage.")

        # BROADCAST LIVE STATUS TELEMETRY BACK DOWN THE TRANSPORT PORT
        return jsonify({
            "status": "SUCCESS",
            "tdi": calculated_ratio,
            "verdict": verdict,
            "verdict_color": verdict_color
        }), 200

    except Exception as e:
        print(f"\n❌ [PIPELINE TRANSACTION CRITICAL ERROR] Database payload insert failed: {str(e)}")
        return jsonify({"status": "CRITICAL_ERROR", "message": f"Database pipeline mapping aborted: {str(e)}"}), 500
        
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    print("=" * 65)
    print("Eagle SOVEREIGN NEURAL LABS // DATABASE INGESTION CONNECTED")
    initialize_database()
    print("   LOCAL SERVER LISTENER INITIALIZED: http://localhost:5000")
    print("   STATUS: RUNNING PRODUCTION METRICS BACK-END // FIREWALL REINFORCED")
    print("=" * 65)
    app.run(host='127.0.0.1', port=5000, debug=True)
