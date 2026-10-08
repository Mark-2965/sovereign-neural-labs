-- ====================================================================
-- SOVEREIGN NEURAL LABS // MASTER RELATIONAL ENTERPRISE ARCHITECTURE
-- TARGET DATABASE: POSTGRESQL // STATUS: PRODUCTION PRIMED
-- ====================================================================

-- 1. TABLE: global_agency_nodes (Tracks your structural empire pipeline infrastructure)
CREATE TABLE global_agency_nodes (
    node_id SERIAL PRIMARY KEY,
    node_name VARCHAR(50) NOT NULL UNIQUE, -- 'LAGOS_EXECUTION', 'ACCRA_INFERENCE', 'GLOBAL_SOURCING'
    region VARCHAR(50) NOT NULL,
    active_status BOOLEAN DEFAULT TRUE,
    last_sync_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. TABLE: behavioral_vetting_ledger (Logs the diagnostics index metrics over sprints)
CREATE TABLE behavioral_vetting_ledger (
    entry_id SERIAL PRIMARY KEY,
    asset_identifier VARCHAR(50) NOT NULL, -- Anonymous unique hashing token for the vetting asset
    sprint_day_marker INT NOT NULL,         -- Day 30, Day 90, Day 180 checkpoint tracking
    tdi_ratio DECIMAL(4,2) NOT NULL,       -- Transactional Density Index (Resource Extracted / Value Injected)
    latency_spikes_count INT DEFAULT 0,    -- Sudden blocks of unexplained communication silence
    integrity_status VARCHAR(20) DEFAULT 'SANDBOX_VETTING', -- 'SANDBOX_VETTING', 'APPROVED', 'PURGED_EJECTED'
    log_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. TABLE: industrial_client_metrics (Relational database hook for shilzy-studio-pro workspace variables)
CREATE TABLE industrial_client_metrics (
    client_id SERIAL PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    bust_dimension_mm INT NOT NULL,
    waist_dimension_mm INT NOT NULL,
    hips_dimension_mm INT NOT NULL,
    last_calibration_date DATE NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
